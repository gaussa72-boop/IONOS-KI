__all__ = ["Mapping", "Sequence"]

try:
    from my_collections.abc import Mapping, Sequence
except ImportError:
    from my_collections import Mapping, Sequence
