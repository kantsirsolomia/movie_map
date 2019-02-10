import folium
from geopy.geocoders import Nominatim
import csv
from geopy.extra.rate_limiter import RateLimiter


def user_input():
    year = input(
        "Enter a year to found out some info on places where was filmed movies at this year: ")
    return year


def location_from_csv():
    """
    ()-> list
    Opens and reads a csv file, returns locations of the movies
    that were filmed in the year, entered by user
    """
    limit = 0
    locations_list = []
    year = user_input()
    with open('locations.csv', 'r') as csvFile:
        reader = csv.reader(csvFile)
        for line in reader:
            limit += 1
            # limit counts lines that have been checked in the file
            if year in line:
                location = line[-1]
                locations_list.append(location)
                # if limit >= 1000:  # limit prevents from "Service timed out" error
    return locations_list


def location_to_coordinates(city):
    """
    Returns coordinates out of location.
    >>> print(location_to_coordinates("London"))
    (51.5073219, -0.1276474, 'London, Greater London, England, SW1A 2DU, UK')
    """
    try:
        geolocator = Nominatim(user_agent="map_1")
        geocode = RateLimiter(geolocator.geocode, min_delay_seconds=1)
        location = geolocator.geocode(city)
        coordinates_tuple = (
            location.latitude, location.longitude, location.address)
        return coordinates_tuple
    except AttributeError:
        new = city.split()
        loc = new[-2] + ' ' + new[-1]
        geolocator = Nominatim(user_agent="map_1")
        geocode = RateLimiter(geolocator.geocode, min_delay_seconds=1)
        location = geolocator.geocode(loc)
        coordinates_tuple = (
            location.latitude, location.longitude, location.address)
        return coordinates_tuple


def markers(funct):
    """
    lst, lst, lst -> str
    Creates the map, takes coordinates and name and makes the marker on the map.

    """
    lat = funct[0]
    lon = funct[1]
    name = funct[2]
    map = folium.Map(location=[49.817545, 24.023932], zoom_start=10)
    fg = folium.FeatureGroup(name='Movie map')
    for lt, ln, name1 in zip(lat, lon, name):
        fg.add_child(folium.Marker(
            location=[lt, ln],  popup=name1, icon=folium.Icon()))

    fg_pp = folium.FeatureGroup(name="Population")

    fg_pp.add_child(folium.GeoJson(data=open('world.json', 'r',
                                             encoding='utf-8-sig').read(),
                                   style_function=lambda x: {'fillColor': 'green'
                                                             if x['properties']['POP2005'] < 10000000
                                                             else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000
                                                             else 'red'}))
    map.add_child(fg)
    map.add_child(fg_pp)
    map.add_child(folium.LayerControl())
    map.save('solomia.html')


def function_join():
    """
    () -> str
    Joins all the functions and provides correct cooperation of
    functions
    """
    city = location_from_csv()
    print("Wait a minute.....")
    final_lat = []
    final_lon = []
    final_name = []
    for place in city:
        coordinates = location_to_coordinates(place)

        final_lat.append(coordinates[0])
        final_lon.append(coordinates[1])
        final_name.append(coordinates[2])
    tuple_for_map = (final_lat, final_lon, final_name)

    markers(tuple_for_map)
    print("Find a html file 'solomia.html' on your computer and open it OR copy\
 and paste this link: file:///Users/solomiakantsir/Desktop/2семестр/solomia.html")


function_join()
