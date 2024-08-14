import sys
import gpxpy

from utils import log

def process(filename, gpx_data):
    original_gpx = gpxpy.parse(gpx_data)
    edited_gpx = gpxpy.parse(gpx_data)
    
    edited_gpx.simplify()
    log(filename, original_gpx, edited_gpx, 'simplify')
    
    return edited_gpx.to_xml()

def main(args):
    filename = args[0]
    
    gpx_data = sys.stdin.read()
    print(
       process(filename, gpx_data) 
    )
    
if __name__ == "__main__":
    main(sys.argv[1:])