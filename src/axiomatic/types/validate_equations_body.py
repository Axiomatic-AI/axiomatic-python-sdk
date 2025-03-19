from .variable_requirement import VariableRequirement
from .equation_processing_response import EquationProcessingResponse
from pydantic import BaseModel

class ValidateEquationsBody(BaseModel):
    variables: list[VariableRequirement]
    paper_equations: EquationProcessingResponse
    include_internal_model: bool = False
