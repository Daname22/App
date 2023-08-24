from geopy.distance import geodesic
from geopy.geocoders import Nominatim

def locationfind():
    geolocator = Nominatim(user_agent="WHERERU")

    location1 = geolocator.geocode(input("Enter your city: "))
    location2 = geolocator.geocode(input("Enter the city you wish to calculate: "))
    

    print("Is this the correct address?")
    print(location1.address)

    local1 = (location1.latitude, location1.longitude)
    local2 = (location2.latitude, location2.longitude)

    print(f"Here are your Longitude and latitude for {location1}: ")
    print(local1)
    print(f"Here are your longitude and latitude for {location2}")
    print(local2)

    print(geodesic(local1,local2).miles)

locationfind()

'''

l1,l2 = locationfind()
print("!!!!!This the distance!!!!")
print(geodesic(l1,l2).miles)
    '''