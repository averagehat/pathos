# Stubs for path (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from . import matchers
from typing import Any, Optional

class TreeWalkWarning(Warning): ...

class ClassProperty(property):
    def __get__(self, cls: Any, owner: Any): ...

class multimethod:
    func: Any = ...
    def __init__(self, func: Any) -> None: ...
    def __get__(self, instance: Any, owner: Any): ...

class Path(str):
    module: Any = ...
    def __init__(self, other: str = ...) -> None: ...
    @classmethod
    def using_module(cls, module: Any): ...
    def __add__(self, more: Any): ...
    def __radd__(self, other: Any): ...
    def __div__(self, rel: Any): ...
    __truediv__: Any = ...
    def __rdiv__(self, rel: Any): ...
    __rtruediv__: Any = ...
    def __enter__(self): ...
    def __exit__(self, *_: Any) -> None: ...
    def __fspath__(self): ...
    @classmethod
    def getcwd(cls): ...
    def abspath(self): ...
    def normcase(self): ...
    def normpath(self): ...
    def realpath(self): ...
    def expanduser(self): ...
    def expandvars(self): ...
    def dirname(self): ...
    def basename(self): ...
    def expand(self): ...
    @property
    def stem(self): ...
    @property
    def namebase(self): ...
    @property
    def ext(self): ...
    def with_suffix(self, suffix: Any): ...
    @property
    def drive(self): ...
    parent: Any = ...
    name: Any = ...
    def splitpath(self): ...
    def splitdrive(self): ...
    def splitext(self): ...
    def stripext(self): ...
    def splitunc(self): ...
    @property
    def uncshare(self): ...
    def joinpath(cls, first: Any, *others: Any): ...
    def splitall(self): ...
    def relpath(self, start: str = ...): ...
    def relpathto(self, dest: Any): ...
    def listdir(self, match: Optional[Any] = ...): ...
    def dirs(self, *args: Any, **kwargs: Any): ...
    def files(self, *args: Any, **kwargs: Any): ...
    def walk(self, match: Optional[Any] = ..., errors: str = ...) -> None: ...
    def walkdirs(self, *args: Any, **kwargs: Any): ...
    def walkfiles(self, *args: Any, **kwargs: Any): ...
    def fnmatch(self, pattern: Any, normcase: Optional[Any] = ...): ...
    def glob(self, pattern: Any): ...
    def iglob(self, pattern: Any): ...
    def open(self, *args: Any, **kwargs: Any): ...
    def bytes(self): ...
    def chunks(self, size: Any, *args: Any, **kwargs: Any): ...
    def write_bytes(self, bytes: Any, append: bool = ...) -> None: ...
    def text(self, encoding: Optional[Any] = ..., errors: str = ...): ...
    def write_text(self, text: Any, encoding: Optional[Any] = ..., errors: str = ..., linesep: Any = ..., append: bool = ...) -> None: ...
    def lines(self, encoding: Optional[Any] = ..., errors: str = ..., retain: bool = ...): ...
    def write_lines(self, lines: Any, encoding: Optional[Any] = ..., errors: str = ..., linesep: Any = ..., append: bool = ...) -> None: ...
    def read_md5(self): ...
    def read_hash(self, hash_name: Any): ...
    def read_hexhash(self, hash_name: Any): ...
    def isabs(self): ...
    def exists(self): ...
    def isdir(self): ...
    def isfile(self): ...
    def islink(self): ...
    def ismount(self): ...
    def samefile(self, other: Any): ...
    def getatime(self): ...
    atime: Any = ...
    def getmtime(self): ...
    mtime: Any = ...
    def getctime(self): ...
    ctime: Any = ...
    def getsize(self): ...
    size: Any = ...
    def access(self, mode: Any): ...
    def stat(self): ...
    def lstat(self): ...
    get_owner: Any = ...
    owner: Any = ...
    def statvfs(self): ...
    def pathconf(self, name: Any): ...
    def utime(self, times: Any): ...
    def chmod(self, mode: Any): ...
    def chown(self, uid: int = ..., gid: int = ...): ...
    def rename(self, new: Any): ...
    def renames(self, new: Any): ...
    def mkdir(self, mode: int = ...): ...
    def mkdir_p(self, mode: int = ...): ...
    def makedirs(self, mode: int = ...): ...
    def makedirs_p(self, mode: int = ...): ...
    def rmdir(self): ...
    def rmdir_p(self): ...
    def removedirs(self): ...
    def removedirs_p(self): ...
    def touch(self): ...
    def remove(self): ...
    def remove_p(self): ...
    def unlink(self): ...
    def unlink_p(self): ...
    def link(self, newpath: Any): ...
    def symlink(self, newlink: Optional[Any] = ...): ...
    def readlink(self): ...
    def readlinkabs(self): ...
    copyfile: Any = ...
    copymode: Any = ...
    copystat: Any = ...
    copy: Any = ...
    copy2: Any = ...
    copytree: Any = ...
    move: Any = ...
    rmtree: Any = ...
    def rmtree_p(self): ...
    def chdir(self) -> None: ...
    cd: Any = ...
    def merge_tree(self, dst: Any, symlinks: bool = ..., *, update: bool = ..., copy_function: Any = ..., ignore: Any = ...): ...
    def chroot(self) -> None: ...
    def startfile(self): ...
    def in_place(self, mode: str = ..., buffering: int = ..., encoding: Optional[Any] = ..., errors: Optional[Any] = ..., newline: Optional[Any] = ..., backup_extension: Optional[Any] = ...) -> None: ...
    @classmethod
    def special(cls): ...

class DirectoryNotEmpty(OSError):
    @staticmethod
    def translate() -> None: ...

class SpecialResolver:
    class ResolverScope:
        paths: Any = ...
        scope: Any = ...
        def __init__(self, paths: Any, scope: Any) -> None: ...
        def __getattr__(self, class_: Any): ...
    def __init__(self, path_class: Any, *args: Any, **kwargs: Any) -> None: ...
    def __getattr__(self, scope: Any): ...
    def get_dir(self, scope: Any, class_: Any): ...

class Multi:
    @classmethod
    def for_class(cls, path_cls: Any): ...
    @classmethod
    def detect(cls, input: Any): ...
    def __iter__(self): ...

class TempDir(Path):
    def __new__(cls, *args: Any, **kwargs: Any): ...
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    def __enter__(self): ...
    def __exit__(self, exc_type: Any, exc_value: Any, traceback: Any) -> None: ...
tempdir = TempDir

class CaseInsensitivePattern(matchers.CaseInsensitive):
    def __init__(self, value: Any) -> None: ...

class FastPath(Path):
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...