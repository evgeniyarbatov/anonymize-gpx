import sys
import gpxpy
import random

def shuffle_points(gpx):
    for track in gpx.tracks:
        for segment in track.segments:
            random.shuffle(segment.points)

def process(gpx_data):
    gpx = gpxpy.parse(gpx_data)
    shuffle_points(gpx)
    return gpx.to_xml()

def main():
    gpx_data = sys.stdin.read()
    print(
       process(gpx_data) 
    )
    
if __name__ == "__main__":
    main()