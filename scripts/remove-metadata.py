import sys
import re
import gpxpy

def remove_xml_tags(xml):
    return re.sub(
        r'<metadata>.*?</metadata>\s*', 
        '', 
        xml,
        flags=re.DOTALL,
    )

def remove_metadata(gpx):
    gpx.creator = None
    for track in gpx.tracks:
        track.name, track.type = None, None
        for segment in track.segments:
            for point in segment.points:
                point.time, point.elevation = None, None
                point.extensions = None

def process(gpx_data):
    gpx = gpxpy.parse(gpx_data)
    remove_metadata(gpx)
    
    xml = gpx.to_xml()
    xml = remove_xml_tags(xml)
    
    return xml

def main():
    gpx_data = sys.stdin.read()
    print(
       process(gpx_data) 
    )
    
if __name__ == "__main__":
    main()