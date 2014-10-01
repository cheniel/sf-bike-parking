# json keys from original data are bad... see data:
# http://data.sfgov.org/resource/w969-5mn4.json

class Result:
	
	def __init__(self, result):
		self.priority = 0

		self.address = result['yr_inst']
		self.location = result['addr_num']
		self.longitude = float(result['latitude']['longitude'])
		self.latitude = float(result['latitude']['latitude'])

		self.yearInstalled = result['yr_installed']
		self.numRacks = result['racks']
		self.spaces = result['spaces']
		self.placement = result['placement']

		self.distanceFromUser = None

	def setPriority(self, priority):
		self.priority = priority

	def setDistanceFromUser(self, latitude, longitude):
		latDiff = latitude - self.latitude
		lonDiff = longitude - self.longitude
		self.distanceFromUser = latDiff * latDiff + lonDiff * lonDiff

	def __unicode__(self):
		return self.address + " " + self.location + " (" + self.longitude + ", " + self.latitude + ")"


