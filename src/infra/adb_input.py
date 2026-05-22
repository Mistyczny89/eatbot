import subprocess


class AdbInput:

    @staticmethod
    def swipe(x1, y1, x2, y2, duration=120):

        subprocess.run([
            "adb",
            "shell",
            "input",
            "swipe",
            str(x1),
            str(y1),
            str(x2),
            str(y2),
            str(duration)
        ])

    @staticmethod
    def tap(x, y):

        subprocess.run([
            "adb",
            "shell",
            "input",
            "tap",
            str(x),
            str(y)
        ])