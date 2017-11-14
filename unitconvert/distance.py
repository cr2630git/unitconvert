"""
A simple python module for converting kilometers to miles or vice versa.
So simple that it doesn't even have any dependencies.
"""

def kilometers_to_miles(dist_in_km):
	"""
	Actually does the conversion of distance from km to mi.
	
	PARAMETERS
	--------
	dist_in_km: float
		A distance in kilometers.
	
	RETURNS	
	-------
	dist_in_mi: float
		The same distance converted to miles.
	"""

	
	return (dist_in_km)/1.609344


def miles_to_kilometers(dist_in_mi):
	"""
	Actually does the conversion of distance from mi to km.
	
	PARAMETERS
	----------
	dist_in_mi: float
		A distance to miles.

	RETURNS
	-------
	dist_in_km: float
		The same distance converted to kilometers.
	"""

	return (dist_in_mi)*1.609344
