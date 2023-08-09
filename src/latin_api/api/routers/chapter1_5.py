from fastapi import APIRouter

router = APIRouter(prefix="/1")

@router.post("/1")
async def one():
    return "First Endpoint!"
