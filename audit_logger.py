import logging

from pathlib import Path



LOG_PATH = Path(__file__).parent / "audit.log"



logger = logging.getLogger("SecureDataAudit")

logger.setLevel(logging.INFO)

logger.propagate = False



if not logger.handlers:

    handler = logging.FileHandler(LOG_PATH, encoding="utf-8")

    handler.setFormatter(

        logging.Formatter(

            "%(asctime)s | %(levelname)s | %(message)s"

        )

    )

    logger.addHandler(handler)





def log_access(role, resource, allowed):

    status = "ALLOWED" if allowed else "DENIED"



    logger.info(

        "Role=%s | Resource=%s | Status=%s",

        role,

        resource,

        status

    )