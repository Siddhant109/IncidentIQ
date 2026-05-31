import logging
import structlog

from app.config import settings


def configure_logging():

    logging.basicConfig(
        level=settings.LOG_LEVEL,
        format="%(message)s",
    )

    structlog.configure(
        wrapper_class=structlog.make_filtering_bound_logger(
            logging.INFO
        ),
    )


logger = structlog.get_logger()