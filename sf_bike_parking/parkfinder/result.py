# json keys from original data are bad... see data:
# http://data.sfgov.org/resource/w969-5mn4.json

class Result:
	
	def __init__(self, result):
		self.address = result['yr_inst']
		self.location = result['addr_num']
		self.longitude = result['latitude']['longitude']
		self.latitude = result['latitude']['latitude']

		self.yearInstalled = result['yr_installed']
		self.numRacks = result['racks']
		self.spaces = result['spaces']
		self.placement = result['placement']

	def __str__(self):
		return self.address + " " + self.location + " (" + self.longitude + ", " + self.latitude + ")"


