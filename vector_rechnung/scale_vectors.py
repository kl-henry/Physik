# function scaleVector(v, s)
# repeat for i=1 to the length of v
# multiply v[i] by s
# end repeat
# return v
# end function

def scaleVectors(v1, x):
    my_new_list = []
    for i in range(len(v1)):
        my_new_list.append(v1[i]*x)
    return my_new_list


if __name__ == "__main__":
    pass
