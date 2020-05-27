import sys
import os
import configparser
import yaml

class iniParser:

    cf = ''

    @staticmethod
    def getBaseDir():
        return os.path.abspath('..')

    @staticmethod
    def getCurrentDir():
        return os.path.abspath('.')

    def __init__(self,filename):
        file_path = iniParser.getCurrentDir()+"/"+filename
        self.cf = configparser.ConfigParser()
        self.cf.read(file_path)

    def getValue(self,section,key):
        return self.cf.get(section, key)

    def getAllSections(self):

        return self.cf.sections()

    def getAllKeys(self,section):

        return self.cf.items(section)

class ymlParser:
    pass
