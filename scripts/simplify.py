import sys
import gpxpy

from utils import log

def process(gpx_data):
    gpx = gpxpy.parse(gpx_data)
    
    gpx.simplify()
    log(gpx, 'simplify')
    
    return gpx.to_xml()

def main():
    gpx_data = sys.stdin.read()
    print(
       process(gpx_data) 
    )
    
if __name__ == "__main__":
    main()