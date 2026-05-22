from infra.adb_input import AdbInput
import time


def main():

    time.sleep(2)

    print("SWIPE DOWN")

    AdbInput.swipe(
        500, 1700,
        500, 700,
        duration=120
    )

    time.sleep(1)

    print("SWIPE UP")

    AdbInput.swipe(
        500, 700,
        500, 1700,
        duration=120
    )


if __name__ == "__main__":
    main()