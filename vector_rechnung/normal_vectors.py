# function normalVector(vector)
# return vector(-vector[2],vector)
# end function
def normalVector(v1):
    # print("in function vorn: ", v1)
    v1_a = -v1[1]
    v1[1] = v1[0]
    v1[0] = v1_a
    # print("in function: ", v1)
    return v1


if __name__ == "__main__":
    pass
