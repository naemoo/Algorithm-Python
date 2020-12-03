import sys

def compareFloat(approx, actual):
    return (True if abs(approx - actual) <= sys.float_info.epsilon else False)