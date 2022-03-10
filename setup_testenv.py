import sys
import os


location = os.path.dirname(__file__)
src = os.path.join(location, "src")


def setup_testenv():
    if src not in sys.path:
        sys.path.insert(0, src)


if __name__ == '__main__':
    setup_testenv()
