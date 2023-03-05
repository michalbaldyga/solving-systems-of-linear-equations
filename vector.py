from math import sin, sqrt


def create_vector(n):
    vector = []
    for i in range(n):
        vector.append(sin(i*5))
    return vector


def copy_vector(vector):
    copy = []
    for value in vector:
        copy.append(value)
    return copy


def subtract_vectors(v1, v2):
    result = []
    for i in range(len(v1)):
        result.append(v1[i] - v2[i])
    return result


def norm(vector):
    result = 0.0
    for value in vector:
        result += pow(value, 2)
    return sqrt(result)
