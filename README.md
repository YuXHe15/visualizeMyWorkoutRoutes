# A Cool Way To Visualize Apple Fitness Workout Routes
## Intro
An easy tool to make a cool visualization of Apple Fitness Workout Routes. not been tested on data from other brands but any ```.gpx``` routes should work.
## Config
config everything in ```config.toml```. Default is:
```toml
[visualization]
line_width = 1.5
line_color = [157, 250, 0]
background_color = [59, 59, 59]
grid_size = 20
output_file = "tracks_visualization.png"

[paths]
gpx_folder = "/path/to/your/gpx/files"
output_file = "/path/to/output/tracks_visualization.png"
```

## Install
Just ```pip install -r requirements.txt```

## Use
Run ```main.py```

## Results
![image](/tracks_visualization.png)

### Add any text you like below:

![imageWithText](/B7316522-B5D7-4E4C-A6FD-E566A8230227_1_201_a.jpeg)


