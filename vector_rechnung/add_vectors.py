# function addVectors(v1, v2)
# // assume v1 and v2 are arrays of the same length
# set newVector to an empty array
# repeat for i=1 to the length of v1
# append v1[i]+v2[i] to newVector
# end repeat
# return newVector
# end function

def addVectors(v1, v2):
    newVector = []
    for i in range(len(v1)):
        newVector.append(v1[i] + v2[i])
    return newVector


if __name__ == "__main__":
    pass
