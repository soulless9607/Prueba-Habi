from dataclasses import dataclass, field
from datetime import datetime
from typing import Optional
from enum import Enum

class PropertyStatus(str, Enum):
    PRE_SALE = "pre_venta"
    FOR_SALE = "en_venta"
    SOLD = "vendido"

@dataclass
class Property:
    id: int
    address: str
    city: str
    price: float
    description: Optional[str]
    year: int
    status: PropertyStatus
    created_at: datetime = field(default_factory=datetime.now)

@dataclass
class PropertyResponse:
    id: int
    address: str
    city: str
    price: float
    description: Optional[str]
    year: int
    status: str