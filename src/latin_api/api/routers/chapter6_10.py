from fastapi import APIRouter

router = APIRouter(prefix="/2")

@router.post("/2")
async def one():
    return "Second Endpoint!"
