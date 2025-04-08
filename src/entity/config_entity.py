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
    

@dataclass(frozen=True)
class DataTransformationConfig:
    """
    Data Transformation Configuration
    """

    root_dir: Path
    input_file: Path
    
    
    
@dataclass(frozen=True)
class ModelTrainingConfig:
    """
    Data Model Training Configuration
    """

    root_dir: Path
    train_data_file: Path
    model_file: Path
    all_params: dict
    target_column: str
    
    