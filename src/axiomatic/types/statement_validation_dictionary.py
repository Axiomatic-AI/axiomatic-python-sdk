# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
import typing
from .statement_validation import StatementValidation
from ..core.pydantic_utilities import IS_PYDANTIC_V2
import pydantic


class StatementValidationDictionary(UniversalBaseModel):
    """
    A dictionary of statement statuses by type.
    """

    cost_functions: typing.Optional[typing.List[StatementValidation]] = None
    parameter_constraints: typing.Optional[typing.List[StatementValidation]] = None
    unformalizable_statements: typing.Optional[typing.List[StatementValidation]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
