Description
- - - - - -
The module "map.py" is destined for finding out some information on movies that
have been filmed in particular year. This module includes next functions:
1.user_input() - offers the user to make an input - year
2.location_from_csv() - opens and reads a csv file, find locations of the movies
that were filmed in year, entered by user
3.location_to_coordinates(city) - takes an argument - location and change it into
coordinates
4.markers(funct) - creates the map, takes an argument(coordinates and name) and
make the marker of this place on the map; creates an additional layer with info
on population.
5.function_join() - joins all the functions and provides correct cooperation of
functions.
To find out information about films and locations I used "location.csv" file.

Description of structure of html tags
- - - - - - - - - - - - - - - - - - -
A html code consists of:
<*head*> - tells the technical info on file; it includes:
<*meta*> - determines metatags, that have a service info for browsers and searching
systems;
<*script*> - intended for scripts description;
<*link*> - makes a connection with outer document;
<*style*> - determines a style of web-page elements;
<*body*> - determines a body of the document.

Conclusion
- - - - - -
The map provides some information on such important things like:
1.country and city, where were filmed movies, which were filmed in the year, entered
by user;
The user enters a year and there appear markers on the map, where movies were made.
These markers also include information about location.
2.population
Countries on the map are colored green if their population is less than 10000000,
orange if population is more than or equals 10000000 but less than 20000000, and red in another case.

As a result, the map has three layers - Open street map, population and movies.
The user has a Layer Control.

Additional
- - - - - - 
You need to install flask and geopy to use my code.
