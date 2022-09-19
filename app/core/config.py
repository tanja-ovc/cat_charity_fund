from typing import Optional

from pydantic import BaseSettings, EmailStr


# отсюда он сначала смотрит в .env, есть там пусто, срабатывает
# дефолтное значение (после =)
class Settings(BaseSettings):
    app_title: str = 'QRKot'
    app_description: str = 'Проект для сбора пожертвований для котов и кошек.'
    database_url: str
    secret: str = 'SECRET'
    first_superuser_email: Optional[EmailStr] = None
    first_superuser_password: Optional[str] = None

    class Config:
        env_file = '.env'


settings = Settings()
