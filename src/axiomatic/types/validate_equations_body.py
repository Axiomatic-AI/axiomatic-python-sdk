from .variable_requirement import VariableRequirement
from .equation_processing_response import EquationProcessingResponse
from pydantic import BaseModel
from typing import List

class ValidateEquationsBody(BaseModel):
    variables: List[VariableRequirement]
    paper_equations: EquationProcessingResponse
    include_internal_model: bool = False
