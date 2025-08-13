from dataclasses import dataclass, field
from typing import Dict

@dataclass
class DatabaseConfig:
    host: str = "13.58.82.14"
    port: int = 3309
    user: str = "pruebas"
    password: str = "VGbt3Day5R"
    database: str = "habi_db"

@dataclass
class AppConfig:
    APP_NAME: str = "Property Service"
    APP_VERSION: str = "1.0.0"
    db: DatabaseConfig = field(default_factory=DatabaseConfig)
    PORT: int = 8000
    
    VALID_PROPERTY_STATES: Dict[int, str] = field(default_factory=lambda: {
        1: "pre_venta",
        2: "en_venta",
        3: "vendido"
    })

# Create global config instance
config = AppConfig()