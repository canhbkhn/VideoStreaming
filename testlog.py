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
        # init config
        jsonObject = json.loads(data)
        self.logLevel = jsonObject["level"]
        self.logPath = jsonObject["path"]
        self.logName = jsonObject["name"]

    def writeToFile(self,logFile, msg):
        file = open(logFile, 'a')
        file.write(msg)
        file.close()
       
    
    def logTrace(self, msg):
        print(strftime("%Y-%m-%d %H:%M:%S", localtime()) , "- TRACE: ", msg)
        content = strftime("%Y-%m-%d %H:%M:%S", localtime()) + " - TRACE: " + msg + '\n'
        self.writeToFile(self.logPath + "\\" + self.logName, content)

    def logDebug(self, msg):
        print(strftime("%Y-%m-%d %H:%M:%S", localtime()) , "- DEBUG: ", msg)
        content = strftime("%Y-%m-%d %H:%M:%S", localtime()) + " - DEBUG: " + msg + '\n'
        self.writeToFile(self.logPath + "\\" + self.logName, content)

    def logInfo(self, msg):
        print(strftime("%Y-%m-%d %H:%M:%S", localtime()) , "- INFO: ", msg)
        content = strftime("%Y-%m-%d %H:%M:%S", localtime()) + " - INFO: " + msg + '\n'
        self.writeToFile(self.logPath + "\\" + self.logName, content)

    def logWarning(self, msg):
        print(strftime("%Y-%m-%d %H:%M:%S", localtime()) , "- WARN: ", msg)
        content = strftime("%Y-%m-%d %H:%M:%S", localtime()) + " - WARN: " + msg + '\n'
        self.writeToFile(self.logPath + "\\" + self.logName, content)

    def logRelease(self, msg):
        print(strftime("%Y-%m-%d %H:%M:%S", localtime()) , "- RELEASE: ", msg)
        content = strftime("%Y-%m-%d %H:%M:%S", localtime()) + " - RELEASE: " + msg + '\n'
        self.writeToFile(self.logPath + "\\" + self.logName, content)

    def logError(self, msg):
        print(strftime("%Y-%m-%d %H:%M:%S", localtime()) , "- ERROR: ", msg)
        content = strftime("%Y-%m-%d %H:%M:%S", localtime()) + " - ERROR: " + msg + '\n'
        self.writeToFile(self.logPath + "\\" + self.logName, content)

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



if __name__ == '__main__':
    log = Logger('config.json')
    log.WriteLog(log.logLevel, 'test log trace')
