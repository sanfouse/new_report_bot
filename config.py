from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    BOT_TOKEN: str
    EMAIL_PASSWORD: str
    EMAIL_LOGIN: str
    EMAIL_ADDRESS: str
    # REDIS_URL: str

    model_config = SettingsConfigDict(env_file=".env")


settings = Settings()
print(settings.EMAIL_ADDRESS)