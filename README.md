# quaternion-rotation

# About The Project
Script allows you to rotate a quaternion by XYZ Euler (so rotation about local target axes) angles and produces new quaternion.

# Built With
Python 3.8.0

# Getting started
### Requirements

All required packages in requirements.txt file.

To install all required packages, type "_pip install -r requirements.txt_" in the terminal.

### Working with quaternion-rotation:
1. At the top of the file, input the quaternion you want to rotate in *quaternion_to_rotate* variable.
2. Input also the angle matrix to *angle_matrix* variable.
3. Run the script.
4. After successful execution, program should print simple rotations and after that, the desired rotation.

# Usage
Script comes in handy in robot programming, when you have no other way of rotating a robot target about axes you specify.

# References
Everything About Unit Quaternions to Express Orientations in Robotics + Great Demos [LESSON 12] - https://www.youtube.com/watch?v=Ek9fySVzuq4  
Conversion between quaternions and Euler angles - https://en.wikipedia.org/wiki/Conversion_between_quaternions_and_Euler_angles  
Maths - Conversion Matrix to Quaternion - https://www.euclideanspace.com/maths/geometry/rotations/conversions/matrixToQuaternion/  
Converting a Rotation Matrix to a Quaternion - https://d3cw3dd2w32x2b.cloudfront.net/wp-content/uploads/2015/01/matrix-to-quat.pdf  

# Licence
Distributed under the MIT License. See LICENSE file for more information.
