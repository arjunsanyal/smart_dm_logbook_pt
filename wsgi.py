
import datetime
import flask
import json
import os
import pdb
import platform
import settings
import sys

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(BASE_DIR + '/healthvault/healthvault')
import healthvault


# Some PaaS (including AppFog) need application here
application = app = flask.Flask(
    'wsgi',
    static_folder='app',  # use ./app for templates and static files
    static_url_path='/static',
    template_folder='app'
)
app.debug = settings.DEBUG


# Routes
@app.route('/')
def redirect_to_hv_login():
    # Note: redirect in qs is only for non-production use
    # only otherwise action_url in app metadata is used
    return flask.redirect(
        settings.HV_SHELL_URL +
        "/redirect.aspx?target=AUTH&targetqs=?appid=" +
        settings.APP_ID +
        "%26redirect=http://" +
        settings.SERVER_NAME +
        ":" +
        str(settings.PORT) +
        "/mvaultaction"
    )


@app.route('/mvaultaction')
def mvaultaction():
    target = flask.request.args.get('target', '')
    if target == 'AppAuthSuccess':
        args = flask.request.args
        wctoken = args.get('wctoken', '')
        if not wctoken:
            return "Couldn't get wctoken from HealthVault! Aborting."

        hvconn = healthvault.HVConn(wctoken)

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
    hvconn = healthvault.HVConn(
        user_auth_token=g('wctoken'),
        record_id=g('record_id'),
        auth_token=g('auth_token'),
        shared_secret=g('shared_secret'),
        get_person_info_p=False
    )

    hvconn.getGlucoseMeasurements()

    # Don't use flask's builtin jsonify function; we want an array
    resp = flask.make_response()
    resp.data = json.dumps(hvconn.person.glucoses)
    resp.mimetype = 'application/json'
    return resp


@app.route('/newGlucoseMeasurement', methods=['POST'])
def newGlucoseMeasurement():
    # flask.request.form is empty, but we have .data (string) and .json
    g = flask.request.json
    hvconn = healthvault.HVConn(user_auth_token=g['wctoken'])
    dt = datetime.datetime(
        g['year'],
        g['month'],
        g['day'],
        g['hours24'],
        g['minutes'],
        0
    )

    # convert mg_dl to mmolPerL
    if g['unit'] == 'mg_dl':
        value = g['value'] / 18
    else:
        value = g['value']

    try:
        hvconn.newGlucoseMeasurement(dt, value, g['whole_or_plasma'])
    except:
        app.logger.error('Coudn\'t post newGlucoseMeasurement!')

    # Don't use flask's builtin jsonify function; we want an array
    resp = flask.make_response()
    resp.data = json.dumps('ok')
    resp.mimetype = 'application/json'
    return resp


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=settings.PORT)
