import sys
import math
quaternionToRotate = [0, 0.980785279, -0.195090328, 0]
rotationMatrix = [0, 0, 90]

def checkQuaternionSquareSum(quaternion):
    squareSum = math.sqrt(quaternion[0]**2 + quaternion[1]**2 + quaternion[2]**2 + quaternion[3]**2)
    precision = 1.e-9
    if abs(squareSum - 1) > precision:
        print("Invalid quaternion. Square sum of quaternion " + str(quaternion) + " coordinates not equal to 1 with " + str(precision) + " precision.")
        print("Square sum equals " + str(squareSum))
        sys.exit()

def printMatrix(matrix):
    for row in matrix:
        print(row)

def rotateQuaternion(quaternion, rotation):
    alpha = math.radians(rotationMatrix[0])
    beta  = math.radians(rotationMatrix[1])
    gamma = math.radians(rotationMatrix[2])

    r11 = round( math.cos(alpha)*math.cos(beta)*math.cos(gamma) - math.sin(alpha)*math.sin(gamma), 15)
    r12 = round(-math.cos(alpha)*math.cos(beta)*math.sin(gamma) - math.sin(alpha)*math.cos(gamma), 15)
    r13 = round( math.cos(alpha)*math.sin(beta), 15)

    r21 = round( math.sin(alpha)*math.cos(beta)*math.cos(gamma) + math.cos(alpha)*math.sin(gamma), 15)
    r22 = round(-math.sin(alpha)*math.cos(beta)*math.sin(gamma) + math.cos(alpha)*math.cos(gamma), 15)
    r23 = round( math.sin(alpha)*math.sin(beta), 15)

    r31 = round(-math.sin(beta)*math.cos(gamma), 15)
    r32 = round( math.sin(beta)*math.sin(gamma), 15)
    r33 = round( math.cos(beta), 15)

    translationMatrix = [[r11, r12, r13], 
                         [r21, r22, r23], 
                         [r31, r32, r33]]
    print("Matrix generated with given " + str(rotation) + " rotation matrix:")
    printMatrix(translationMatrix)
    q0 = 1/2*math.sqrt(1 + r11 + r22 + r33)
    q1 = 1/(4*q0)*(r32 - r23)
    q2 = 1/(4*q0)*(r13 - r31)
    q3 = 1/(4*q0)*(r21 - r12)
    newQuaternion = [q0, q1, q2, q3]
    print("Quaternion after rotation with given " + str(rotation) + " rotation matrix equal to " + str(newQuaternion))

if __name__ == '__main__':
    checkQuaternionSquareSum(quaternionToRotate)
    rotateQuaternion(quaternionToRotate, rotationMatrix)