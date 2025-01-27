# This file was auto-generated by Fern from our API Definition.

from ..core.client_wrapper import SyncClientWrapper
from .lens.client import LensClient
from ..core.client_wrapper import AsyncClientWrapper
from .lens.client import AsyncLensClient


class FsoClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper
        self.lens = LensClient(client_wrapper=self._client_wrapper)


class AsyncFsoClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper
        self.lens = AsyncLensClient(client_wrapper=self._client_wrapper)
