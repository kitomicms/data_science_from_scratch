## vector
import math

def vector_add(v,w):
    """
    add vectors
    """
    return [v_i + w_i for v_i,w_i in zip(v,w)]

def vector_minus(v,w):
    """add vectors"""
    return [v_i - w_i for v_i,w_i in zip(v,w)]

# [[1,2],[3,4]]

def vector_sum(vectors):
    num_of_elements = len(vectors[0]) # get the number of elements in the first 
    return [sum(vector[n] for vector in vectors)
            for n in range(num_of_elements)]

def scalar_multiply(c,v):
    return [v_i * c for v_i in v]

def vector_mean(vectors):
    n = len(vectors)
    return scalar_multiply(1/n,vector_sum(vectors))

def dot(v,w):
    """sum of all the element of the product"""
    return sum(v_i * w_i for v_i,w_i in zip(v,w))

def sum_of_squares(v):
    return dot(v,v)

def magnitude(v):
    return math.sqrt(sum_of_squares(v)) # square root

def squared_distance(v,w):
    return sum_of_squares(vector_minus(v,w))

def distance(v,w):
    return math.sqrt(squared_distance(v,w))

if __name__ == "__main__":
    pass