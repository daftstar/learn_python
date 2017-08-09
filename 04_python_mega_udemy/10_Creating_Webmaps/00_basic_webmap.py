import folium


# ['CircleMarker', 'ClickForMarker', 'ColorMap', 'CssLink', 'CustomIcon',
# 'Div', 'DivIcon', 'Element', 'FeatureGroup', 'Figure', 'FitBounds',
# 'GeoJson', 'Html', 'IFrame', 'Icon', 'JavascriptLink', 'LatLngPopup',
# 'LayerControl', 'LinearColormap', 'Link', 'MacroElement', 'Map',
# 'Marker', 'MarkerCluster', 'PolyLine', 'Popup', 'RegularPolygonMarker',
# 'StepColormap', 'TileLayer', 'TopoJson', 'Vega', 'WmsTileLayer',
# '__all__', '__builtins__', '__cached__', '__doc__', '__file__',
# '__loader__', '__name__', '__package__', '__path__', '__spec__',
# '__version__', 'absolute_import', 'features', 'folium', 'map']


# create a map object   # Latitude = -90 to 90, long = -180, 180
# map = folium.Map(location=[38.58, -99.09])

# Create HTML map
# map.save("Map1.html")

# Add zoom parameters
# map = folium.Map(location=[38.58, -99.09], zoom_start=6)
# map.save("Map1.html")

# Change map background styling
map = folium.Map(
                location=[38.58, -99.09],
                zoom_start=6,
                tiles="Mapbox Bright")

map.save("Map1.html")

# Add point markers
map.add_child(folium.Marker(
                location=[38.2, -99.1],
                popup="Here I am!",
                icon=folium.Icon(color="green")))


map.save("Map1.html")
