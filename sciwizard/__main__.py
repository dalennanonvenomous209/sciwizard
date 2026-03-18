"""Entry point: python -m sciwizard"""

import sys
import logging

from sciwizard.app import main

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s — %(message)s",
    handlers=[
        logging.StreamHandler(sys.stdout),
    ],
)

if __name__ == "__main__":
    main()
