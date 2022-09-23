from sqlalchemy import Boolean, Column, DateTime, Integer

from app.core.db import Base


class CommonProjectDonation(Base):
    __abstract__ = True
    full_amount = Column(Integer) # больше 0
    invested_amount = Column(Integer, default=0) # значение по умолчанию — 0
    fully_invested = Column(Boolean, default=False) #  значение по умолчанию — False
    create_date = Column(DateTime) # должно добавляться автоматически в момент создания проекта/поступления пожертвования
    close_date = Column(DateTime) # проставляется автоматически в момент набора нужной суммы/когда вся сумма пожертвования была распределена по проектам