from pydantic_settings import BaseSettings
from pydantic import ConfigDict


class Settings(BaseSettings):

    PROJECT_NAME: str

    KAFKA_BOOTSTRAP_SERVERS: str

    MONGO_URI: str
    MONGO_DB_NAME: str

    OLLAMA_BASE_URL: str

    LOG_LEVEL: str = "INFO"

    PROMETHEUS_ENABLED: bool = True

    model_config = ConfigDict(
        env_file=".env",
        extra="ignore"
    )


settings = Settings()