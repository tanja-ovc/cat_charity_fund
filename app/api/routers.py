from fastapi import APIRouter

from app.api.endpoints import user_router, charityproject_router

main_router = APIRouter()
main_router.include_router(
    charityproject_router, prefix='/charity_project', tags=['Charity Projects']
)
# main_router.include_router(
#     ..., prefix='/...', tags=['...']
# )
main_router.include_router(user_router)
