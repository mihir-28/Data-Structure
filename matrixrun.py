from matrixadt import *

m1 = Matrix(2, 3)
m1[0, 0] = 1
m1[0, 1] = 2
m1[0, 2] = 3
m1[1, 0] = 4
m1[1, 1] = 5
m1[1, 2] = 6
print("M1: ")
m1.printMat()

m2 = Matrix(3, 2)
m2[0, 0] = 7
m2[0, 1] = 8
m2[1, 0] = 9
m2[1, 1] = 10
m2[2, 0] = 11
m2[2, 1] = 12
print("M2: ")
m2.printMat()

m3 = m1 + m1
print("M3(Add): ")
m3.printMat()

m4 = m1 - m1
print("M4(Sub): ")
m4.printMat()

m5 = m1 * m2
print("M5(Mul): ")
m5.printMat()

m6 = m2.transpose()
print("M6(Trans): ")
m6.printMat()

m2.scaleBy(5)
print("M7(Scale): ")
m2.printMat()
