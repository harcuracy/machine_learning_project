from pathlib import Path
from dataclasses import dataclass



@dataclass(frozen=True)
class DataIngestionConfig:
    """
    Data Ingestion Configuration
    """

    root_dir: Path
    source_URL: str 
    local_data_file: Path
    unzip_dir: Path


@dataclass(frozen=True)
class DataValidationConfig:
    """
    Data validation Configuration
    """

    root_dir: Path
    data_file: Path
    status: str
    all_schema: dict