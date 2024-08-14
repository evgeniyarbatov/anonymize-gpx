import sys
import gpxpy

from utils import log

def adjust_accuracy(gpx):
    for track in gpx.tracks:
        for segment in track.segments:
            for point in segment.points:
                point.latitude = round(point.latitude, 6)
                point.longitude = round(point.longitude, 6)

def process(filename, gpx_data):
    original_gpx = gpxpy.parse(gpx_data)
    edited_gpx = gpxpy.parse(gpx_data)
    
    adjust_accuracy(edited_gpx)
    log(filename, original_gpx, edited_gpx, 'adjust-accuracy')
    
    return edited_gpx.to_xml()

def main(args):
    filename = args[0]
    
    gpx_data = sys.stdin.read()
    print(
       process(filename, gpx_data) 
    )
    
if __name__ == "__main__":
    main(sys.argv[1:])