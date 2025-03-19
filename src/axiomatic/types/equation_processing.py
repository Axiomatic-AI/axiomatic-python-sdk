from pydantic import BaseModel, Field
from typing import List, Dict, Optional

class DictItem(BaseModel):
    key: str
    value: str

class ResponseEquation(BaseModel):
    """
    Pydantic model representing a scientific or mathematical equation.
    """

    name: str = Field(
        ...,
        description="Human-readable name of the equation (e.g., 'Newton's Law')",
    )
    description: str = Field(..., description="Text describing the equation")
    original_format: str = Field(..., description="Original form of the equation (e.g., LaTeX)")
    wolfram_expressions: str = Field(
        ..., description="Equation in Wolfram Language (or other symbolic form)"
    )
    latex_symbols: list[DictItem] = Field(
        ..., description="Detailed metadata for each latex variable in original format"
    )
    wolfram_symbols: list[str] = Field(
        ..., description="List of symbols used in the wolfram expression"
    )
    narrative_assumptions: list[str] = Field(
        ..., description="Narrative text describing assumptions/approximations"
    )
    type: list[str] = Field(
        ...,
        description="List of equation classifications (e.g., ['scalar','tensor'])",
    )
    field_tags: list[str] = Field(
        ...,
        description="Classification tags (e.g., ['quantum mechanics','gravitation'])",
    )