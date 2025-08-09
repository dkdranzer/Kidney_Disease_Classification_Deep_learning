from dataclasses import dataclass
from pathlib import Path

# dataclass is a decorator which does not create class but like to store the variables for access
@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir: Path
    source_URL: str
    local_data_file: Path
    unzip_dir: Path
