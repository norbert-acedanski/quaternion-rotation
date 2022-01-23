import sys
import math
import numpy
# quaternionToRotate = [1, 0, 0, 0]
quaternionToRotate = [0, 0.980785279, -0.195090328, 0]
# with given example, program should print [0, 0.831461357, 0.555582588, 0]
# quaternionToRotate = [0, 0.831469616,  0.555570228, 0]
angleMatrix = [0, 0, 90]

def checkQuaternionSquareSum(quaternion):
    squareSum = math.sqrt(quaternion[0]**2 + quaternion[1]**2 + quaternion[2]**2 + quaternion[3]**2)
    precision = 1.e-9
    if abs(squareSum - 1) > precision:
        print("\nInvalid quaternion. Square sum of quaternion " + str(quaternion) + " coordinates not equal to 1 with " + str(precision) + " precision.")
        print("Square sum equals " + str(squareSum))
        sys.exit()

def printMatrixMethod(matrix):
    for row in matrix:
        print(row)

def changeQuaternionToRotationMatrix(quaternion, printMatrix):
    if len(quaternion) != 4:
        print("\nInvalid quaternion length. Quaternion consists of 4 elements, " + str(len(quaternion)) + " given for quaternion " + str(quaternion) + ".")
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
        printMatrixMethod(matrix)
    return matrix

def changeAngleMatrixToRotationMatrix(angleMatrix, printMatrix):
    if len(angleMatrix) != 3:
        print("\nInvalid angle matrix length. Angle matrix consists of 3 elements, " + str(len(angleMatrix)) + " given for angle matrix " + str(angleMatrix) + ".")
        sys.exit()
    alpha = math.radians(angleMatrix[0])
    beta  = math.radians(angleMatrix[1])
    gamma = math.radians(angleMatrix[2])
    
    xRotationMatrix = numpy.array([[1,               0,                0],
                                   [0, math.cos(alpha), -math.sin(alpha)],
                                   [0, math.sin(alpha),  math.cos(alpha)]])
    yRotationMatrix = numpy.array([[ math.cos(beta), 0, math.sin(beta)],
                                   [              0, 1,              0],
                                   [-math.sin(beta), 0, math.cos(beta)]])
    zRotationMatrix = numpy.array([[math.cos(gamma), -math.sin(gamma), 0],
                                   [math.sin(gamma),  math.cos(gamma), 0],
                                   [              0,                0, 1]])
    partialMatrix = numpy.matmul(zRotationMatrix, yRotationMatrix)
    matrix = numpy.matmul(partialMatrix, xRotationMatrix)

    if printMatrix:
        print("\nAngle matrix " + str(angleMatrix) + " transforms into rotation matrix:")
        print(matrix)
    return matrix

def multiplyTwo2DMatices(matrix1, matrix2, printProduct):
    numpyMatrix1 = numpy.array(matrix1)
    numpyMatrix2 = numpy.array(matrix2)
    if numpyMatrix1.dtype.char == "O":
        print("\nInput 1 is not a matrix. Wrong sizes of rows or columns.")
        sys.exit()
    if numpyMatrix2.dtype.char == "O":
        print("\nInput 2 is not a matrix. Wrong sizes of rows or columns.")
        sys.exit()
    try:
        productMatrix = numpy.matmul(numpyMatrix1, numpyMatrix2)
    except ValueError as e:
        print("\n" + str(e))
        sys.exit()
    if printProduct:
        print("\nProduct of two given matrices:")
        print(productMatrix)
    return productMatrix

def changeRotationMatrixToQuaternion(rotationMatrix, printQuaternion):
    if len(rotationMatrix) != 3:
        print("\nInvalid rotation matrix row number. Rotation matrix consists of 3 rows and 3 columns, " + str(len(rotationMatrix)) + " rows given for rotation matrix:")
        printMatrixMethod(rotationMatrix)
        sys.exit()
    else:
        for rowNumber, row in enumerate(rotationMatrix):
            if (len(row) != 3):
                print("\nInvalid rotation matrix size in row " + str(rowNumber + 1) + ". Rotation matrix consists of 3 rows and 3 columns, but size " + str(len(row)) + " given.")
                sys.exit()
    r11 = rotationMatrix[0][0]
    r12 = rotationMatrix[0][1]
    r13 = rotationMatrix[0][2]

    r21 = rotationMatrix[1][0]
    r22 = rotationMatrix[1][1]
    r23 = rotationMatrix[1][2]

    r31 = rotationMatrix[2][0]
    r32 = rotationMatrix[2][1]
    r33 = rotationMatrix[2][2]

    if r11 + r22 + r33 > 0:
        squareRoot = math.sqrt(1 + r11 + r22 + r33)*2
        q0 = 1/4*squareRoot
        q1 = (r32 - r23)/squareRoot
        q2 = (r13 - r31)/squareRoot
        q3 = (r21 - r12)/squareRoot
    elif (r11 > r22) and (r11 > r33):
        squareRoot = math.sqrt(1 + r11 - r22 - r33)*2
        q0 = (r32 - r23)/squareRoot
        q1 = 1/4*squareRoot
        q2 = (r12 + r21)/squareRoot
        q3 = (r13 + r31)/squareRoot
    elif r22 > r33:
        squareRoot = math.sqrt(1 - r11 + r22 - r33)*2
        q0 = (r13 - r31)/squareRoot
        q1 = (r12 + r21)/squareRoot
        q2 = 1/4*squareRoot
        q3 = (r23 + r32)/squareRoot
    else:
        squareRoot = math.sqrt(1 - r11 - r22 + r33)*2
        q0 = (r21 - r12)/squareRoot
        q1 = (r13 + r31)/squareRoot
        q2 = (r23 - r32)/squareRoot
        q3 = 1/4*squareRoot
    quaternion = [q0, q1, q2, q3]
    quaternion = [round(q, 15) for q in quaternion]

    if printQuaternion:
        print("\nRotation matrix:")
        printMatrixMethod(rotationMatrix)
        print("transforms into quaterion " + str(quaternion))
    return quaternion

def rotateQuaternion(quaternionToRotate, angleRotationMatrix):
    rotationMatrix = changeAngleMatrixToRotationMatrix(angleRotationMatrix, False)
    matrixFromQuaternionToRotate = changeQuaternionToRotationMatrix(quaternionToRotate, False)
    matrixOfNewQuaternion = multiplyTwo2DMatices(matrixFromQuaternionToRotate, rotationMatrix, False)
    newQuaternion = changeRotationMatrixToQuaternion(matrixOfNewQuaternion, False)
    print("\nQuaternion " + str(quaternionToRotate) + " after rotation, with given " + str(angleRotationMatrix) + " angles matrix equal to " + str(newQuaternion))

if __name__ == '__main__':
    checkQuaternionSquareSum(quaternionToRotate)
    rotateQuaternion(quaternionToRotate, angleMatrix)