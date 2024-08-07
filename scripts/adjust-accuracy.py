import sys
import gpxpy

def adjust_accuracy(gpx):
    for track in gpx.tracks:
        for segment in track.segments:
            for point in segment.points:
                point.latitude = round(point.latitude, 6)
                point.longitude = round(point.longitude, 6)

def process(gpx_data):
    gpx = gpxpy.parse(gpx_data)
    adjust_accuracy(gpx)
    return gpx.to_xml()

def main():
    gpx_data = sys.stdin.read()
    print(
       process(gpx_data) 
    )
    
if __name__ == "__main__":
    main()


