from dataclasses import dataclass


@dataclass(slots=True, frozen=True)
class Config:
    fps_target: int = 20

    icon_threshold: float = 0.80
    button_threshold: float = 0.80

    hold_min_ms: int = 5000
    hold_max_ms: int = 9000