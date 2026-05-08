from pydantic_settings import BaseSettings


class Settings(BaseSettings):

    DATABASE_URL: str

    REDIS_HOST: str
    REDIS_PORT: int

    KAFKA_BOOTSTRAP_SERVERS: str

    OPENAI_API_KEY: str

    class Config:
        env_file = ".env"


settings = Settings()