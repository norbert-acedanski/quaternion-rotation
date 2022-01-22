import sys
import math
quaternionToRotate = [0, 0.980785279, -0.195090328, 0]
angleMatrix = [0, 0, 90]

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

def changeQuaternionToRotationMatrix(quaternion, printMatrix):
    if len(quaternion) != 4:
        print("Invalid quaternion length. Quaternion consists of 4 elements, " + str(len(quaternion)) + " given for quaternion " + str(quaternion) + ".")
        sys.exit()
    q0 = quaternion[0]
    q1 = quaternion[1]
    q2 = quaternion[2]
    q3 = quaternion[3]

    r11 = round(q0**2 + q1**2 - q2**2 - q3**3, 15)
    r12 = round(2*(q1*q2 - q0*q3), 15)
    r13 = round(2*(q0*q2 + q1*q3), 15)

    r21 = round(2*(q0*q3 + q1*q2), 15)
    r22 = round(q0**2 - q1**2 + q2**2 - q3**3, 15)
    r23 = round(2*(q2*q3 - q0*q1), 15)

    r31 = round(2*(q1*q3 - q0*q2), 15)
    r32 = round(2*(q0*q1 + q2*q3), 15)
    r33 = round(q0**2 - q1**2 - q2**2 + q3**3, 15)

    matrix = [[r11, r12, r13], 
              [r21, r22, r23], 
              [r31, r32, r33]]
    if printMatrix:
        print("\nQuaternion " + str(quaternion) + " transforms into rotation matrix:")
        for row in matrix:
            print(row)
    return matrix

def changeAngleMatrixToRotationMatrix(angleMatrix, printMatrix):
    if len(angleMatrix) != 3:
        print("Invalid angle matrix length. Angle matrix consists of 3 elements, " + str(len(angleMatrix)) + " given for angle matrix " + str(angleMatrix) + ".")
        sys.exit()
    alpha = math.radians(angleMatrix[0])
    beta  = math.radians(angleMatrix[1])
    gamma = math.radians(angleMatrix[2])

    r11 = round( math.cos(alpha)*math.cos(beta)*math.cos(gamma) - math.sin(alpha)*math.sin(gamma), 15)
    r12 = round(-math.cos(alpha)*math.cos(beta)*math.sin(gamma) - math.sin(alpha)*math.cos(gamma), 15)
    r13 = round( math.cos(alpha)*math.sin(beta), 15)

    r21 = round( math.sin(alpha)*math.cos(beta)*math.cos(gamma) + math.cos(alpha)*math.sin(gamma), 15)
    r22 = round(-math.sin(alpha)*math.cos(beta)*math.sin(gamma) + math.cos(alpha)*math.cos(gamma), 15)
    r23 = round( math.sin(alpha)*math.sin(beta), 15)

    r31 = round(-math.sin(beta)*math.cos(gamma), 15)
    r32 = round( math.sin(beta)*math.sin(gamma), 15)
    r33 = round( math.cos(beta), 15)

    matrix = [[r11, r12, r13], 
              [r21, r22, r23], 
              [r31, r32, r33]]

    if printMatrix:
        print("\nAngle matrix " + str(angleMatrix) + " transforms into rotation matrix:")
        for row in matrix:
            print(row)
    return matrix

def rotateQuaternion(quaternionToRotate, angleRotationMatrix):

    translationMatrix = changeAngleMatrixToRotationMatrix(angleRotationMatrix, False)

    print("\nMatrix generated with given " + str(angleRotationMatrix) + " rotation matrix:")
    printMatrix(translationMatrix)
    # q0 = 1/2*math.sqrt(1 + r11 + r22 + r33)
    # q1 = 1/(4*q0)*(r32 - r23)
    # q2 = 1/(4*q0)*(r13 - r31)
    # q3 = 1/(4*q0)*(r21 - r12)
    # newQuaternion = [q0, q1, q2, q3]
    # print("Quaternion after rotation with given " + str(angleRotationMatrix) + " rotation matrix equal to " + str(newQuaternion))

if __name__ == '__main__':
    changeQuaternionToRotationMatrix([math.sqrt(2)/2, math.sqrt(2)/2, 0, 0], True)
    changeAngleMatrixToRotationMatrix([30, 60, 45], True)
    checkQuaternionSquareSum(quaternionToRotate)
    rotateQuaternion(quaternionToRotate, angleMatrix)