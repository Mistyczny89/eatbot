class Touch:
    def tap(self, x: int, y: int):
        raise NotImplementedError

    def hold(self, x: int, y: int, ms: int):
        raise NotImplementedError