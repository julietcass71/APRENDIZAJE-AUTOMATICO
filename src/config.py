from dataclasses import dataclass
from pathlib import Path
import os

@dataclass
class Config:
    DATA_DIR: Path = Path(os.getenv("DATA_DIR", "./data"))
    RANDOM_STATE: int = int(os.getenv("RANDOM_STATE", "42"))

cfg = Config()
