import sys
import math
import numpy
quaternion_to_rotate = [0, 0.980785279, -0.195090328, 0] # with given example, program should print [0, 0.555582588, 0.831461357, 0]
angle_matrix = [0, 0, 90]

def check_quaternion_square_sum(quaternion):
    square_sum = math.sqrt(quaternion[0]**2 + quaternion[1]**2 + quaternion[2]**2 + quaternion[3]**2)
    precision = 1.e-9
    if abs(square_sum - 1) > precision:
        print("\nInvalid quaternion. Square sum of quaternion " + str(quaternion) + " coordinates not equal to 1 with " + str(precision) + " precision.")
        print("Square sum equals " + str(square_sum))
        sys.exit()

def print_matrix_method(matrix):
    for row in matrix:
        print(row)

def change_quaternion_to_rotation_matrix(quaternion, print_matrix):
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
    if print_matrix:
        print("\nQuaternion " + str(quaternion) + " transforms into rotation matrix:")
        print_matrix_method(matrix)
    return matrix

def change_angle_matrix_to_rotation_matrix(angle_matrix, print_matrix):
    if len(angle_matrix) != 3:
        print("\nInvalid angle matrix length. Angle matrix consists of 3 elements, " + str(len(angle_matrix)) + " given for angle matrix " + str(angle_matrix) + ".")
        sys.exit()
    alpha = math.radians(angle_matrix[0])
    beta  = math.radians(angle_matrix[1])
    gamma = math.radians(angle_matrix[2])
    
    x_rotation_matrix = numpy.array([[1,               0,                0],
                                   [0, math.cos(alpha), -math.sin(alpha)],
                                   [0, math.sin(alpha),  math.cos(alpha)]])
    y_rotation_matrix = numpy.array([[ math.cos(beta), 0, math.sin(beta)],
                                   [              0, 1,              0],
                                   [-math.sin(beta), 0, math.cos(beta)]])
    z_rotation_matrix = numpy.array([[math.cos(gamma), -math.sin(gamma), 0],
                                   [math.sin(gamma),  math.cos(gamma), 0],
                                   [              0,                0, 1]])
    partial_matrix = numpy.matmul(z_rotation_matrix, y_rotation_matrix)
    matrix = numpy.matmul(partial_matrix, x_rotation_matrix)

    if print_matrix:
        print("\nAngle matrix " + str(angle_matrix) + " transforms into rotation matrix:")
        print(matrix)
    return matrix

def multiply_two_2D_matices(matrix_1, matrix_2, print_product):
    numpy_matrix_1 = numpy.array(matrix_1)
    numpy_matrix_2 = numpy.array(matrix_2)
    if numpy_matrix_1.dtype.char == "O":
        print("\nInput 1 is not a matrix. Wrong sizes of rows or columns.")
        sys.exit()
    if numpy_matrix_2.dtype.char == "O":
        print("\nInput 2 is not a matrix. Wrong sizes of rows or columns.")
        sys.exit()
    try:
        product_matrix = numpy.matmul(numpy_matrix_1, numpy_matrix_2)
    except ValueError as e:
        print("\n" + str(e))
        sys.exit()
    if print_product:
        print("\nProduct of two given matrices:")
        print(product_matrix)
    return product_matrix

def change_rotation_matrix_to_quaternion(rotation_matrix, print_quaternion):
    if len(rotation_matrix) != 3:
        print("\nInvalid rotation matrix row number. Rotation matrix consists of 3 rows and 3 columns, " + str(len(rotation_matrix)) + " rows given for rotation matrix:")
        print_matrix_method(rotation_matrix)
        sys.exit()
    else:
        for row_number, row in enumerate(rotation_matrix):
            if (len(row) != 3):
                print("\nInvalid rotation matrix size in row " + str(row_number + 1) + ". Rotation matrix consists of 3 rows and 3 columns, but size " + str(len(row)) + " given.")
                sys.exit()
    r11 = round(rotation_matrix[0][0], 15)
    r12 = round(rotation_matrix[0][1], 15)
    r13 = round(rotation_matrix[0][2], 15)

    r21 = round(rotation_matrix[1][0], 15)
    r22 = round(rotation_matrix[1][1], 15)
    r23 = round(rotation_matrix[1][2], 15)

    r31 = round(rotation_matrix[2][0], 15)
    r32 = round(rotation_matrix[2][1], 15)
    r33 = round(rotation_matrix[2][2], 15)

    if r33 < 0:
        if r11 > r22:
            matrix_trace = 1 + r11 - r22 - r33
            q0 = r32 - r23
            q1 = matrix_trace
            q2 = r12 + r21
            q3 = r13 + r31
        else:
            matrix_trace = 1 - r11 + r22 - r33
            q0 = r31 - r13
            q1 = - r12 - r21
            q2 = matrix_trace
            q3 = r23 + r32
    else:
        if r11 < -r22:
            matrix_trace = 1 - r11 - r22 + r33
            q0 = r21 - r12
            q1 = r13 + r31
            q2 = r23 + r32
            q3 = matrix_trace
        else:
            matrix_trace = 1 + r11 + r22 + r33
            q0 = matrix_trace
            q1 = r32 - r23
            q2 = r13 - r31
            q3 = r21 - r12

    # if r11 + r22 + r33 > 0:
    #     square_root = math.sqrt(1 + r11 + r22 + r33)*2
    #     q0 = 1/4*square_root
    #     q1 = (r32 - r23)/square_root
    #     q2 = (r13 - r31)/square_root
    #     q3 = (r21 - r12)/square_root
    # elif (r11 > r22) and (r11 > r33):
    #     square_root = math.sqrt(1 + r11 - r22 - r33)*2
    #     q0 = (r32 - r23)/square_root
    #     q1 = 1/4*square_root
    #     q2 = (r12 + r21)/square_root
    #     q3 = (r13 + r31)/square_root
    # elif r22 > r33:
    #     square_root = math.sqrt(1 - r11 + r22 - r33)*2
    #     q0 = (r13 - r31)/square_root
    #     q1 = (r12 + r21)/square_root
    #     q2 = 1/4*square_root
    #     q3 = (r23 + r32)/square_root
    # else:
    #     square_root = math.sqrt(1 - r11 - r22 + r33)*2
    #     q0 = (r21 - r12)/square_root
    #     q1 = (r13 + r31)/square_root
    #     q2 = (r23 + r32)/square_root
    #     q3 = 1/4*square_root
    quaternion = [q0, q1, q2, q3]
    quaternion = [round(q*0.5/math.sqrt(matrix_trace), 15) for q in quaternion]

    if print_quaternion:
        print("\nRotation matrix:")
        print_matrix_method(rotation_matrix)
        print("transforms into quaterion " + str(quaternion))
    return quaternion

def rotate_quaternion(quaternion_to_rotate, anglerotation_matrix):
    check_quaternion_square_sum(quaternion_to_rotate)
    rotation_matrix = change_angle_matrix_to_rotation_matrix(anglerotation_matrix, False)
    matrixFromquaternion_to_rotate = change_quaternion_to_rotation_matrix(quaternion_to_rotate, False)
    matrixOfNewQuaternion = multiply_two_2D_matices(matrixFromquaternion_to_rotate, rotation_matrix, False)
    newQuaternion = change_rotation_matrix_to_quaternion(matrixOfNewQuaternion, False)
    print("\nQuaternion " + str(quaternion_to_rotate) + " after rotation, with given " + str(anglerotation_matrix) + " angles matrix equal to " + str(newQuaternion))

if __name__ == '__main__':
    for i in range(3):
        angle_matrix_for_simple_rorations = [0, 0, 0]
        for j in range(2):
            angle_matrix_for_simple_rorations[i] = 90*(-1)**j
            rotate_quaternion(quaternion_to_rotate, angle_matrix_for_simple_rorations)
        angle_matrix_for_simple_rorations[i] = 180
        rotate_quaternion(quaternion_to_rotate, angle_matrix_for_simple_rorations)
    rotate_quaternion(quaternion_to_rotate, angle_matrix)