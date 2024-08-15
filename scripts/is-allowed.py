import sys
import gpxpy

LOCATIONS = [
    (1.130475, 1.450475, 103.609168, 104.029168), # Singapore
]

def is_within_box(point, min_lat, max_lat, min_lon, max_lon):
    return min_lat <= point.latitude <= max_lat and min_lon <= point.longitude <= max_lon

def is_location_allowed(gpx):
    for track in gpx.tracks:
        for segment in track.segments:
            start = segment.points[0]
            stop = segment.points[-1]   
            for location in LOCATIONS:
                min_lat, max_lat, min_lon, max_lon = location
                if (
                    is_within_box(start,  min_lat, max_lat, min_lon, max_lon)
                    and is_within_box(stop , min_lat, max_lat, min_lon, max_lon)
                ):
                    return True
    return False

def is_allowed(gpx_data):
    try:
        gpx = gpxpy.parse(gpx_data)
    except gpxpy.gpx.GPXException:
        return False
    
    is_allowed = is_location_allowed(gpx)
    
    return is_allowed

def main(args):
    filename = args[0]

    gpx_data = open(filename, 'r')

    sys.exit(0 if is_allowed(gpx_data) else 1)
    
if __name__ == "__main__":
    main(sys.argv[1:])