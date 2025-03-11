from pydantic import BaseModel
from typing import List


class DictItem(BaseModel):
    key: str
    value: str


class EquationExtraction(BaseModel):
    id: str
    name: str
    description: str
    original_format: str
    latex_symbols: List[DictItem]
    narrative_assumptions: List[str]


class EquationExtractionResponse(BaseModel):
    equations: List[EquationExtraction]


class VariableRequirement(BaseModel):
    symbol: str
    name: str
    value: float
    units: str
    tolerance: float
