from Array import Array

class Array2D:
    def __init__(self, rows, cols) -> None:
        self.Array = Array(rows)
        for i in range(rows):
            self.Array[i] = Array(cols)

    def numRows(self):
        return len(self.Array)
    
    def numCols(self):
        return len(self.Array[0])
    
    def remove(self, row, col):
        assert row >= 0 and row < self.numRows() and col >= 0 and col < self.numCols(), "Rows and Cols out of range"
        self.Array[row][col] = None                
    
    def setitem(self, row, col, value):
        assert row >= 0 and row < self.numRows() and col >= 0 and col < self.numCols(), "Rows and Cols out of range"
        self.Array[row][col] = value

    def getitem(self, row, col):
        assert row >= 0 and row < self.numRows() and col >= 0 and col < self.numCols(), "Rows and Cols out of range"
        return self.Array[row][col]
    
    def printValue(self):
        for i in range(self.numRows()):
            print()
            for j in range(self.numCols()):
                print(self.Array[i][j], end=" ")
    # Extra functions:
    def transpose(self):
        assert self.numRows() == self.numCols(), "Rows and Cols are not equal"
        transArray = Array2D(self.numRows(), self.numCols())
        for i in range(self.numRows()):
            for j in range(self.numCols()):
                transArray.setitem(j, i, self.Array[i][j])
        transArray.printValue()

    def addSubValue(self, Array2, operator):
        assert self.numRows() == Array2.numRows() and self.numCols() == Array2.numCols(), "Rows and Cols are not matched"
        newArray = Array2D(self.numRows(), self.numCols())
        for i in range(self.numRows()):
            for j in range(self.numCols()):
                if operator == '+':
                    newArray.setitem(i, j, (self.Array[i][j] + Array2.Array[i][j]))
                elif operator == '-':
                    newArray.setitem(i, j, (self.Array[i][j] - Array2.Array[i][j]))
        newArray.printValue()

    def add(self, Array2):
        self.addSubValue(Array2, '+')
    
    def sub(self, Array2):
        self.addSubValue(Array2, '-')

    def MulMatrix(self, Array2):
        assert self.numRows() == Array2.numCols(), "No. of rows of 1st matrix and no. of columns of 2nd matrix are not equal"
        mulArray = Array2D(self.numRows(), self.numCols())
        tempLst = []
        tempVar = 0
        for i in range(self.numRows()):
            tempVar = 0
            for j in range(self.numRows()):
                for k in range(self.numCols()):
                    value = self.Array[i][k] * Array2.Array[k][i]
                    tempLst.append(value)
                mulArray.setitem(i,j, sum(tempLst))
                tempVar += 1
                tempLst = []
        return mulArray.printValue()
    
    def scaleArray(self, value):
        assert len(self.Array) != 0, "Array is empty"
        scaleArray = Array2D(self.numRows(), self.numCols())
        for i in range(self.numRows()):
            for j in range(self.numCols()):
                scaleArray[i][j] = self.Array[i][j] * value
        return scaleArray.printValue()
    
    
obj = Array2D(5,5)
value = 1
for i in range(5):
    for j in range(5):
        obj.setitem(i, j, value)
    value += 1
obj.printValue()
obj2 = Array2D(5,5)
value = 1
for i in range(5):
    for j in range(5):
        obj2.setitem(i, j, value)
    value += 1

print()
print(f"\nTranspose:")
obj.transpose()

print()
print(f"\nAddition:")
obj.add(obj2)

print()
print(f"\nMultiplication:")
obj.MulMatrix(obj2)

print('\n\nAnd so on')