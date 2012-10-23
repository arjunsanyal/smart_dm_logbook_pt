from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.shortcuts import render_to_response, redirect
from healthvault import HVConn
from settings import *

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
        return HttpResponseRedirect('/start?' + \
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

def start(request):
    target = request.GET['target']
    wctoken = ""
    if target == "AppAuthSuccess":
        wctoken = request.GET['wctoken']
    else:
        return HttpResponse("cannot get wctoken")

    hvconn = HVConn(wctoken)
    hvconn.getPersonInfo()
    hvconn.getWeightMeasurements()

    #import pdb; pdb.set_trace()

    template_values = {
        'name': hvconn.person.name,
        'weights': hvconn.person.weights
    }
    return render_to_response('start.html', template_values)

