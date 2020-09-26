import sys
from gmath import gProduct
import math
import pygame

from gmath import*

vtX = pygame.math.Vector2(10,9.8)

vtY = pygame.math.Vector2(9,3)

print(pygame.math.Vector2(10,9.8).cross(pygame.math.Vector2(9,3)))

print(pygame.math.Vector2(5,10))

print(vtX.dot(vtY))

print(2**3)

print(pygame.math.Vector2.magnitude(vtY))

print(pygame.math.Vector2.normalize(vtY))

aa = 9/gLength(vtY)
print(aa)
aa = vtY.normalize()
print(aa)

print(aa.is_normalized())

#print(gReflect(gVector2(9,3)))

vt1 = pygame.math.Vector2(10,3)
vt2 = pygame.math.Vector2(2,5)
print(vt1.angle_to(vt2))

print(vt1.rotate(3.14))

print(vt1.distance_to(vt2))

print(vt1.distance_squared_to(vt2))
