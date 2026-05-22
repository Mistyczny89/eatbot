from __future__ import annotations

import scrcpy
import cv2
import numpy as np


class ScrcpyStream:

    def __init__(self):

        self.client = scrcpy.Client(
            max_fps=30,
            bitrate=16_000_000,
            block_frame=False
        )

        self.latest_frame: np.ndarray | None = None

        @self.client.listener("frame")
        def on_frame(frame):

            if frame is not None:
                self.latest_frame = frame

    def start(self):

        self.client.start(threaded=True)

    def get_gray(self):

        if self.latest_frame is None:
            return None

        return cv2.cvtColor(
            self.latest_frame,
            cv2.COLOR_BGR2GRAY
        )