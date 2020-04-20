import os
import sys
import glob
import argparse

def pythonCommand(cmd):
    cmd = sys.executable + " " + cmd
    ret = os.system(cmd)
    if ret != 0:
        print("%s returned %d" , (cmd, ret))
        raise OSError

def main():
    parser = argparse.ArgumentParser(description="Install and test wheels build",
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("--wheels", type=str, default="dist/*.whl", help="Wheel glob")
    parser.add_argument("--test", type=str, default="-m pytest", help="Test command")
    parms = parser.parse_args()

    for wheelName in glob.glob(parms.wheels):
        pythonCommand("-m pip install --upgrade %s" % (wheelName,))

    pythonCommand(parms.test)

    return 0

if __name__ == "__main__":
    main()