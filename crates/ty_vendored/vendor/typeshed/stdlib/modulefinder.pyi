"""Find modules used by a script, using introspection."""

import sys
from collections.abc import Container, Iterable, Iterator, Sequence
from types import CodeType
from typing import IO, Any, Final

if sys.version_info < (3, 11):
    LOAD_CONST: Final[int]  # undocumented
    IMPORT_NAME: Final[int]  # undocumented
    STORE_NAME: Final[int]  # undocumented
    STORE_GLOBAL: Final[int]  # undocumented
    STORE_OPS: Final[tuple[int, int]]  # undocumented
    EXTENDED_ARG: Final[int]  # undocumented

packagePathMap: dict[str, list[str]]  # undocumented

def AddPackagePath(packagename: str, path: str) -> None: ...

replacePackageMap: dict[str, str]  # undocumented

def ReplacePackage(oldname: str, newname: str) -> None: ...

class Module:  # undocumented
    def __init__(self, name: str, file: str | None = None, path: str | None = None) -> None: ...

class ModuleFinder:
    modules: dict[str, Module]
    path: list[str]  # undocumented
    badmodules: dict[str, dict[str, int]]  # undocumented
    debug: int  # undocumented
    indent: int  # undocumented
    excludes: Container[str]  # undocumented
    replace_paths: Sequence[tuple[str, str]]  # undocumented

    def __init__(
        self,
        path: list[str] | None = None,
        debug: int = 0,
        excludes: Container[str] | None = None,
        replace_paths: Sequence[tuple[str, str]] | None = None,
    ) -> None: ...
    def msg(self, level: int, str: str, *args: Any) -> None: ...  # undocumented
    def msgin(self, *args: Any) -> None: ...  # undocumented
    def msgout(self, *args: Any) -> None: ...  # undocumented
    def run_script(self, pathname: str) -> None: ...
    def load_file(self, pathname: str) -> None: ...  # undocumented
    def import_hook(
        self, name: str, caller: Module | None = None, fromlist: list[str] | None = None, level: int = -1
    ) -> Module | None: ...  # undocumented
    def determine_parent(self, caller: Module | None, level: int = -1) -> Module | None: ...  # undocumented
    def find_head_package(self, parent: Module, name: str) -> tuple[Module, str]: ...  # undocumented
    def load_tail(self, q: Module, tail: str) -> Module: ...  # undocumented
    def ensure_fromlist(self, m: Module, fromlist: Iterable[str], recursive: int = 0) -> None: ...  # undocumented
    def find_all_submodules(self, m: Module) -> Iterable[str]: ...  # undocumented
    def import_module(self, partname: str, fqname: str, parent: Module) -> Module | None: ...  # undocumented
    def load_module(self, fqname: str, fp: IO[str], pathname: str, file_info: tuple[str, str, str]) -> Module: ...  # undocumented
    def scan_opcodes(self, co: CodeType) -> Iterator[tuple[str, tuple[Any, ...]]]: ...  # undocumented
    def scan_code(self, co: CodeType, m: Module) -> None: ...  # undocumented
    def load_package(self, fqname: str, pathname: str) -> Module: ...  # undocumented
    def add_module(self, fqname: str) -> Module: ...  # undocumented
    def find_module(
        self, name: str, path: str | None, parent: Module | None = None
    ) -> tuple[IO[Any] | None, str | None, tuple[str, str, int]]: ...  # undocumented
    def report(self) -> None:
        """Print a report to stdout, listing the found modules with their
        paths, as well as modules that are missing, or seem to be missing.
        """

    def any_missing(self) -> list[str]:  # undocumented
        """Return a list of modules that appear to be missing. Use
        any_missing_maybe() if you want to know which modules are
        certain to be missing, and which *may* be missing.
        """

    def any_missing_maybe(self) -> tuple[list[str], list[str]]:  # undocumented
        """Return two lists, one with modules that are certainly missing
        and one with modules that *may* be missing. The latter names could
        either be submodules *or* just global names in the package.

        The reason it can't always be determined is that it's impossible to
        tell which names are imported when "from module import *" is done
        with an extension module, short of actually importing it.
        """

    def replace_paths_in_code(self, co: CodeType) -> CodeType: ...  # undocumented

def test() -> ModuleFinder | None: ...  # undocumented
