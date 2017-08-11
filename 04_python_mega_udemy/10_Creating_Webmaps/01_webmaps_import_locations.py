import folium
import pandas as pd

# ['CircleMarker', 'ClickForMarker', 'ColorMap', 'CssLink', 'CustomIcon',
# 'Div', 'DivIcon', 'Element', 'FeatureGroup', 'Figure', 'FitBounds',
# 'GeoJson', 'Html', 'IFrame', 'Icon', 'JavascriptLink', 'LatLngPopup',
# 'LayerControl', 'LinearColormap', 'Link', 'MacroElement', 'Map',
# 'Marker', 'MarkerCluster', 'PolyLine', 'Popup', 'RegularPolygonMarker',
# 'StepColormap', 'TileLayer', 'TopoJson', 'Vega', 'WmsTileLayer',
# '__all__', '__builtins__', '__cached__', '__doc__', '__file__',
# '__loader__', '__name__', '__package__', '__path__', '__spec__',
# '__version__', 'absolute_import', 'features', 'folium', 'map']

data = pd.read_csv("data/Volcanoes.txt")

LAT = [lat for lat in data["LAT"]]
LON = [lon for lon in data["LON"]]
COORD = map(list, zip(LAT, LON))

# print (COORD)
# for i in COORD:
#     print (i)


map = folium.Map(tiles="Mapbox Bright", zoom_start=6)

fg = folium.FeatureGroup(name="Nik's Map")


def add_lots(locations):
    for loc in locations:
        fg.add_child(folium.Marker(
            location=loc,
            popup="I'm a marker",
            icon=folium.Icon(color="red")))
        map.add_child(fg)
    map.save("Map3.html")


add_lots(COORD)

