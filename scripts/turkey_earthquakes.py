import time
from uuid import uuid4
import json
import sagemaker_geospatial_map

# data obtained from https://geojson-maps.ash.ms/
def add_world(earthquakes_map):
    f = open('data/world-vector.json')
    earth_data = json.load(f)
    dataset_id=str(uuid4())
    earthquakes_map.add_dataset(
        {
            'id': dataset_id,
            'label': 'Earth',
            'data': earth_data,
            'color': [127, 127, 127]
        },
        auto_create_layers = True
    )

# Data obtained from https://earthquake.usgs.gov/earthquakes/search/
# 4.5+ magnitude earthquakes in the region defined by:
# maxlatitude=41.354, minlatitude=33.688, maxlongitude=45.264, minlongitude=26.191
# between 1950 and May 2023
def add_earthquakes(earthquakes_map):
    f = open('data/turkey-earthquakes-1950-4.5m.json')
    turkey_earthquakes = json.load(f)
    dataset_id=str(uuid4())
    earthquakes_map.add_dataset(
        {
            'id': dataset_id,
            'label': 'Turkey Earthquakes',
            'data': turkey_earthquakes,
            'color': [255,0,0]
        },
        auto_create_layers = True
    )

def visualize_turkey_earthquakes(earthquakes_map):
    add_world(earthquakes_map)
    add_earthquakes(earthquakes_map)

    
# Example - adding a layer
# earthquakes_map.add_layer({
#     'id': 'earthquake_points',
#     'type': 'point',
#     'data_id': dataset_id,
#     'label': 'Earthquakes',
#     'fields': {
#         'lat': 'Latitude',
#         'lng': 'Longitude'
#     },
#     'is_visible': True,
#     'config': {
#         'visual_channels': {
#             'colorField': {'name': 'Depth', 'type': 'real'}
#         }
        
#     }
# })