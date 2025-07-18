"""

Compatibility shim for .resources.simple as found on Python 3.10.

Consumers that can rely on Python 3.11 should use the other
module directly.
"""

import sys

if sys.version_info >= (3, 11):
    from .resources.simple import (
        ResourceContainer as ResourceContainer,
        ResourceHandle as ResourceHandle,
        SimpleReader as SimpleReader,
        TraversableReader as TraversableReader,
    )

    __all__ = ["SimpleReader", "ResourceHandle", "ResourceContainer", "TraversableReader"]
