import tempfile
import os
import shutil
import sys
import unittest
from maya import cmds as mc


class BaseTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        startup_maya_session()


def startup_maya_session():
    print("SETTING UP SESSION")
    currentMayaAppDir = os.environ.get("MAYA_APP_DIR")
    os.environ["MAYA_APP_DIR"] = tempfile.mkdtemp()

    from maya import standalone

    standalone.initialize()

    return {
        "tmpMayaAppDir": os.environ["MAYA_APP_DIR"],
        "origMayaAppDir": currentMayaAppDir,
    }


def setup_environment():
    # Adding package into the environment
    path = get_src_folder_path()
    if path not in sys.path:
        sys.path.append(path)
    from pprint import pprint

    pprint(sys.path)


def get_src_folder_path():
    path = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
    path = os.path.join(path, "src")
    return path


def teardown_maya_session(state):
    from maya import standalone

    standalone.uninitialize()

    try:
        shutil.rmtree(state["tmpMayaAppDir"])
    # Windows hasn't given up the handles to the files yet. So, ignore it.
    except WindowsError:
        pass

    if state["origMayaAppDir"] is not None:
        os.environ["MAYA_APP_DIR"] = state["origMayaAppDir"]
