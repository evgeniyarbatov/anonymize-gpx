import os
import glob
import shutil
import sys

import matplotlib.pyplot as plt
import contextily as ctx

from utils import parse_gpx, get_output_path

MAPS_DIR = 'maps'

def make_map(df, filename):
    plt.figure(figsize=(15, 8))
    plt.plot(df['longitude'], df['latitude'], color='red', label='Route')
    ctx.add_basemap(plt.gca(), crs='EPSG:4326', source=ctx.providers.OpenStreetMap.Mapnik)
    plt.legend()
    plt.xticks([], [])
    plt.yticks([], [])
    plt.tick_params(axis='both', which='both', bottom=False, top=False, left=False, right=False)
    plt.savefig(filename, bbox_inches='tight', pad_inches=0)

def main(args):
    gpx_dir = args[0]

    maps_dir = os.path.join(gpx_dir, MAPS_DIR)
    if os.path.exists(maps_dir):
        shutil.rmtree(maps_dir)
    os.makedirs(maps_dir)

    gpx_files = glob.glob(
        os.path.join(gpx_dir, '*.gpx')
    )
    for gpx_file in gpx_files:
        df = parse_gpx(gpx_file)
        
        output_path = get_output_path(maps_dir, gpx_file, 'png')
        make_map(df, output_path)

if __name__ == "__main__":
    main(sys.argv[1:])