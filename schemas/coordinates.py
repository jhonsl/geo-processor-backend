from pydantic import BaseModel
from typing import List

class Point(BaseModel):
    lat: float
    lng: float

class Bounds(BaseModel):
    north: float
    south: float
    east: float
    west: float

class Coordinates(BaseModel):
    points: List[Point]

class CoordinatesResponse(BaseModel):
    centroid: Point
    bounds: Bounds
