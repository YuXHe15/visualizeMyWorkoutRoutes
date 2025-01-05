import matplotlib.pyplot as plt
from scipy.signal import savgol_filter
import numpy as np
import toml

config = toml.load("config.toml")
visualization_config = config["visualization"]
paths_config = config["paths"]
output_file = paths_config["output_file"]

line_width = visualization_config["line_width"]
line_color = tuple(c / 255 for c in visualization_config["line_color"])
background_color = tuple(c / 255 for c in visualization_config["background_color"])
grid_size = visualization_config["grid_size"]


def smooth_track(latitudes, longitudes, window_size=9, poly_order=2):
    if len(latitudes) > window_size:
        latitudes = savgol_filter(latitudes, window_size, poly_order)
        longitudes = savgol_filter(longitudes, window_size, poly_order)
    return latitudes, longitudes


def normalize_track(latitudes, longitudes):
    if not latitudes or not longitudes:
        return None, None
    latitudes, longitudes = smooth_track(latitudes, longitudes)
    min_lat, max_lat = min(latitudes), max(latitudes)
    min_lon, max_lon = min(longitudes), max(longitudes)
    latitudes = (np.array(latitudes) - min_lat) / (max_lat - min_lat)
    longitudes = (np.array(longitudes) - min_lon) / (max_lon - min_lon)
    return latitudes, longitudes


def plot_tracks(tracks, grid_size=grid_size, output_file=output_file):

    fig, axes = plt.subplots(grid_size, grid_size, figsize=(20, 20))
    axes = axes.flatten()
    fig.patch.set_facecolor(background_color)

    for idx, ax in enumerate(axes):
        if idx < len(tracks):
            latitudes, longitudes = tracks[idx]
            if latitudes and longitudes:
                norm_lat, norm_lon = normalize_track(latitudes, longitudes)
                if norm_lat is not None and norm_lon is not None:
                    ax.plot(norm_lon, norm_lat, linewidth=line_width, color=line_color)
        ax.axis("off")

    plt.subplots_adjust(left=0.05, right=0.95, top=0.95, bottom=0.05)
    plt.savefig(output_file, dpi=300, facecolor=fig.get_facecolor())
    plt.show()
