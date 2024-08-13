import logging
import os

from geopy.distance import geodesic

LOG_DIR = 'log'
os.makedirs(LOG_DIR, exist_ok=True)

logging.basicConfig(
    filename=f"{LOG_DIR}/anonymize.log", 
    filemode='a',
    encoding='utf-8', 
    level=logging.INFO,
    format='%(message)s',
)

def get_stats(gpx):
    count, distance = 0, 0.0
    for track in gpx.tracks:
        for segment in track.segments:
            count += len(segment.points)
            for i in range(1, len(segment.points)):
                point1 = segment.points[i - 1]
                point2 = segment.points[i]
                
                distance += geodesic(
                    (point1.latitude, point1.longitude), 
                    (point2.latitude, point2.longitude),
                ).kilometers

    return count, round(distance, 2) 

def log(gpx, step):
    logger = logging.getLogger(__name__)
    count, distance = get_stats(gpx)
    logger.info('%d points %f distance (%s)', count, distance, step)