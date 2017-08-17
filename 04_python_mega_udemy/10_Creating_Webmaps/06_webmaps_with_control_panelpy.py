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


def add_volcano_markers(locations):
    """
    Requires COORD variable:
             COORD = 3 integer values, lat, lon, elevation

    OUTPUT: Creates coordinates with popup value using
        Folium feature group.
    """
    # FEATURE GROUP DEFINITION:
    # >> main, volcanoes & population

    # main_fg = folium.FeatureGroup(name="Nik's Map")
    volcano_fg = folium.FeatureGroup(name="Volcanoes")
    population_fg = folium.FeatureGroup(name="Population")

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

    # CREATE INSTANCE OF MAP
    mymap = folium.Map(location=center,
                       # tiles="Stamen Terrain",
                       tiles="Mapbox Bright",
                       zoom_start=5)

    # CHOROPLETH FOR POPULATION
    population_fg.add_child(folium.GeoJson(
                 geo_j_data,
                 style_function=lambda x: {
                    'fillColor': 'white' if x['properties']['POP2005'] < 1000000
                    else 'blue' if 10000000 <= x['properties']['POP2005'] < 20000000
                    else 'black'}))

    # POPULATION OF VOLCANOES & ELEVATION COLORS
    for lt, ln, el in COORD:
        volcano_fg.add_child(folium.CircleMarker(
            location=[lt, ln],
            popup=("Volcano Elevation: %s meters" % el),
            fill_color=elev_color(el),
            radius=5.5,
            color="white",
            weight=1.0,
            fill_opacity=0.7))

    # Add feature groups as defined above
    # mymap.add_child(main_fg)
    mymap.add_child(population_fg)
    mymap.add_child(volcano_fg)

    # Add map control panel
    mymap.add_child(folium.LayerControl())
    mymap.save("Map8.html")


add_volcano_markers(COORD)
