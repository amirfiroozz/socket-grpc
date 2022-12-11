from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Error(_message.Message):
    __slots__ = ["isError", "message"]
    ISERROR_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    isError: bool
    message: str
    def __init__(self, isError: bool = ..., message: _Optional[str] = ...) -> None: ...

class RequestSorting(_message.Message):
    __slots__ = ["array", "isDone", "sleepTime", "type"]
    ARRAY_FIELD_NUMBER: _ClassVar[int]
    ISDONE_FIELD_NUMBER: _ClassVar[int]
    SLEEPTIME_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    array: _containers.RepeatedScalarFieldContainer[int]
    isDone: bool
    sleepTime: float
    type: str
    def __init__(self, type: _Optional[str] = ..., array: _Optional[_Iterable[int]] = ..., isDone: bool = ..., sleepTime: _Optional[float] = ...) -> None: ...

class ResponseSorting(_message.Message):
    __slots__ = ["array", "error", "isDone", "left", "right"]
    ARRAY_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    ISDONE_FIELD_NUMBER: _ClassVar[int]
    LEFT_FIELD_NUMBER: _ClassVar[int]
    RIGHT_FIELD_NUMBER: _ClassVar[int]
    array: _containers.RepeatedScalarFieldContainer[int]
    error: Error
    isDone: bool
    left: int
    right: int
    def __init__(self, array: _Optional[_Iterable[int]] = ..., isDone: bool = ..., left: _Optional[int] = ..., right: _Optional[int] = ..., error: _Optional[_Union[Error, _Mapping]] = ...) -> None: ...
