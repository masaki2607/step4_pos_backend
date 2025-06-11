from fastapi import APIRouter

example_router = APIRouter()

@example_router.get("/example")
async def example():
    return {"message": "This is an example endpoint."}