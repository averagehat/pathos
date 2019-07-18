# Stubs for yaml (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from .error import *
from .tokens import *
from .events import *
from .nodes import *
from .loader import *
from .dumper import *
from .cyaml import *
from typing import Any, Optional

__with_libyaml__: bool

def warnings(settings: Optional[Any] = ...): ...

class YAMLLoadWarning(RuntimeWarning): ...

def load_warning(method: Any) -> None: ...
def scan(stream: Any, Loader: Any = ...) -> None: ...
def parse(stream: Any, Loader: Any = ...) -> None: ...
def compose(stream: Any, Loader: Any = ...): ...
def compose_all(stream: Any, Loader: Any = ...) -> None: ...
def load(stream: Any, Loader: Optional[Any] = ...): ...
def load_all(stream: Any, Loader: Optional[Any] = ...) -> None: ...
def full_load(stream: Any): ...
def full_load_all(stream: Any): ...
def safe_load(stream: Any): ...
def safe_load_all(stream: Any): ...
def unsafe_load(stream: Any): ...
def unsafe_load_all(stream: Any): ...
def emit(events: Any, stream: Optional[Any] = ..., Dumper: Any = ..., canonical: Optional[Any] = ..., indent: Optional[Any] = ..., width: Optional[Any] = ..., allow_unicode: Optional[Any] = ..., line_break: Optional[Any] = ...): ...
def serialize_all(nodes: Any, stream: Optional[Any] = ..., Dumper: Any = ..., canonical: Optional[Any] = ..., indent: Optional[Any] = ..., width: Optional[Any] = ..., allow_unicode: Optional[Any] = ..., line_break: Optional[Any] = ..., encoding: Optional[Any] = ..., explicit_start: Optional[Any] = ..., explicit_end: Optional[Any] = ..., version: Optional[Any] = ..., tags: Optional[Any] = ...): ...
def serialize(node: Any, stream: Optional[Any] = ..., Dumper: Any = ..., **kwds: Any): ...
def dump_all(documents: Any, stream: Optional[Any] = ..., Dumper: Any = ..., default_style: Optional[Any] = ..., default_flow_style: bool = ..., canonical: Optional[Any] = ..., indent: Optional[Any] = ..., width: Optional[Any] = ..., allow_unicode: Optional[Any] = ..., line_break: Optional[Any] = ..., encoding: Optional[Any] = ..., explicit_start: Optional[Any] = ..., explicit_end: Optional[Any] = ..., version: Optional[Any] = ..., tags: Optional[Any] = ..., sort_keys: bool = ...): ...
def dump(data: Any, stream: Optional[Any] = ..., Dumper: Any = ..., **kwds: Any): ...
def safe_dump_all(documents: Any, stream: Optional[Any] = ..., **kwds: Any): ...
def safe_dump(data: Any, stream: Optional[Any] = ..., **kwds: Any): ...
def add_implicit_resolver(tag: Any, regexp: Any, first: Optional[Any] = ..., Loader: Any = ..., Dumper: Any = ...) -> None: ...
def add_path_resolver(tag: Any, path: Any, kind: Optional[Any] = ..., Loader: Any = ..., Dumper: Any = ...) -> None: ...
def add_constructor(tag: Any, constructor: Any, Loader: Any = ...) -> None: ...
def add_multi_constructor(tag_prefix: Any, multi_constructor: Any, Loader: Any = ...) -> None: ...
def add_representer(data_type: Any, representer: Any, Dumper: Any = ...) -> None: ...
def add_multi_representer(data_type: Any, multi_representer: Any, Dumper: Any = ...) -> None: ...

class YAMLObjectMetaclass(type):
    def __init__(cls, name: Any, bases: Any, kwds: Any) -> None: ...

class YAMLObject(metaclass=YAMLObjectMetaclass):
    yaml_loader: Any = ...
    yaml_dumper: Any = ...
    yaml_tag: Any = ...
    yaml_flow_style: Any = ...
    @classmethod
    def from_yaml(cls, loader: Any, node: Any): ...
    @classmethod
    def to_yaml(cls, dumper: Any, data: Any): ...
