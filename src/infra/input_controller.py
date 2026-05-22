from __future__ import annotations

import scrcpy
import time


class InputController:

    def __init__(self, client: scrcpy.Client):

        self.client = client

    def tap(self, x: int, y: int):

        self.client.control.touch(
            x,
            y,
            scrcpy.ACTION_DOWN
        )

        self.client.control.touch(
            x,
            y,
            scrcpy.ACTION_UP
        )

    def hold(
        self,
        x: int,
        y: int,
        ms: int
    ):

        self.client.control.touch(
            x,
            y,
            scrcpy.ACTION_DOWN
        )

        time.sleep(ms / 1000)

        self.client.control.touch(
            x,
            y,
            scrcpy.ACTION_UP
        )

    def swipe(
        self,
        x1: int,
        y1: int,
        x2: int,
        y2: int,
        steps: int = 10
    ):

        self.client.control.swipe(
            x1,
            y1,
            x2,
            y2,
            steps=steps
        )