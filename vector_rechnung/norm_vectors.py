# The norm() function normalizes a vector:
# function norm(v)
# set m to magnitude(v)
# // you can’t normalize a zero vector
# if m=0 then return “error”
# return scaleVector(v,1/m)
# end function
from vector_rechnung.mag_vector import magVectors
from vector_rechnung.scale_vectors import scaleVectors


def normVectors(v1):
    m = magVectors(v1)
    if m == 0:
        return [0,0]
    return scaleVectors(v1, 1/m)



if __name__ == "__main__":
    pass
