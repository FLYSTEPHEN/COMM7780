from geopy.geocoders import Nominatim
from geopy.distance import great_circle
#from geopy.distance import vincenty
geolocator=Nominatim(user_agent="my-application")

a=input("Starting point:")
b=input("Destination:")

exa=geolocator.geocode(b)
exb=geolocator.geocode(a)

loc_a=(exa.latitude,exa.longitude)
loc_b=(exb.latitude,exb.longitude)

gcd=great_circle(loc_a,loc_b).kilometers
#v=vincenty(loc_a,loc_b).kilometers

distance=round(gcd,1)
#distance=round(v,1)

print('The great circle distance between %s and %s is %s kilometers'%(exa,exb,distance))
#print('The vincenty distance between %s and %s is %s kilometers'%(a,b,v))
