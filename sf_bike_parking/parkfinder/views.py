from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader
from parkfinder.result import Result
import urllib2
import json


# source:https://data.sfgov.org/Transportation/Bicycle-Parking-Public-/w969-5mn4
API_URL="http://data.sfgov.org/resource/w969-5mn4.json?";
SEARCH_RANGE=.1 # miles
MI_PER_LATITUDE=69.11 
MI_PER_LONGITUDE=68.69 # specific to SF area
LAT_OFFSET=SEARCH_RANGE/MI_PER_LATITUDE
LON_OFFSET=SEARCH_RANGE/MI_PER_LONGITUDE
RESULT_LIMIT=10

def index(request):
	template = loader.get_template('parkfinder/index.html')
	latitude = request.GET.get('latitude', None)
	longitude = request.GET.get('longitude', None)
	street = request.GET.get('street', None)
	query = None
	results = None

	if ((latitude and longitude) or street):
		try:
			if street:
				query = createStreetQuery(street)
			else:
				query = createLocationQuery(float(latitude), float(longitude))
			results = getResults(query)
		except ValueError:
			print "Query was not valid, not searching for results."
			latitude = ""
			longitude = ""

	context = RequestContext(request, {
		'latitude': latitude,
		'longitude': longitude,
		'street': street,
		'rawDataLink': query,
		'results' : results
	})

	return HttpResponse(template.render(context))

def createLocationQuery(latitude, longitude):
	lat_low = latitude - LAT_OFFSET
	lat_high = latitude + LAT_OFFSET
	lon_low = longitude - LON_OFFSET
	lon_high = longitude + LON_OFFSET
	
	query=API_URL
	query+="$limit=" + str(RESULT_LIMIT)
	query+="&$where=within_box(latitude,"+str(lat_high)+","+str(lon_low)+","+str(lat_low)+","+str(lon_high)+")"

	return query

def createStreetQuery(street):
	query=API_URL
	query+="&$where=street_name='" + str(street) + "'"

	return query

def getResults(query):
	jsonResults = None
	results = []

	try:
		resultPage = urllib2.urlopen(query)	
		jsonResults = json.load(resultPage)
		resultPage.close()
		
		order = 1
		for result in jsonResults:
			newResult = Result(result)
			newResult.setPriority(order)
			results.append(newResult)
			order += 1

	except urllib2.HTTPError, e:
	    print "HTTPError when retrieving results"
	except urllib2.URLError, e:
	    print "URLError when retrieving results"



	return results
