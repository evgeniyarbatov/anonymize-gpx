import sys
import gpxpy

def remove_timestamps(gpx):
    for track in gpx.tracks:
        for segment in track.segments:
            for point in segment.points:
                point.time = None

def read_gpx(file_path):
    with open(file_path, 'r') as file:
        gpx = gpxpy.parse(file)
    return gpx

def write_gpx(gpx, output_file_path):
    with open(output_file_path, 'w') as file:
        file.write(gpx.to_xml())

def process_file(input_file, output_file):
    gpx = read_gpx(input_file)
    remove_timestamps(gpx)
    write_gpx(gpx, output_file)

if __name__ == "__main__":
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    process_file(input_file, output_file)
