from typing import Tuple, Optional
from ural.types import AnyUrlTarget

class SuffixTrie(object):
    def add(self, tld: str, private: bool = ...) -> None: ...
    def split(self, url: AnyUrlTarget) -> Optional[Tuple[str, str]]: ...
    def has_valid_domain_name(self, url: AnyUrlTarget) -> bool: ...
    def extract_suffix(self, url: AnyUrlTarget) -> Optional[str]: ...
    def extract_domain_name(self, url: AnyUrlTarget) -> Optional[str]: ...
