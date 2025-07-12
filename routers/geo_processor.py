from fastapi import APIRouter
from fastapi.params import Depends

from dependencies.validate_coordinates import validate_coordinates
from schemas.coordinates import Coordinates
from utils.analyze_coordinates import get_coordinates_data

router = APIRouter(
    prefix="/geo",
    tags=["geo"],
    responses={
        404: {"description": "Not found"},
    },
)

@router.post("/process/")
async def process_coordinates(coordinates: Coordinates = Depends(validate_coordinates)):
    coordinates_data = get_coordinates_data(coordinates.points)

    return coordinates_data
