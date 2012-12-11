#!/usr/bin/env python
from settings import *
import datetime
import flask
import json
import os
import pdb
import platform
import sys

# FIXME: lame submodule import
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
git_sub_modules = BASE_DIR+'/healthvault' # Relative paths ok too
for dir in os.listdir(git_sub_modules):
    path = os.path.join(git_sub_modules, dir)
    if not path in sys.path:
        sys.path.append(path)

from healthvault import HVConn

# Are we running on AppFog? (imprecise)
AF_P = False
AF_PLATFORM = 'Linux-3.2.0-23-virtual-x86_64-with-Ubuntu-12.04-precise'
if platform.platform() == AF_PLATFORM:
    AF_P = True
    SERVER_NAME = 'smart-hv-patient.aws.af.cm'
else:
    SERVER_NAME = 'localhost'

# Note: using ./app for both the templates and static files
# AF needs "application" here
application = app = flask.Flask(
    'wsgi',
    static_folder='app',
    static_url_path='/static',
    template_folder='app'
)
app.debug = True
app.config['SERVER_NAME'] = SERVER_NAME

# Routes
@app.route('/')
def redirect_to_hv_login():
    # Note: redirect in qs is only for non-production use
    # only otherwise action_url in app metadata is used
    return flask.redirect(HV_SHELL_URL +
             "/redirect.aspx?target=AUTH&targetqs=?appid=" +
             APP_ID + "%26redirect=http://"+app.config['SERVER_NAME'] +
             "/mvaultaction")

@app.route('/mvaultaction')
def mvaultaction():
    target = flask.request.args.get('target','')
    if target == 'AppAuthSuccess':
        args = flask.request.args
        wctoken = args.get('wctoken', '')
        if not wctoken:
            return "Couldn't get wctoken from HealthVault! Aborting."

        hvconn = HVConn(wctoken)

        return flask.render_template(
            'main.html',
            wctoken=wctoken,
            name=hvconn.person.name,
            person_id=hvconn.person.person_id,
            selected_record_id=hvconn.person.selected_record_id,
            auth_token=hvconn._auth_token,
            shared_secret=hvconn._shared_secret
        )
    else:
        return 'Did not get AppAuthSuccess from HealthVault! Aborting.'

    # TODO: more responses here
    #if target == "Home":
        #return HttpResponseRedirect('/')

@app.route('/getGlucoseMeasurements')
def getGlucoseMeasurements():
    g = flask.request.args.get
    hvconn = HVConn(user_auth_token=g('wctoken'),
                    record_id=g('record_id'),
                    auth_token=g('auth_token'),
                    shared_secret=g('shared_secret'),
                    get_person_info_p=False)
    hvconn.getGlucoseMeasurements()
    # don't use flask's builtin jsonify function... it creates
    # one big dict not an array for these
    resp = flask.make_response()
    resp.data = json.dumps(hvconn.person.glucoses)
    resp.mimetype = 'application/json'
    return resp

@app.route('/newGlucoseMeasurement')
def newGlucoseMeasurement():
    pass
    #params = json.loads(request.raw_post_data)
    #hvconn = HVConn(params['wctoken'])
    #dt = datetime.datetime(
            #params['year'],
            #params['month'],
            #params['day'],
            #params['hours24'],
            #params['minutes'],
            #0)

    ## convert mg_dl to mmolPerL
    #if params['unit'] == 'mg_dl':
        #value = params['value'] / 18
    #else:
        #value = params['value']

    #hvconn.newGlucoseMeasurement(dt, value, params['whole_or_plasma'])
    #return HttpResponse(json.dumps('ok'), mimetype='application/json')

# Run on port 80 for consistency with AF
if __name__ == '__main__':
    app.run(port=80)
