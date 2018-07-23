import random

from copy import deepcopy


class Matrix:
    def __init__(self, nrows, ncols):
        """Construct a (nrows X ncols) matrix"""
        self.rows=nrows
        self.cols=ncols
        self.matrix=[[] for i in range(nrows)]
        for i in range(nrows):
            for j in range(ncols):
                self.matrix[i].append(random.randint(0,9))
    def add(self, m):
        """return a new Matrix object after summation"""
        if self.cols!=m.cols:
            print("Matrixs' size should be in the same size")
            return
        elif self.rows!=m.rows:
            print("Matrixs' size should be in the same size")
            return
        temp=self.matrix
        for i in range(self.rows):
            for j in range(self.cols):
                self.matrix[i][j]=temp[i][j]+m.matrix[i][j]
        print("="*10,"A + B","="*10)
        self.display()
    def sub(self, m):
        """return a new Matrix object after substraction"""
        if self.cols!=m.cols:
            print("Matrixs' size should be in the same size")
            return
        elif self.rows!=m.rows:
            print("Matrixs' size should be in the same size")
            return
        temp=self.matrix
        for i in range(self.rows):
            for j in range(self.cols):
                self.matrix[i][j]=temp[i][j]-m.matrix[i][j]
        print("="*10,"A - B","="*10)
        self.display()

    def mul(self, m):
        """return a new Matrix object after multiplication"""
        if self.cols!=m.rows:
            print("Matrixs' size should be in the same size")
            return
        temp=[[] for i in range(self.rows)]
        for i in range(self.rows):
            for j in range(self.cols):
                temp[i].append(self.matrix[i][j])
        for i in range(self.rows):
            for j in range(m.cols):
                sum=0
                for k in range(self.cols):
                    sum+=temp[i][k]*(m.matrix[k][j])
                self.matrix[i][j]=sum
        print("="*10,"A * B","="*10)
        self.display()

    def transpose(self):
        """return a new Matrix object after transpose"""
        if self.rows!=self.cols:
            print("can't transpose in different cols and rows size ")
            return
        temp=[[] for i in range(self.rows)]
        for i in range(self.rows):
            for j in range(self.cols):
                temp[i].append(self.matrix[i][j])
        for i in range(self.rows):
            for j in range(self.cols):
                if i==j:
                    continue
                self.matrix[i][j]=temp[j][i]
        print("="*10,"Transpose","="*10)
        self.display()
    def display(self):
        """Display the content in the matrix"""
        for i in range(self.rows):
            for j in range(self.cols):
                print('{0:>3}'.format(self.matrix[i][j]),end = " ")
            print()
            
Arows=int(input("Enter A Matrix's rows :"))
Acols=int(input("Enter A Matrix's cols :"))
Brows=int(input("Enter B Matrix's rows :"))
Bcols=int(input("Enter B Matrix's cols :"))
A=Matrix(Arows,Acols)
B=Matrix(Brows,Bcols)
A.add(B)
A.transpose()
A.sub(B)
A.mul(B)

