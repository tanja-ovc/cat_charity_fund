# from typing import Optional

# from sqlalchemy import select
# from sqlalchemy.ext.asyncio import AsyncSession

from app.crud.base import CRUDBase
from app.models import CharityProject


class CRUDCharityProject(CRUDBase):
    pass


charityproject_crud = CRUDCharityProject(CharityProject)
