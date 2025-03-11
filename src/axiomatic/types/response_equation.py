# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
import pydantic
import typing
from ..core.pydantic_utilities import IS_PYDANTIC_V2


class ResponseEquation(UniversalBaseModel):
    """
    Pydantic model representing a scientific or mathematical equation.
    """

    name: str = pydantic.Field()
    """
    Human-readable name of the equation (e.g., 'Newton's Law')
    """

    description: str = pydantic.Field()
    """
    Text describing the equation
    """

    original_format: str = pydantic.Field()
    """
    Original form of the equation (e.g., LaTeX)
    """

    wolfram_expressions: str = pydantic.Field()
    """
    Equation in Wolfram Language (or other symbolic form)
    """

    latex_symbols: typing.List[typing.Dict[str, typing.Optional[typing.Any]]] = pydantic.Field()
    """
    Detailed metadata for each latex variable in original format
    """

    wolfram_symbols: typing.List[str] = pydantic.Field()
    """
    List of symbols used in the wolfram expression
    """

    narrative_assumptions: typing.List[str] = pydantic.Field()
    """
    Narrative text describing assumptions/approximations
    """

    type: typing.List[str] = pydantic.Field()
    """
    List of equation classifications (e.g., ['scalar','tensor'])
    """

    field_tags: typing.List[str] = pydantic.Field()
    """
    Classification tags (e.g., ['quantum mechanics','gravitation'])
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
