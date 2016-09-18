import os
from os.path import join


def ourrename(tagString,file):
    if tagString in file:
        return
    basedir = tagString + "/"
    taggedFiles = os.rename(basedir + file, basedir + tagString +" "  + file)

class Tagging():
    def __init__(self,tagString):
        if not tagString.startswith("#"):
            return
        files = os.listdir(tagString)
        for file in files:
            ourrename(tagString,file)
class TaggingAllFolderContent():
    def __init__(self):
        tagDirs = os.listdir(".")
        for dir in tagDirs:
            Tagging(dir)
if __name__ == '__main__':
    TaggingAllFolderContent()
