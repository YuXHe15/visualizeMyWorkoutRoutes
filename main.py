from load import load_gpx_files
from plot import plot_tracks

tracks = load_gpx_files()
plot_tracks(tracks=tracks)
