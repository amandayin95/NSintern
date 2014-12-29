NSintern
========
this python file uses urllib2 and json library to enable JSON file parsing.

Question:

In Technology data is key in making critical decisions and having too little or duplicate data may generate mislead reports. Using the City of Seattle's API, https://data.seattle.gov, develop process for continually polling/ collecting available dataset(s).
It’s not enough just to have rich data, but you must able to quickly visualize in meaning full way. Use the data previously collected to create visualizations.


Language: python 

Example:
Road Weather Information Stations (the information updates every 15 minutes)
http://dev.socrata.com/foundry/#/data.seattle.gov/egc4-d24i

first I created a base_url that just contains the API, 
then allow some interaction with the user, mostly to filter through the data, and retrieve only what the user wants, (the same logic applies to multiple parameters, just using & to connect them.)
then load the json file. 
In python we would be able to get a list of dictionaries.

I imported the time module as well, so that
For every fifteen minutes passed, check the datasets again, update it. (To enhance accuracy: record the current “updated_at” time, initially check every one minute, until the data updates, then check every 15 minutes, in this way we will be able to narrow down our “lag-behind” error within one minute window)

Then for each member in the dictionary that satisfies the requirement, put the road/air temperature value in the lists that I built before, named user_wanted_road and user_wanted_air seperately. This is also an advantage of list over array in that it is easier to change the length of a list.

In addition, before the for loop started I created a variable that serves as a time reference. 
This is sort of like "visited" in the searching mechanisms, in this case, I only add the temperature to the list if and only if the 'datetime' of that data member is bigger than (after) the reference. (Which means that it is a NEW DATA) This is to avoid duplicating the data over and over again, which would take up both unecessarily longer runtime and waste a lot of memory. 
This is also useful if the publisher deletes the oldest information when he updates it every 15 minutes, it allows us to keep track of the previous information that might be no longer available in the current call of that API.

An alternate way is to authenticate and then manipulate the data. I did not include that in my file.




After having the data we want, I think there can be two general ways of visualizing it.

First is to make horizontal comparison. That is, to compare the temerature across a number of different roads. In that case when we retrieve the data we can make the url += '&datetime=2014-04-08UTC13:00:00Z' and loop through the resulted dictionary in the same logic as we just did. 

Second is to make vertical comparison, that is, to get a trend line of the temperature of a specific road, which is what we see in the python file. The trick of that is to avoid stack overflow.

I imported the numpy library to get arrays from lists and get ready to parse them as x and y axis 
The matplotlib takes in the processed result of numpy library and then make it into a graph.



