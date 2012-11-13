from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.shortcuts import render_to_response, redirect
from healthvault import HVConn
from settings import *
import datetime
import json
import pdb

def index(request):
    """ Redirect to the HealthVault login which on completion of a
        successful login will redirect the browser to the APP_ACTION_URL. """
    # TODO: check this: note: redirect in qs is only for non-production use
    # only otherwise action_url in app metadata is used
    return redirect(HV_SHELL_URL + \
             "/redirect.aspx?target=AUTH&targetqs=?appid=" + \
             APP_ID + \
             "%26redirect=" + \
             APP_ACTION_URL)

def mvaultaction(request):
    # TODO: clean this up
    target = ''
    if request.GET.has_key('target'):
        target = request.GET['target']
    else:
        return HttpResponse('')

    if target == "Home":
        return HttpResponseRedirect('/')
    if target == "AppAuthSuccess":
        return HttpResponseRedirect('/main?' + \
                request.META['QUERY_STRING'])
    if target == "ServiceAgreement":
        return HttpResponseRedirect('/YouAPPTermsOfService.html')
    if target == "Help":
        return HttpResponseRedirect('/YourAppHelp.html')
    if target == "Privacy":
        return HttpResponseRedirect('/YourAppPrivacy.html')
    if target == "AppAuthReject":
        return HttpResponseRedirect('/')
    if target == "SelectedRecordChanged":
        return HttpResponseRedirect('/')
    if target == "ShareRecordSuccess":
        return HttpResponseRedirect('/')
    if target == "ShareRecordFailed":
        return HttpResponseRedirect('/')
    if target == "SignOut":
        return HttpResponseRedirect('/')
    return HttpResponse('')

def main(request):
    target = request.GET['target']
    wctoken = ""
    if target == "AppAuthSuccess":
        wctoken = request.GET['wctoken']
    else:
        return HttpResponse("cannot get wctoken")

    hvconn = HVConn(wctoken)

    template_values = {
        'wctoken': wctoken,
        'name': hvconn.person.name
    }
    return render_to_response('main.html', template_values)

def getPersonInfo(request):
    hvconn = HVConn(request.GET['wctoken'])
    hvconn.getPersonInfo()
    res = {'name': hvconn.person.name }
    return HttpResponse(json.dumps(res), mimetype='application/json')

def getWeightMeasurements(request):
    hvconn = HVConn(request.GET['wctoken'])
    hvconn.getWeightMeasurements()
    res = hvconn.person.weights
    return HttpResponse(json.dumps(res), mimetype='application/json')

def getGlucoseMeasurements(request):
    hvconn = HVConn(request.GET['wctoken'])
    hvconn.getGlucoseMeasurements()
    res = hvconn.person.glucoses
    return HttpResponse(json.dumps(res), mimetype='application/json')

def newGlucoseMeasurement(request):
    params = json.loads(request.raw_post_data)
    hvconn = HVConn(params['wctoken'])
    dt = datetime.datetime(
            params['year'],
            params['month'],
            params['day'],
            params['hours24'],
            params['minutes'],
            0)

    # convert mg_dl to mmolPerL
    if params['unit'] == 'mg_dl':
        value = params['value'] / 18
    else:
        value = params['value']

    hvconn.newGlucoseMeasurement(dt, value, params['whole_or_plasma'])
    return HttpResponse(json.dumps('ok'), mimetype='application/json')
