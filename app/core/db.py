from sqlalchemy import Boolean, Column, DateTime, Integer
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import declarative_base, declared_attr, sessionmaker

from app.core.config import settings


class PreBase:

    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()

    id = Column(Integer, primary_key=True)


Base = declarative_base(cls=PreBase)

class CommonProjectDonation(Base):
    __abstract__ = True
    full_amount = Column(Integer) # больше 0
    invested_amount = Column(Integer, default=0) # значение по умолчанию — 0
    fully_invested = Column(Boolean, default=False) #  значение по умолчанию — False
    create_date = Column(DateTime) # должно добавляться автоматически в момент создания проекта/поступления пожертвования
    close_date = Column(DateTime) # проставляется автоматически в момент набора нужной суммы/когда вся сумма пожертвования была распределена по проектам


engine = create_async_engine(settings.database_url)

AsyncSessionLocal = sessionmaker(engine, class_=AsyncSession)


# Асинхронный генератор сессий.
async def get_async_session():
    # Через асинхронный контекстный менеджер и sessionmaker
    # открывается сессия.
    async with AsyncSessionLocal() as async_session:
        # Генератор с сессией передается в вызывающую функцию.
        yield async_session
        # Когда HTTP-запрос отработает - выполнение кода вернётся сюда,
        # и при выходе из контекстного менеджера сессия будет закрыта.
