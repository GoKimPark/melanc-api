import os
import logging.config
from melanc.config import ROOT_PATH, STAGE

LOGGING = {
    "version": 1,
    "disabled_existing_loggers": False,
    "formatters": {
        "standard": {
            "format": "%(asctime)s - %(module)s - %(levelname)s - %(message)s"
        },
    },
    "handlers": {
        "default": {
            "class": "logging.StreamHandler",
            "level": "DEBUG",
            "formatter": "standard",
        },
        "melanc": {
            "class": "logging.handlers.RotatingFileHandler",
            "level": "INFO",
            "formatter": "standard",
            "filename": os.path.join(ROOT_PATH, "logs", f"{STAGE}.log"),
        },
    },
    "loggers": {
        "": {
            "handlers": ["default"],
            "level": "DEBUG",
        },
        "melanc": {
            "handlers": ["melanc"],
            "level": "INFO",
            "propagate": STAGE == "development",
        },
    },
}

logging.config.dictConfig(LOGGING)

logger = logging.getLogger("melanc")
