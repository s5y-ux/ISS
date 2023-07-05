'''
********************************************************************************
*                                                                              *
* Project Start Date: 07/03/2023                                               *
* Project End Date: 07/04/2023                                                  *
*                                                                              *
* License: https://opensource.org/license/mit/                                 *
*                                                                              *
* Programmed By: Joseph R. Shumaker                                            *
*                                                                              *
* Purpose: This project was made as a reference library for some of my         *
* Co-Workers at the LRC (Learning Resource Center) where we hope to use        *
* the data in this API wrapper to create a robot that points at the ISS.       *
* The code in this project is protected under the MIT Licensing Agreement      *
* and by using this software you agree not to break any laws regarding         *
* communications with the application server or abuse such services.    	   *
*                                                                              *
* All code seen below is my original work and all information regarding the    *
* use of library-specific methods and attributes were learned directly from    *
* the libraries' documentation.                                                *
*                                                                              *
* If you have any questions or would like to get in contact with me, my email  *
* and phone number is listed below...                                          *
*                                                                              *
* Phone: (805) 701 - 3171                                                      *
*                                                                              *
* Email: josephshumaker11@gmail.com                                            *
*                                                                              *
********************************************************************************
'''

import urllib.request
import json
import pandas

'''
urllib.request: Used to probe HTTPS for JASON Data
Documentation: https://urllib3.readthedocs.io/en/stable/user-guide.html

json: Used to parse the Data from urllib
Documentation: https://docs.python.org/3/library/json.html

pandas: Used to parse data for use in plotly (Could have used standard dictionaries but, better practices yk?)
Documentation: https://pandas.pydata.org/docs/
'''

#Function for calling API through URL
def Request(URLparameter: str) -> dict:

	#Stores JSON data in 'Response' variable
	Response = urllib.request.urlopen(URLparameter)

	#Parses data as dictionary and returns dict (Notice Return Data Type)
	Result = json.loads(Response.read())
	return(Result)

#Function for returning DataFrame including all data from API
def AllISSData() -> pandas.DataFrame():

	#Calls 'Request' function with URL for ISS positional data 
	ReferenceLocation = Request("http://api.open-notify.org/iss-now.json")

	#Creates empty dictionary variable and updates with various Key/Value pairs for DataFrame
	LocationalDictionary = dict();
	LocationalDictionary.update({"timestamp":ReferenceLocation["timestamp"], 
		"message":ReferenceLocation["message"], "latitude": ReferenceLocation["iss_position"]["latitude"],
		"longitude": ReferenceLocation["iss_position"]["longitude"]})

	#Create and return DataFrame with Dictionary data 
	ReferenceFrame = pandas.DataFrame(LocationalDictionary, [0])
	return(ReferenceFrame)

#Function used for quick positional data in DataFrame
def PositionalData() -> pandas.DataFrame():

	#Calls 'Request' function with URL for ISS positional data 
	ReferenceLocation = Request("http://api.open-notify.org/iss-now.json")["iss_position"]

	#Creates empty dictionary variable and updates with various Key/Value pairs for DataFrame
	LocationalDictionary = dict();
	LocationalDictionary.update({"latitude": ReferenceLocation["latitude"],
		"longitude": ReferenceLocation["longitude"]})

	#Create and return DataFrame with Dictionary data 
	ReferenceFrame = pandas.DataFrame(LocationalDictionary, [0])
	return(ReferenceFrame)

#Function used for returning DataFrame with all of the Astronauts included
def AstronautData() -> pandas.DataFrame():

	#Calls 'Request' function with URL for Astronaut data 
	ReferenceData = Request("http://api.open-notify.org/astros.json")['people']

	#Variable to hold enumerable data
	data = [[], []]

	#Loop to gather and store data
	for dictionaries in ReferenceData:
		data[0].append(dictionaries['name'])
		data[1].append(dictionaries['craft'])

	#Reference dictionary
	referenceDict = {"name": data[0], "craft": data[1]}

	#Store and return DataFrame
	Astronauts = pandas.DataFrame(referenceDict)
	return(Astronauts)

#Attribute for quick real time Longitude
Longitude = Request("http://api.open-notify.org/iss-now.json")["iss_position"]["longitude"]

#Attribute for quick real time Latitude
Latitude = Request("http://api.open-notify.org/iss-now.json")["iss_position"]["longitude"]

#Quick function to test if the data is retrievable
Ping = lambda: print("{0}, {1}".format(Request("http://api.open-notify.org/iss-now.json")["message"], 
	Request("http://api.open-notify.org/iss-now.json")["timestamp"]))