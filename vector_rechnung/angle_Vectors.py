# Durch eine Umformung erhalten wir:   cos=Skalarprodukt(a⋅b)/ ∣a∣⋅∣b∣
import math

from vector_rechnung.mag_vector import magVectors


def angleBetween(v1, v2):
    # print("in function angleBetween: ", v1, v2)
    SkalarProkdukt = v1[0]*v2[0] + v1[1]*v2[1]
    Nenner = magVectors(v1)*magVectors(v2)

    # print(f"angleBetween: Terme: SkalarProkdukt={SkalarProkdukt:.3f}, Nenner={Nenner:.3f}")

    return math.degrees(math.acos(SkalarProkdukt / Nenner))


if __name__ == "__main__":
    pass
