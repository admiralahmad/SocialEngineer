import os
from dataclasses import dataclass
from pathlib import Path

from dotenv import load_dotenv


load_dotenv()


def env_bool(name: str, default: bool = False) -> bool:
    value = os.getenv(name)

    if value is None:
        return default

    return value.strip().lower() in {
        "1",
        "true",
        "yes",
        "on",
    }


@dataclass(frozen=True)
class Settings:
    environment: str
    log_level: str
    data_dir: Path

    smtp_server: str | None
    smtp_port: int
    smtp_username: str | None
    smtp_password: str | None
    smtp_use_tls: bool

    require_confirmation: bool


def load_settings() -> Settings:
    return Settings(
        environment=os.getenv("SE_ENV", "development"),
        log_level=os.getenv("SE_LOG_LEVEL", "INFO"),
        data_dir=Path(os.getenv("SE_DATA_DIR", "data")),

        smtp_server=os.getenv("SMTP_SERVER"),
        smtp_port=int(os.getenv("SMTP_PORT", "587")),
        smtp_username=os.getenv("SMTP_USERNAME"),
        smtp_password=os.getenv("SMTP_PASSWORD"),
        smtp_use_tls=env_bool("SMTP_USE_TLS", True),

        require_confirmation=env_bool(
            "SE_REQUIRE_CONFIRMATION",
            True,
        ),
    )