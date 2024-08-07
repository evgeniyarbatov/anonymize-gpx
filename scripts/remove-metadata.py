import sys
import gpxpy

def remove_metadata(gpx):
    (
        gpx.name, 
        gpx.creator, 
        gpx.description, 
        gpx.time,
        gpx.bounds,
    ) = (
        None,
        None,
        None,
        None,
        None,
    )
    for track in gpx.tracks:
        track.name, track.type = None, None
        for segment in track.segments:
            for point in segment.points:
                point.time, point.elevation = None, None
                point.extensions = None

def process(gpx_data):
    gpx = gpxpy.parse(gpx_data)
    remove_metadata(gpx)
    return gpx.to_xml()

def main():
    gpx_data = sys.stdin.read()
    print(
       process(gpx_data) 
    )
    
if __name__ == "__main__":
    main()