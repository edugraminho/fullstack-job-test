from pathlib import Path, PurePath
import os
from datetime import datetime
from enum import Enum

# ====================== DIRETÓRIOS LOCAIS e DATAS ======================
FULL_DATE_FORMAT = "%d/%m/%Y %H:%M:%S"
ROOT = Path(os.path.dirname(os.path.abspath(__file__))).parent
DATA_DIRECTORY = os.path.join(ROOT, "data")
ASSETS_DIRECTORY = os.path.join(ROOT, "app/services/assets")
DATE_NOW = datetime.now().strftime(FULL_DATE_FORMAT)


class Color(Enum):
    SECONDARY = "#000"
    PRIMARY = "#000"
    # BACK = "#FFF"
    PIXELS = "#000"


# class Color(Enum):
#     SECONDARY = "#ff9000"
#     PRIMARY = "#1C70CE"
#     BACK = "#FFF"
#     PIXELS = "#000"