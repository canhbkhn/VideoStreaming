import sys, os
import constants

# Check type of msg
def checkTypeMsg(msg):
    if type(msg) is int:
        print(type(msg))
        return constants.INT
    elif type(msg) is str:
        print(type(msg))
        return constants.STRING
    elif type(msg) is float:
        print(type(msg))
        return constants.FLOAT

# Format log output
def logFormat(msg):
    if type(msg) is constants.STRING:
        pass

# Split string
def splitString(msg):
    pass

# String length
def strLen(msg):
    return len(msg)

# String start with
def strStartWith(keyword, start, end):
    return str.startswith(keyword, start, end)

# String index()
def strIndex(string):
    pass

# Numeric check
def isNumeric(value):
    pass

# Alpha check
def isAlpha(value):
    pass

checkTypeMsg(10)
checkTypeMsg("10")
checkTypeMsg(10.02)

