import numpy as np
vec = [1,2,3,2,1,3,4]
for i in range(len(vec)):
    vec[i] *= vec[i]

print(vec)

vec2 = [1,2,23,2,3,21,1]
for i in range(len(vec2)):
    vec2[i] = vec[i]+2

