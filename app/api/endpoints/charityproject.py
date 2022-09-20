
from datetime import datetime

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.db import get_async_session
from app.core.user import current_superuser
from app.crud import charityproject_crud
from app.schemas import CharityProjectCreate, CharityProjectDB

router = APIRouter()


async def insert_current_time() -> datetime:
        return datetime.now()


@router.post(
    '/',
    response_model=CharityProjectDB,
    response_model_exclude_none=True,
    dependencies=[Depends(current_superuser)],
)
async def create_new_charityproject(
        charityproject: CharityProjectCreate,
        session: AsyncSession = Depends(get_async_session),
):
    """Только для суперюзеров."""
    # await check_name_duplicate(meeting_room.name, session) # ?
    new_charityproject = await charityproject_crud.create(charityproject, session)
    return new_charityproject
