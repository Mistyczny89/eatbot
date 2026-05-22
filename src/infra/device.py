from __future__ import annotations

import scrcpy


class Device:

    def __init__(self):

        self.client = scrcpy.Client(
            max_fps=30,
            bitrate=16_000_000,
            block_frame=False
        )

    def start(self):

        self.client.start(threaded=True)