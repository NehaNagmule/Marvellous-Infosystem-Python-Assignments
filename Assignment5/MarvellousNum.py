def checkFactor(icnt, no):
    if no == 0:
        return False

    if no % icnt == 0:
        return True
    else:
        return False


def checkPrime(no):
    if no == 0 or no == 1:
        return False

    iCnt = 2
    while iCnt <= no:
        if checkFactor(iCnt, no) == True:
            break
        iCnt = iCnt + 1

    if iCnt == no:
        return True
    else:
        return False