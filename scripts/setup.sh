apt-get update && apt-get install -y python3-opencv
jupyter nbextension install --py --symlink --sys-prefix ipyleaflet
jupyter nbextension enable --py --sys-prefix ipyleaflet
pip install leafmap
pip install segment-geospatial
pip install --find-links=https://girder.github.io/large_image_wheels --no-cache GDAL
pip install localtileserver
pip install opencv-python
