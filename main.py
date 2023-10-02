import phonenumbers
from phonenumbers import geocoder, carrier
import folium
from opencage.geocoder import OpenCageGeocode

# Replace 'your_phone_number_here' with the phone number you want to lookup
phone_number = "+923214383141"

# Parse the phone number
pep_number = phonenumbers.parse(phone_number)

# Get the location information
location = geocoder.description_for_number(pep_number, "en")
print("Location:", location)

# Get the carrier information
service_provider = carrier.name_for_number(pep_number, "en")
print("Service Provider:", service_provider)

# Set your OpenCage API key
opencage_key = '4da1a9675d634febb6ad57f03c1ab992'

# Initialize the OpenCageGeocode instance
geocoder = OpenCageGeocode(opencage_key)

# Get the geolocation (latitude and longitude) for the location
query = str(location)
results = geocoder.geocode(query)

# Check if results were found
if results:
    lat = results[0]['geometry']['lat']
    lng = results[0]['geometry']['lng']
    print("Latitude:", lat)
    print("Longitude:", lng)

    # Create a map
    my_map = folium.Map(location=[lat, lng], zoom_start=9)

    # Add a marker to the map
    folium.Marker([lat, lng], popup=location).add_to(my_map)

    # Save the map to an HTML file
    my_map.save('irbaz.html')
else:
    print("Location not found.")
