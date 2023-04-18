from pydantic import BaseSettings, BaseModel
import base64
from typing import List


__settings = None



class __Settings(BaseSettings):
    DATABASE_PORT: int
    POSTGRES_PASSWORD: str
    POSTGRES_USER: str
    POSTGRES_DB: str
    POSTGRES_HOST: str
    POSTGRES_HOSTNAME: str

    JWT_PUBLIC_KEY: str
    JWT_PRIVATE_KEY: str
    REFRESH_TOKEN_EXPIRES_IN: int
    ACCESS_TOKEN_EXPIRES_IN: int
    JWT_ALGORITHM: str

    CLIENT_ORIGIN: str

    class Config:
        env_file = './.env'


    class AuthSettings(BaseModel):
        __settings

        authjwt_algorithm: str = __settings.JWT_ALGORITHM
        authjwt_decode_algorithms: List[str] = [__settings.JWT_ALGORITHM]
        authjwt_token_location: set = {'cookies', 'headers'}
        authjwt_access_cookie_key: str = 'access_token'
        authjwt_refresh_cookie_key: str = 'refresh_token'
        authjwt_public_key: str = base64.b64decode(
            __settings.JWT_PUBLIC_KEY).decode('utf-8')
        authjwt_private_key: str = base64.b64decode(
            __settings.JWT_PRIVATE_KEY).decode('utf-8')


def get_config() -> __Settings:
    if not __settings:
        __settings = __Settings()
        setattr(__settings.AuthSettings, "__settings", __settings)
    return __settings











