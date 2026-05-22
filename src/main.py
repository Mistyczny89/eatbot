import cv2

from infra.scrcpy_stream import ScrcpyStream


def main():

    stream = ScrcpyStream()
    stream.start()

    while True:

        gray = stream.get_gray()

        if gray is None:
            continue

        cv2.imshow("stream", gray)

        if cv2.waitKey(1) == ord("q"):
            break


if __name__ == "__main__":
    main()