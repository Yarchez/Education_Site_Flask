from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    DB_HOST: str
    DB_PORT: int
    DB_USER: str
    DB_PASS: str
    DB_NAME: str

    @property
    def DATABASE_URL(self):
        return f"postgresql+psycopg2://{self.DB_USER}:{self.DB_PASS}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"

    # model_config = SettingsConfigDict(env_file=".env")


settings = Settings(
    DB_HOST="localhost",
    DB_PORT=YOUR_DB_PORT,
    DB_USER="YOUR_DB_USER",
    DB_PASS="YOUR_DB_PASS",
    DB_NAME="YOUR_DB_NAME",
)

print(settings.DATABASE_URL)
