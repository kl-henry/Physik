# function intersectionPoint(a, b, c, d)
# set tc1 to b[1]-a[1]
# set tc2 to b[2]-a[2]
# set sc1 to c[1]-d[1]
# set sc2 to c[2]-s[2]
# set con1 to c[1]-a[1]
# set con2 to c[2]-a[2]
# set det to (tc2*sc1-tc1*sc2)
# if det=0 then return “no unique solution”
# set con to tc2*con1-tc1*con2
# set s to con/det
# return c+s*(d-c)
# end function
from vector_rechnung.add_vectors import addVectors
from vector_rechnung.scale_vectors import scaleVectors


def intersectionPoint(a, b, c, d):
    tc1 = b[0] - a[0]
    tc2 = b[1] - a[1]
    sc1 = c[0] - d[0]
    sc2 = c[1] - d[1]
    con1 = c[0] - a[0]
    con2 = c[1] - a[1]

    det = tc2*sc1 - tc1*sc2
    con = tc2*con1 - tc1*con2
    s = con/det
    cd = addVectors(d, scaleVectors(c, -1))
    solution = addVectors(c, scaleVectors(cd,s))
    return solution
