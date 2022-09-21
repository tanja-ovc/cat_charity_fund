from datetime import datetime
from pydantic import BaseModel, Field, PositiveInt, validator
from typing import Optional


class CharityProjectBase(BaseModel):
    name: Optional[str] = Field(None, min_length=1, max_length=100)
    description: Optional[str] = Field(None, min_length=1)
    full_amount: Optional[PositiveInt]


class CharityProjectCreate(CharityProjectBase):
    name: str = Field(..., min_length=1, max_length=100)
    description: str = Field(..., min_length=1)
    full_amount: PositiveInt
    create_date: datetime = Field(default_factory=datetime.utcnow) # должно добавляться автоматически в момент создания проекта/поступления пожертвования

    class Config:
        schema_extra = {
           'example': {
               'name': 'Сбор на стерилизацию бездомных кошек',
               'description': 'В рамках кампании по стерилизации кошек Кошачьего района.',
               'full_amount': 34000
           }
        } 

class CharityProjectDB(CharityProjectCreate):
    id: int
    invested_amount: int # значение по умолчанию — 0 (in the model)
    fully_invested: bool #  значение по умолчанию — False (in the model)
    create_date: datetime
    close_date: Optional[datetime] # проставляется автоматически в момент набора нужной суммы/когда вся сумма пожертвования была распределена по проектам

    class Config:
        orm_mode = True


class CharityProjectUpdate(CharityProjectBase):
    
    @validator('name')
    def name_cannot_be_null(cls, value):
        if value is None:
            raise ValueError('Имя проекта не может быть пустым.')
        return value
