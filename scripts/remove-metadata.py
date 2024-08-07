import sys
import gpxpy

def remove_timestamps(gpx):
    for track in gpx.tracks:
        track.name = None
        track.type = None
        for segment in track.segments:
            for point in segment.points:
                point.time = None

def process(gpx_data):
    gpx = gpxpy.parse(gpx_data)
    remove_timestamps(gpx)
    return gpx.to_xml()

def main():
    gpx_data = sys.stdin.read()
    print(
       process(gpx_data) 
    )
    
if __name__ == "__main__":
    main()