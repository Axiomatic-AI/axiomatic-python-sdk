# This file was auto-generated by Fern from our API Definition.

from ..core.client_wrapper import SyncClientWrapper
from .document.client import DocumentClient
from .circuit.client import CircuitClient
from .component.client import ComponentClient
from ..core.client_wrapper import AsyncClientWrapper
from .document.client import AsyncDocumentClient
from .circuit.client import AsyncCircuitClient
from .component.client import AsyncComponentClient


class PicClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper
        self.document = DocumentClient(client_wrapper=self._client_wrapper)
        self.circuit = CircuitClient(client_wrapper=self._client_wrapper)
        self.component = ComponentClient(client_wrapper=self._client_wrapper)


class AsyncPicClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper
        self.document = AsyncDocumentClient(client_wrapper=self._client_wrapper)
        self.circuit = AsyncCircuitClient(client_wrapper=self._client_wrapper)
        self.component = AsyncComponentClient(client_wrapper=self._client_wrapper)
