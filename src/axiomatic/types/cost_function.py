# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
import typing
from .statement_type import StatementType
import pydantic
from .pic_z3expression import PicZ3Expression
from .statement_validation import StatementValidation
from ..core.pydantic_utilities import IS_PYDANTIC_V2


class CostFunction(UniversalBaseModel):
    type: typing.Optional[StatementType] = None
    text: str = pydantic.Field()
    """
    The natural language content of the statement.
    """

    formalization: typing.Optional[PicZ3Expression] = None
    validation: typing.Optional[StatementValidation] = pydantic.Field(default=None)
    """
    The validation result of the statement.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
