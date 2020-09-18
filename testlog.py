import os, sys
import time
import json
from datetime import datetime
from time import gmtime, strftime, localtime

class Logger:
    logLevel = -1
    logPath = ""
    logName = ""
    def __init__(self, configPath):
        # read config file
        with open('config.json','r' ) as jsonFile:
            data = jsonFile.read()

        jsonObject = json.loads(data)
        self.logLevel = jsonObject["level"]
        self.logPath = jsonObject["path"]
        self.logName = jsonObject["name"]
    
    def logTrace(self, msg):
        print(strftime("%Y-%m-%d %H:%M:%S", localtime()) , "- TRACE: ", msg)

    def logDebug(self, msg):
        print(strftime("%Y-%m-%d %H:%M:%S", localtime()) , "- DEBUG: ", msg)

    def logInfo(self, msg):
        print(strftime("%Y-%m-%d %H:%M:%S", localtime()) , "- INFO: ", msg)

    def logWarning(self, msg):
        print(strftime("%Y-%m-%d %H:%M:%S", localtime()) , "- WARN: ", msg)

    def logRelease(self, msg):
        print(strftime("%Y-%m-%d %H:%M:%S", localtime()) , "- RELEASE: ", msg)

    def logError(self, msg):
        print(strftime("%Y-%m-%d %H:%M:%S", localtime()) , "- ERROR: ", msg)

    def logNone(self, msg):
        print("None")

    def logFunction(self, functionName):
        print(functionName)

    def WriteLog(self,logLevel, msg):
        if logLevel == 0:
            self.logTrace(msg)
        elif logLevel == 1:
            self.logDebug(msg)
        elif logLevel == 2:
            self.logInfo(msg)
        elif logLevel == 3:
            self.logWarning(msg)
        elif logLevel == 4:
            self.logError(msg)
        elif logLevel == 5:
            self.logRelease(msg)
        elif logLevel == 6:
            self.logNone(msg)

    def writeToFile(self,logFile):
        file = open(logFile, 'w')


if __name__ == '__main__':
    log = Logger('config.json')
    log.WriteLog(log.logLevel, 'test log trace')
    log.writeToFile(log.logPath + "\\" + log.logName)
