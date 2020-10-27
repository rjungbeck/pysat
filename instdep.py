import argparse
import sys
import os
import platform
import re

import requests

suffixes= {
    (3, 6, "32bit"): "cp36-cp36m-win32",
    (3, 7, "32bit"): "cp37-cp37m-win32",
    (3, 8, "32bit"): "cp38-cp38-win32",
    (3, 9, "32bit"): "cp39-cp39-win32",
    (3, 6, "64bit"): "cp36-cp36m-win_amd64",
    (3, 7, "64bit"): "cp37-cp37m-win_amd64",
    (3, 8, "64bit"): "cp38-cp38-win_amd64",
    (3, 9, "64bit"): "cp39-cp39-win_amd64"
}

def pythonCall(cmd):
    fullCommand= sys.executable + " " + cmd
    print(fullCommand)
    os.system(fullCommand)

def main():
    parser=argparse.ArgumentParser(description="Dependency installation",
                                   formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("--releaseUrl", type=str, default="https://api.github.com/repos/rjungbeck/pypblib/releases/latest",
                        help="Reelease URL")
    parms=parser.parse_args()

    req=requests.get(parms.releaseUrl)
    rsp=req.json()

    version=sys.version_info[:2]
    architecture=platform.architecture()[0]
    wheelId=(version[0], version[1], architecture)
    suffix=suffixes[wheelId]

    print("Suffix", suffix)


    for asset in rsp["assets"]:
        print(asset["name"])
        if suffix in asset["name"]:
            pythonCall("-m pip install --upgrade %s" % (asset["browser_download_url"]))

if __name__=="__main__":
    main()