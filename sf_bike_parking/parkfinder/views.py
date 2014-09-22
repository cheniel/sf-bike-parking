from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader

def index(request):
	template = loader.get_template('parkfinder/index.html')
	context = RequestContext(request, {
		'latitude': request.GET.get('latitude', None),
		'longitude': request.GET.get('longitude', None),
	})
	return HttpResponse(template.render(context))

def results(request, latitude, longitude):
	template = loader.get_template('parkfinder/results.html')
	form = cgi.FieldStorage()
	context = RequestContext(request, {
		'latitude': latitude,
		'longitude': longitude,
	})
	return HttpResponse(template.render(context))
