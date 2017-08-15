import folium
import pandas as pd
from statistics import mean

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
center = [mean(LAT), mean(LON)]
# for lat, lon, elevation in COORD:
#     print ([lat, lon], elevation)



fg = folium.FeatureGroup(name="Nik's Map")
mymap = folium.Map(location=center,
                   tiles="Stamen Terrain",
                   zoom_start=5)


def add_lots(locations):
    """
    Requires COORD variable:
             COORD = 3 integer values, lat, lon, elevation

    OUTPUT: Creates coordinates with popup value using
        Folium feature group.
    """
    def elev_color(elevation):
        """
        helper function that takes in elevation value from coordinates
        and outputs color based on range value
        """
        if elevation < 1000:
            return 'orange'
        elif elevation < 3000:
            return "blue"
        else:
            return "black"

    for lt, ln, el in COORD:
        fg.add_child(folium.CircleMarker(
            location=[lt, ln],
            popup=("elevation: %s meters" % el),
            fill_color=elev_color(el),
            # icon=folium.Icon(color=elev_color(el)),
            radius=8,
            color="yellow",
            fill_opacity=0.7))
    mymap.add_child(fg)
    mymap.save("Map5.html")


add_lots(COORD)

# n