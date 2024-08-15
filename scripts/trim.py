import sys
import gpxpy

from utils import log, get_config

DISTANCE = get_config('distance_to_trim')

def trim(gpx):
    for track in gpx.tracks:
        for segment in track.segments:
            distances = [0.0]
            for i in range(1, len(segment.points)):
                previous_point = segment.points[i-1]
                current_point = segment.points[i]
                
                distance = distances[-1] + previous_point.distance_2d(current_point)
                distances.append(distance)
            
            end_distance = distances[-1] - DISTANCE
            start_index = next(i for i, d in enumerate(distances) if d >= DISTANCE)
            end_index = next(i for i, d in enumerate(distances) if d >= end_distance)
            
            segment.points = segment.points[start_index:end_index]

def process(filename, gpx_data):
    original_gpx = gpxpy.parse(gpx_data)
    edited_gpx = gpxpy.parse(gpx_data)
    
    trim(edited_gpx)
    log(filename, original_gpx, edited_gpx, 'trim')
    
    return edited_gpx.to_xml()

def main(args):
    filename = args[0]
    
    gpx_data = sys.stdin.read()
    print(
       process(filename, gpx_data) 
    )
    
if __name__ == "__main__":
    main(sys.argv[1:])