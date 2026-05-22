from __future__ import annotations

import time
import scrcpy


# =========================
# CREATE CLIENT
# =========================

client = scrcpy.Client(
    max_fps=30,
    bitrate=16_000_000,
    block_frame=False
)

# =========================
# START SCRCPY
# =========================

client.start(threaded=True)

print("SCRCPY STARTED")

time.sleep(2)

# =========================
# SWIPE DOWN
# =========================

print("SCROLL DOWN")

client.control.swipe(
    500,   # start x
    1700,  # start y
    500,   # end x
    700,   # end y
    move_step_length=5,
    move_steps_delay=0.005
)

time.sleep(2)

# =========================
# SWIPE UP
# =========================

print("SCROLL UP")

client.control.swipe(
    500,
    700,
    500,
    1700,
    move_step_length=5,
    move_steps_delay=0.005
)

print("DONE")

time.sleep(2)