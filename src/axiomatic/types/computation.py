# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
import pydantic
import typing
from .computation_arguments_value import ComputationArgumentsValue
from ..core.pydantic_utilities import IS_PYDANTIC_V2


class Computation(UniversalBaseModel):
    """
    A class describing a computation.
    """

    name: str = pydantic.Field()
    """
    The name of the computation.
    """

    arguments: typing.Dict[str, ComputationArgumentsValue] = pydantic.Field()
    """
    The arguments of the computation.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
