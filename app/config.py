from pydantic import BaseSettings
import base64


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
        env_file = "./.env"

# TODO: pass the link to this function in main.py as we do lambda
    def auth_settings(self):
        return {
            "authjwt_algorithm": self.JWT_ALGORITHM,
            "authjwt_decode_algorithms": [self.JWT_ALGORITHM],
            "authjwt_token_location": {'cookies', 'headers'},
            "authjwt_access_cookie_key": 'access_token',
            "authjwt_refresh_cookie_key": 'refresh_token',
            "authjwt_public_key": base64.b64decode(
                self.JWT_PUBLIC_KEY
            ).decode('utf-8'),
            "authjwt_private_key": base64.b64decode(
                self.JWT_PRIVATE_KEY
            ).decode('utf-8'),
        }


def get_config() -> __Settings:
    global __settings
    if not __settings:
        __settings = __Settings()
    return __settings











