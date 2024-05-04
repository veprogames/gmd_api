from .level_object import LevelObject
from .color import ColorChannel
from .level_string import InnerLevelString
from .keys.level import *
from typing import Self
import base64

class Level:
    def __init__(self, name: str = "", description: str = "") -> None:
        self.inner_string: InnerLevelString = InnerLevelString()
        self.properties: dict[str, any] = {}

        self.set_name(name)
        self.set_description(description)
        self.set(K_LEVEL_VERSION, 1)
        self.set(K_LEVEL_TYPE, LEVEL_TYPE_LOCAL)
        self.set(K_BINARY_VERSION, 40)
        self.set(K_KCEK, 4)
    
    def set(self, key: str, value: any) -> Self:
        self.properties[key] = value
        return self
    
    def set_time_spent(self, seconds: int) -> Self:
        return self.set(K_SECS_SPENT_EDITING, seconds)
    
    def set_official_song_id(self, id: int) -> Self:
        return self.set(K_OFFICIAL_SONG_ID, id)
    
    def set_custom_song_id(self, id: int) -> Self:
        return self.set(K_CUSTOM_SONG_ID, id)
    
    def set_name(self, name: str) -> Self:
        return self.set(K_LEVEL_NAME, name)

    def set_description(self, description: str) -> Self:
        encoded = base64.urlsafe_b64encode(bytes(description, encoding="utf-8"))
        decoded_back = encoded.decode("utf-8")
        return self.set(K_DESCRIPTION_BASE64, decoded_back)

    def add_object(self, obj: LevelObject) -> Self:
        self.inner_string.objects.append(obj)
        return self
    
    def add_color_channel(self, channel: ColorChannel) -> Self:
        self.inner_string.color_channels.append(channel)
        return self
    
    def inner(self) -> InnerLevelString:
        return self.inner_string

    def to_string(self) -> str:
        props = "".join(
            f"<k>{k}</k><{get_type_tag(v)}>{v}</{get_type_tag(v)}>" for k, v in self.properties.items()
        )

        string: str = f"""<?xml version="1.0"?>
<plist version="1.0" gjver="2.0">
    <dict>
        <k>k4</k><s>{self.inner_string.to_string()}</s>
        {props}
    </dict>
</plist>"""
        return string \
            .replace("\n", "") \
            .replace("\t", "")
    
    def save(self, to_file: str) -> None:
        with open(to_file, "w") as f:
            f.write(self.to_string())

def get_type_tag(value: any) -> str:
    if isinstance(value, int):
        return "i"
    return "s"