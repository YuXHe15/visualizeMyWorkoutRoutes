import gpxpy
import os
import toml

config = toml.load("config.toml")
paths_config = config["paths"]
gpx_folder = paths_config["gpx_folder"]


def load_gpx_files():
    tracks = []
    for file_name in os.listdir(gpx_folder):
        if file_name.endswith(".gpx"):
            with open(os.path.join(gpx_folder, file_name), "r") as gpx_file:
                gpx = gpxpy.parse(gpx_file)
                for track in gpx.tracks:
                    for segment in track.segments:
                        latitudes = [point.latitude for point in segment.points]
                        longitudes = [point.longitude for point in segment.points]
                        if latitudes and longitudes:
                            tracks.append((latitudes, longitudes))
    return tracks
