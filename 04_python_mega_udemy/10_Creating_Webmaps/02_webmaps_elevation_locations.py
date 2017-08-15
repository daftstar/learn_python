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

LAT = list(data["LAT"])
LON = list(data["LON"])
ELEV = list(data["ELEV"])

COORD = zip(LAT, LON, ELEV)
# for lat, lon, elevation in COORD:
#     print ([lat, lon], elevation)



fg = folium.FeatureGroup(name="Nik's Map")
mymap = folium.Map(tiles="Mapbox Bright", zoom_start=3)


def add_lots(locations):
    """
    Requires COORD variable:
             COORD = 3 integer values, lat, lon, elevation
    
    OUTPUT: Creates coordinates with popup value using
        Folium feature group.
    """
    for lt, ln, el in COORD:
        fg.add_child(folium.Marker(
            location=[lt, ln],
            popup=("elevation: %s" % el),
            icon=folium.Icon(color="black")))
        mymap.add_child(fg)
    mymap.save("Map4.html")


add_lots(COORD)

