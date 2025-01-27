# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
import typing
import pydantic
from .structure_function_call import StructureFunctionCall
from ..core.pydantic_utilities import IS_PYDANTIC_V2


class StructureConstraint(UniversalBaseModel):
    type: typing.Optional[typing.Literal["STRUCTURE_CONSTRAINT"]] = None
    text: str = pydantic.Field()
    """
    The natural language content of the statement.
    """

    formalization: typing.Optional[StructureFunctionCall] = None
    formalized: bool

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
