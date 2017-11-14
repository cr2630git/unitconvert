"""
A simple python module for converting Fahrenheit to Celsius or vice versa.
So simple that it doesn't even have any dependencies.
"""

def fahrenheit_to_celsius(temp_in_f):
	"""
	Actually does the conversion of temperature from F to C.
	
	PARAMETERS
	--------
	temp_in_f: float
		A temperature in degrees Fahrenheit.
	
	RETURNS	
	-------
	temp_in_c: float
		The same temperature converted to degrees Celsius.
	"""

	
	return (temp_in_f-32)*5/9


def celsius_to_fahrenheit(temp_in_c):
	"""
	Actually does the conversion of temperature from C to F.
	
	PARAMETERS
	----------
	temp_in_c: float
		A temperature in degrees Celsius.

	RETURNS
	-------
	temp_in_f: float
		The same temperature converted to degrees Fahrenheit.
	"""

	return (9/5*temp_in_c)+32
