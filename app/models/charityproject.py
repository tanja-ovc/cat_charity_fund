from sqlalchemy import Column, String, Text

from app.core.db import CommonProjectDonation


class CharityProject(CommonProjectDonation):
    name = Column(String(100), unique=True, nullable=False)
    description = Column(Text, nullable=False) # not shorter that 1 symbol
