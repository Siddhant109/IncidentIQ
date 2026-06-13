from fastapi import APIRouter

router = APIRouter()


@router.get("/debug")
async def debug():

    return {
        "message":
        "simulators running"
    }