from dataclasses import dataclass


@dataclass(slots=True)
class State:
    active_station: tuple[int, int] | None = None

    def locked(self) -> bool:
        return self.active_station is not None

    def lock(self, pos):
        self.active_station = pos

    def unlock(self):
        self.active_station = None