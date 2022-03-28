# function calculatePosition(initialPosition,
# initialVelocity,
# acceleration, time)
# return initialPosition + initialVelocity * time
# + acceleration * time * time/2
# end function
from vector_rechnung.add_vectors import addVectors
from vector_rechnung.scale_vectors import scaleVectors


def calculatePosition(initialPosition, initialVelocity, acceleration, time):
    result = addVectors(initialPosition, scaleVectors(initialVelocity, time))
    result = addVectors(result, scaleVectors(acceleration, time*time/2))
    return result