# gmd_api

A simple api to create .gmd files for GDShare.

This removes the necessity to interact with the save file directly and saving levels somewhere in a filesystem for easy sharing as a bonus.

This is a rather low level interface. There are helper methods, but no safeguards against missing or malformed data. Your Game can crash when opening a level with malformed data.

# Installation

- venv, conda, micromamba or any other environment solution recommended
- `pip install https://github.com/veprogames/gmd_api`
- or add it to requirements.txt
- remember the above notation supports specifying a specific commit hash

# Example

This adds a 30x30 grid of differently colored blocks, sets the song to Explorers (won't play) and makes you having spent over 30 hours in the editor.

```py
from gmd_api.level import Level
from gmd_api.level_object import LevelObject
from gmd_api.color import ColorChannel

lvl = Level(name="~* Bypassing the Title Limits of the Client *~", description="")

for x in range(30):
    for y in range(30):
        obj = LevelObject(211) \
            .move_to(15 + 30 * x, 15 + 30 * y) \
            .set_detail_hsv(-180 + (60 * x + 60 * y) % 360, 1.0, 1.0)
        lvl.add_object(obj)

channel = ColorChannel(1).set_rgb(255, 0, 0)
lvl.add_color_channel(channel)

lvl.inner() \
    .set_platformer() \
    .set_background_id(12) \
    .set_middleground_id(2)

lvl.set_time_spent(123456) \
    .set_official_song_id(22)

lvl.save("next.gmd")
```