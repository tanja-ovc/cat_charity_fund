from sqlalchemy import Column, ForeignKey, Integer, Text

from app.core.db import CommonProjectDonation


class Donation(CommonProjectDonation):
    user_id = Column(Integer, ForeignKey('user.id'))
    comment = Column(Text)
