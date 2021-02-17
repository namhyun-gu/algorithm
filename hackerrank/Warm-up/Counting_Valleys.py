MOUNTAIN = 1
VALLERY = -1
NONE = 0


def countingValleys(steps, path):
    altitude = 0
    ret = 0
    state = NONE

    for p in path:
        if p == "D":
            altitude -= 1
        elif p == "U":
            altitude += 1

        if altitude < 0:
            if state != VALLERY:
                ret += 1
            state = VALLERY
        elif altitude > 0:
            state = MOUNTAIN
        else:
            state = NONE
    return ret


if __name__ == "__main__":
    ret = countingValleys(8, "UDDDUDUU")
    print(ret)