from datetime import datetime
from pydantic import BaseModel, Field, PositiveInt
from typing import Optional


class CharityProjectBase(BaseModel):
    name: str = Field(None, min_length=1, max_length=100)
    description: str = Field(None, min_length=1)
    full_amount: PositiveInt


class CharityProjectCreate(CharityProjectBase):
    create_date: datetime = Field(default_factory=datetime.utcnow) # должно добавляться автоматически в момент создания проекта/поступления пожертвования


class CharityProjectDB(CharityProjectBase):
    id: int
    invested_amount: int # значение по умолчанию — 0 (in the model)
    fully_invested: bool #  значение по умолчанию — False (in the model)
    create_date: datetime
    close_date: Optional[datetime] # проставляется автоматически в момент набора нужной суммы/когда вся сумма пожертвования была распределена по проектам

    class Config:
        orm_mode = True
