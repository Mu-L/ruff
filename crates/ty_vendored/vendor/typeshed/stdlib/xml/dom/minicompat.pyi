"""Python version compatibility support for minidom.

This module contains internal implementation details and
should not be imported; use xml.dom.minidom instead.
"""

from collections.abc import Iterable
from typing import Any, Literal, TypeVar

__all__ = ["NodeList", "EmptyNodeList", "StringTypes", "defproperty"]

_T = TypeVar("_T")

StringTypes: tuple[type[str]]

class NodeList(list[_T]):
    @property
    def length(self) -> int:
        """The number of nodes in the NodeList."""

    def item(self, index: int) -> _T | None: ...

class EmptyNodeList(tuple[()]):
    @property
    def length(self) -> Literal[0]:
        """The number of nodes in the NodeList."""

    def item(self, index: int) -> None: ...
    def __add__(self, other: Iterable[_T]) -> NodeList[_T]: ...  # type: ignore[override]
    def __radd__(self, other: Iterable[_T]) -> NodeList[_T]: ...

def defproperty(klass: type[Any], name: str, doc: str) -> None: ...
