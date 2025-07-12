from schemas.coordinates import Point, Bounds, CoordinatesResponse
from typing import List

# Analyze coordinates and get information
def get_coordinates_data(points: List[Point]) -> CoordinatesResponse:
    bounds = analyze_bounds(points)
    centroid_point = calculate_centroid(points)

    return CoordinatesResponse(
        centroid=centroid_point,
        bounds=bounds
    )


# Calculate centroid points accord to document
def calculate_centroid(points: List[Point] ) -> Point:
    centroid_lat = sum(point.lat for point in points) / len(points)
    centroid_lng = sum(point.lng for point in points) / len(points)

    return Point(
        lat=round(centroid_lat, 4),
        lng=round(centroid_lng, 4),
    )

# Get bounds from points
def analyze_bounds(points: List[Point] ) -> Bounds:
    north_point = max(points, key=lambda point: point.lat)
    south_point = min(points, key=lambda point: point.lat)
    east_point = max(points, key=lambda point: point.lng)
    west_point = min(points, key=lambda point: point.lng)

    return Bounds(
        north=round(north_point.lat, 4),
        south=round(south_point.lat, 4),
        east=round(east_point.lng, 4),
        west=round(west_point.lng, 4),
    )
