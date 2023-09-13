import abc


class ModuleInterface(abc.ABC):
    def __init__(
        self,
        name: str,
        version: str,
    ):
        self._name = name
        self._version = version

    @property
    def name(self) -> str:
        if self._name:
            return self._name
        raise NotImplementedError

    @property
    def version(self) -> str:
        if self._version:
            return self._version
        raise NotImplementedError
