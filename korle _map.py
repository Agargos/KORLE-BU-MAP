import folium  # Import the folium library for map creation

# Step 1: Define the coordinates (latitude, longitude) of Korle Bu Teaching Hospital
korle_bu_coords = (5.543432, -0.221929)

# Step 2: Create a folium map object centered on the hospital location
# The zoom_start parameter sets the initial zoom level (higher = closer)
map_korle_bu = folium.Map(location=korle_bu_coords, zoom_start=17)

# Step 3: Add a marker to indicate the location of the hospital
folium.Marker(
    location=korle_bu_coords,  # Coordinates of the marker
    popup='Korle Bu Teaching Hospital',  # Text that shows when you click the marker
    icon=folium.Icon(color='red', icon='plus')  # Icon color and symbol
).add_to(map_korle_bu)  # Add the marker to the map

# Step 4: Save the map to an HTML file so it can be opened in a web browser
map_korle_bu.save('korle_bu_map.html')

print("Map has been created and saved as 'korle_bu_map.html'")