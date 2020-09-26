import sys
import math
import pygame
import unittest

# Vector 2d
def gVector2(x,y):
    return pygame.math.Vector2(x,y)

def gDot(v1,v2):
    return v1.dot(v2)

def gProduct(v1, v2):
    return v1.cross(v2)

# Do lon vector
def gMagnitude(v):
    return pygame.math.Vector2.magnitude(v)

def gMagnitude_squared(v):
    return pygame.math.Vector2.magnitude_squared(v)

def gLength(v):
    return v.length()

def gLength_squared(v):
    return v.length_squared()

def gNormalize(v):
    return v.normalize()

def gNormalize_ip(v):
    return v.normalize_ip()

def gIsNormalized(v):
    return v.is_normalized()

def gScaleToLength():
    return pygame.math.Vector2.scale_to_length()

def gReflect(self,v):
    return pygame.math.Vector2.reflect(self,v)

def gReflect_ip():
    return pygame.math.Vector2.reflect_ip()

def gDistanceTo(v1,v2):
    return v1.distance_to(v2)

def gDistance_Squared_To(v1, v2): # faster than length
    return v1.distance_squared_to(v2)

def gLerp():
    return pygame.math.Vector2.lerp()

def gSLerp():
    return pygame.math.Vector2.slerp()

def gElementTwise():
    return pygame.math.Vector2.elementwise()

def gRotate(v, angle):
    return v.rotate(angle) # degrees

def gRotate_Rad(v, radians):
    return v.rotate_rad(radians) # radians

def gRotate_Rad_ip():
    return pygame.math.Vector2.rotate_ip()

def gRotate_ip_rad():
    return pygame.math.Vector2.rotate_ip_rad()

def gAngleTo(v1,v2):
    return v1.angle_to(v2)

def gAsPolar():
    return pygame.math.Vector2.as_polar()

def gFromPolar():
    return pygame.math.Vector2.from_polar()

def gUpdate():
    return pygame.math.Vector2.update()

class Testing(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_init_vector2(self):
        self.assertEqual(gVector2(9,3), [9,3])

    def test_vector_Equal(self):
        self.assertEqual(gProduct(pygame.math.Vector2(10,9.8), pygame.math.Vector2(9,3)), -58.2)

    def test_dot(self):
        self.assertEqual(gDot(pygame.math.Vector2(10,9.8),  pygame.math.Vector2(9,3)), 119.4)

    def test_Magnitude(self):
        self.assertEqual(gMagnitude(gVector2(9,3)), 9.486832980505138)

    def test_vector_length(self):
        self.assertEqual(gLength(gVector2(9,3)), 9.486832980505138)

    def test_vector_lengthSquared(self):
        self.assertEqual(gLength_squared(gVector2(9,3)), gVector2(9,3).length_squared())

    def test_normalization_vector(self):
        self.assertEqual(gNormalize(gVector2(9,3)), [0.948683, 0.316228])

    def test_isNormalized(self):
        self.assertEqual(gIsNormalized(gVector2(9,3)), False)

    def test_angle_to(self):
        vt1 = gVector2(10,3)
        vt2 = gVector2(2,5)
        self.assertEqual(gAngleTo(vt1, vt2), 51.49934627965456)

    def test_rotation_vector_degrees(self):
        self.assertEqual(gRotate(gVector2(9,3), 180), gVector2(9,3).rotate(180))

    def test_rotation_vector_radians(self):
        self.assertEqual(gRotate_Rad(gVector2(9,3), 3.14), gVector2(9,3).rotate_rad(3.14))

    def test_magnitude_squared(self):
        self.assertEqual(gMagnitude_squared(gVector2(9,3)), pygame.math.Vector2.magnitude_squared(gVector2(9,3)))

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(Testing)
    unittest.TextTestRunner(verbosity=2).run(suite)
