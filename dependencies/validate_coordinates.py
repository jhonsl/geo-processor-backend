from schemas.coordinates import Coordinates
from fastapi import Request, HTTPException

async def validate_coordinates(request: Request) -> Coordinates:
    try:
        body = await request.json()
        coordinates = Coordinates(**body)

        if len(coordinates.points) == 0:
            raise HTTPException(
                status_code=400,
                detail={
                    "error": "Bad Request",
                    "details": "Points are missing",
                }
            )
        return coordinates
    except Exception as e:
        raise HTTPException(
            status_code=400,
            detail={
                "error": "Bad Request",
                "details": "Bad body structure",
            }
        )