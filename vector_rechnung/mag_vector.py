# function magnitude(v)
# set s to 0
# repeat with i=1 to the length of v
# add v[i]*v[i] to s
# end repeat
# return sqrt(s)
# end function
import math


def magVectors(v1):
    mag = 0
    for i in range(len(v1)):
        mag += v1[i] * v1[i]
    return math.sqrt(mag)


if __name__ == "__main__":
    pass
