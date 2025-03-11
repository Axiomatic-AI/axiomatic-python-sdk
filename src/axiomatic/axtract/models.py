from pydantic import BaseModel

class DictItem(BaseModel):
    key: str
    value: str


class EquationExtraction(BaseModel):
    id: str
    name: str
    description: str
    original_format: str
    latex_symbols: list[DictItem]
    narrative_assumptions: list[str]


class EquationExtractionResponse(BaseModel):
    equations: list[EquationExtraction]


class VariableRequirement(BaseModel):
    symbol: str
    name: str
    value: float
    units: str
    tolerance: float