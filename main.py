#
# Created by Martin Plut and Ryan Romero March 31, 2019
#   Finished and completed by Martin Plut June 24, 2020
# CS415 - Project 2
# Karatsuba Multiplication and Exponentiation
#
#import numpy as np
import math

class Project2():
    def KaratsubaSingle(self, a, b):
        return int(a[0]) * int(b[0])

    def stringToNumAdd(self, a, b):

        return str(int(a) + int(b))
        # a, b = isEqualLength(a, b)
        # if(len(a) == 1 and len(b) == 1):
        #     return str(int(a) + int(b))
        # elif(len(a) == 2 and len(b) == 1):
        #     aTens = a[0] + '0'
        #     aOnes = a[1]
        #     bTens = b[0] + '0'
        #     bOnes = b[1]
        #     onesPlace = int(aOnes) + int(bOnes)
        #     tensPlace = int(aTens) + int(bTens)
        #     return str(tensPlace + onesPlace)
        # else:
        #     return str(int(a) + int(b))

    def reverse(self, s):
        str = ""
        for i in s:
            str = i + str
        return str

    def KaratsubaMultiplication(self, a, b):
        # a = str(abs(int(a)))
        # b = str(abs(int(b)))
        if(len(a) == 0) or (len(b) == 0):
            return 0
        elif ((len(a) == 1) and (len(b) == 1)):
            return self.KaratsubaSingle(a, b)
        else:
            a, b = self.isEqualLength(a, b)
            n = len(b)
            nHalf = n // 2

            # split lists into two
            firstHalfA = a[:nHalf]
            secondHalfA = a[nHalf:]

            firstHalfB = b[:nHalf]
            secondHalfB = b[nHalf:]

            c2 = self.KaratsubaMultiplication(firstHalfA, firstHalfB)
            c0 = self.KaratsubaMultiplication(secondHalfA, secondHalfB)
            # c1 = (KaratsubaMultiplication(stringToNumAdd(firstHalfA, secondHalfA),
            #                               (stringToNumAdd(firstHalfB, secondHalfB))) - (c2+c0))
            a1a2 = self.stringToNumAdd(firstHalfA, secondHalfA)
            b1b2 = self.stringToNumAdd(firstHalfB, secondHalfB)
            c1 = self.KaratsubaMultiplication(a1a2, b1b2) - (c2+c0)

            # return ((c2 * (1 << (nHalf * 2))) + ((c1 - c2 - c0) * (1 << nHalf) + c0))
            # x = c2 * (10 ** (nHalf * 2))
            # y = c1 * (10 ** nHalf)
            # return x + y + c0
            x = str(c2) + '0'*(2*nHalf)
            y = str(c1) + '0'*nHalf
            return abs(int(x) + int(y) + c0)
            # return (c2 << (nHalf * 2) + (c1 << (nHalf)) + c0)

    def isEqualLength(self, a, b):

        lenA = len(a)
        lenB = len(b)

        if(lenA < lenB):
            if(lenB == 3):
                b = '0' + b
            diff = len(b) - lenA
            for i in range(diff, 0, -1):
                a = '0' + a
        elif(lenA > lenB):
            if (lenA == 3):
                a = '0' + a
            diff = len(a) - lenB
            for i in range(diff, 0, -1):
                b = '0' + b
        elif(lenA == 1 and lenB == 1):
            return a, b
        elif (lenA % 2 != 0 and lenB % 2 != 0):
            a = '0' + a
            b = '0' + b
        return a, b

    def exponentiation(self, a, b):

        if b == 0:
            return 1
        elif b == 1:
            return a
        elif (b % 2) == 0:
            e = self.exponentiation(a, b / 2)
            if e < 0:
                e *= -1
            return self.KaratsubaMultiplication(str(self.exponentiation(a, b // 2)), str(self.exponentiation(a, b // 2)))

            # return KaratsubaMultiplication(str(e), str(e))
        else:
            e = self.exponentiation(a, ((b - 1) // 2))
            if e < 0:
                e *= -1

            return self.KaratsubaMultiplication(str(self.exponentiation(a, ((b - 1) // 2))), str(self.exponentiation(a, ((b - 1) // 2))))

            # return KaratsubaMultiplication(str(KaratsubaMultiplication(str(e), str(e))), str(a))

        # if b == 0:
        #     return 1
        # elif b == 1:
        #     return a
        # elif (b % 2) == 0:
        #     # # e = exponentiation(a, b // 2)
        #     # if e < 0:
        #     #     e *= -1
        #     return KaratsubaMultiplication(str(exponentiation(a, b // 2)), str(exponentiation(a, b // 2)))
        # else:
        #     # # e = exponentiation(a, ((b - 1) // 2))
        #     # if e < 0:
        #     #     e *= -1
        #     return KaratsubaMultiplication(str(exponentiation(a, ((b - 1) // 2))), str(exponentiation(a, ((b - 1) // 2))))

    def main(self):
        print(" -- Project 2: Karatsuba Multiplication and Exponentiation using Karatsuba Multiplication -- ")
        print("1) A*B")
        print("2) A**B")
        print("3) quit")
        option = (input("1, 2, or 3?: "))
        while(option != '3'):
            if(option == '1'):
                numA = input("Enter integer A for A*B: ")
                numB = input("Enter integer B for A*B: ")
                print("\n", numA, "*", numB, ":", self.KaratsubaMultiplication(numA, numB), "\n")
            elif option == "2":
                a2 = int(input("Enter integer A for A**B: "))
                b2 = int(input("Enter integer B for A**B: "))
                print("\n", a2, "**", b2, ":", self.exponentiation(a2, b2), "\n")
            else:
                print("Unrecognized input:", input)

            print("1) A*B")
            print("2) A**B")
            print("3) quit")
            option = (input("1, 2 or 3?: "))


if __name__ == '__main__':
    project2 = Project2()
    project2.main()