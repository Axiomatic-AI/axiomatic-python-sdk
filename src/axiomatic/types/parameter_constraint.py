# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
import typing
import pydantic
from .z_3_expression_output import Z3ExpressionOutput
from ..core.pydantic_utilities import IS_PYDANTIC_V2


class ParameterConstraint(UniversalBaseModel):
    type: typing.Optional[typing.Literal["PARAMETER_CONSTRAINT"]] = None
    text: str = pydantic.Field()
    """
    The natural language content of the statement.
    """

    formalization: typing.Optional[Z3ExpressionOutput] = None
    formalized: bool

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
