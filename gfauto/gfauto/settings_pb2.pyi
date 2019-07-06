# @generated by generate_proto_mypy_stubs.py.  Do not edit!
import sys
from gfauto.common_pb2 import (
    Binary as gfauto___common_pb2___Binary,
)

from gfauto.device_pb2 import (
    DeviceList as gfauto___device_pb2___DeviceList,
)

from google.protobuf.internal.containers import (
    RepeatedCompositeFieldContainer as google___protobuf___internal___containers___RepeatedCompositeFieldContainer,
)

from google.protobuf.message import (
    Message as google___protobuf___message___Message,
)

from typing import (
    Iterable as typing___Iterable,
    Optional as typing___Optional,
)

from typing_extensions import (
    Literal as typing_extensions___Literal,
)


class Settings(google___protobuf___message___Message):

    @property
    def device_list(self) -> gfauto___device_pb2___DeviceList: ...

    @property
    def custom_binaries(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[gfauto___common_pb2___Binary]: ...

    def __init__(self,
        device_list : typing___Optional[gfauto___device_pb2___DeviceList] = None,
        custom_binaries : typing___Optional[typing___Iterable[gfauto___common_pb2___Binary]] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> Settings: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def HasField(self, field_name: typing_extensions___Literal[u"device_list"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"custom_binaries",u"device_list"]) -> None: ...
    else:
        def HasField(self, field_name: typing_extensions___Literal[u"device_list",b"device_list"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[b"custom_binaries",b"device_list"]) -> None: ...
