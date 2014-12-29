
#shuopeng yin

from urllib2 import urlopen
from json import load
import numpy as np # to create 1D arrays (scalar) for charts and graphs
import matplotlib.pyplot as plt # uses 1D arrays to make graphs
import time # for constant update of the information

# base url https://data.seattle.gov/resource/e8hy-uiwc.json
base_url = 'https://data.seattle.gov/resource/e8hy-uiwc.json'

# Now we have the base url, let the user decide which station's information they would like to retrieve

# A='35thAveSW_SWMyrtleSt'
# B='AlaskanWayViaduct_KingSt'
# C='AlbroPlaceAirportWay'
# D='AuroraBridge'
# E='HarborAveUpperNorthBridge'
# F='MagnoliaBridge'
# G='NE45StViaduct'
# H='RooseveltWay_NE80thSt'
# I='SpokaneSwingBridge'

user_wanted_road=[]
user_wanted_air = []

stationName_userInput =
raw_input('which station would you like to query? 35thAveSW_SWMyrtleSt; AlaskanWayViaduct_KingSt; AlbroPlaceAirportWay; AuroraBridge; HarborAveUpperNorthBridge; MagnoliaBridge; NE45StViaduct; RooseveltWay_NE80thSt; SpokaneSwingBridge;')

# our consomized user request
url = base_url+ '?stationname=' + stationName_userInput
response = urlopen(url)
json_obj = load(response)
# the json array loads into a python list, inside it is a number of dictionaries with keys being "field names"

time_ref = json_obj[0]['datetime'] # serve as reference, records the most current time of the temperature

roadOrAir_userInput = raw_input('what temperature would you like to plot? roadsurfacetemperature, airtemeprature, or both?')
if roadOrAir_userInput = 'roadsurfacetemperature':
    for data in json_obj:  #json object is a list, each member inside is a dictionary
        if data['datetime']>time_ref:
            time_ref =data['datetime']
           user_wanted_road.append(data['roadsurfacetemperature'])
if roadOrAir_userInput = 'airtemperature':
    for data in json_obj:  #json object is a list, each member inside is a dictionarys
            if data['datetime']>time_ref:
            time_ref =data['datetime']
           user_wanted_air.append(data['airtemperature'])
if roadOrAir_userInput = 'both':
    while true:
        for data in json_obj:  #json object is a list, each member inside is a dictionary
            if data['datetime']>time_ref:
                time_ref =data['datetime']
               user_wanted_road.append(data['roadsurfacetemperature'])
               user_wanted_air.append(data['airtemperature'])
                time.sleep(900)
                
#Suppose the user input is both

# now we do the indexing
# x -axis
x_axis = np.array(range(len(user_wanted_road)))
# lists vs. arrays: numpy is faster if we want to do math
# the reason we use lists in the beginning: easy to grow in size, hence easy to update
# y-axis the numpy version of the list user_wanted_road
y_axis_road = np.array(user_wanted_road)

# now we do the plotting –line graph
plt.plot(x_axis, y_axis_road, color = 'blue', linestyle = solid, lable= 'road temperature')
plt.plot(x_axis, y_axis_air, color = 'green', linestyle = solid, lable= 'air temperature')
plt.legend(loc = 'upper right' )#show legend
plt.title('temperature information')

# histogram or bar graph horizontal comparison
plt.hist(user_wanted_bargraph)
plt.bar(user_wanted_bargraph)



#ensure that the date updates constantly
time.sleep(900) # execute every 15 minutes
#run the update
