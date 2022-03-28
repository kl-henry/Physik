# function intersectionTime(p1, v1, p2, v2)
# set tc1 to v1[1]
# set tc2 to v1[2]
# set sc1 to v2[1]
# set sc2 to v2[2]
# set con1 to p2[1]-p1[1]
# set con2 to p2[2]-p1[2]
# set det to (tc2*sc1-tc1*sc2)
# if det=0 then return “no unique solution”
# set con to sc1*con2-sc2*con1
# set t to con/det
# return t
# end function
#intersectionTime((1, 1), (0, 1), (1, -1), (-1, 1))
def intersectionTime(p1, v1, p2, v2):
    tc1 = v1[0]
    tc2 = v1[1]
    sc1 = v2[0]
    sc2 = v2[1]
    con1 = p2[0] - p1[0]
    con2 = p2[1] - p1[1]

    det = (tc2*sc1 - tc1*sc2)
    con = sc1*con2 - sc2*con1
    # print("intersectionTime: det, con, con1, con2:", det, con, con1, con2)
    return con/det
