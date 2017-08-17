from statistics import mean
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

# geo_k_data contains polygon info for all countries
geo_j_data = open("data/world.json", "r", encoding="utf-8-sig")
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
                   # tiles="Stamen Terrain",
                   tiles="Mapbox Bright",
                   zoom_start=5)


fg.add_child(folium.GeoJson(geo_j_data))


def add_volcano_markers(locations):
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
            return 'yellow'
        elif elevation < 3000:
            return "blue"
        else:
            return "black"

    for lt, ln, el in COORD:
        fg.add_child(folium.CircleMarker(
            location=[lt, ln],
            popup=("elevation: %s meters" % el),
            fill_color=elev_color(el),
            radius=5.5,
            color="white",
            weight=1.0,
            fill_opacity=0.7))
    mymap.add_child(fg)
    mymap.save("Map6.html")


add_volcano_markers(COORD)
