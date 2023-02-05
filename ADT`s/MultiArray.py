from Array import Array
class MultiArray:

    def __init__(self, *dimensions):
        assert len(dimensions) > 1, "Dimensions can not be less than 1"
        self._dims = dimensions
        size = 1
        for d in dimensions:
            assert d > 0, "Dimensions should be greater than 0"
            size *= d
        self._elements = Array(size)
        self._factors = Array(len(dimensions))
        self._computeFactors()

    def numDims(self):
        return len(self._dims) 
    
    def length(self, dim):
        assert dim >= 1 and dim <= len(self._dims),\
        "Dimension component out of range"
        return self._dims[dim-1] 
        
    def clear(self, value):
        self._elements.clear(value)
        
    def __getitem__(self, ndxTuple):
        assert len(ndxTuple) == self.numDims(), "Invalid array subscripts!"
        index = self._computeIndex(ndxTuple)
        assert index is not None, "Array subscript out of range"
        return self._elements[index]

    def __setitem__(self, ndxTuple, value):
        assert len(ndxTuple) == self.numDims(), "Invalid # of array subscripts"
        index = self._computeIndex(ndxTuple)
        assert index is not None, "Array subscript out of range"
        self._elements[index] = value
        
    def _computeIndex(self, idx):
        offset = 0
        for j in range(len(idx)):
            if idx[j] < 0 or idx[j] >= self._dims[j]:
                return None
            else:
                offset += idx[j] * self._factors[j]
                return offset
    def _computeFactors(self):
        self._factors[len(self._factors)-1] = 1
        for j in reversed(range(len(self._factors) - 1)):
            self._factors[j] = self._factors[j+1] * self._dims[j+1]


if __name__ == "__main__":
    # Creating a multi-dimensional array with dimensions 2x3x4
    arr = MultiArray(2, 3, 4)
    print("Number of dimensions: ", arr.numDims())

    # Setting values at various indices
    arr[0, 0, 0] = 10
    arr[0, 1, 1] = 20
    arr[1, 2, 3] = 30

    # Accessing values at various indices
    print("Value at (0, 0, 0): ", arr[0, 0, 0])
    print("Value at (0, 1, 1): ", arr[0, 1, 1])
    print("Value at (1, 2, 3): ", arr[1, 2, 3])

    # Clearing the multi-dimensional array
    arr.clear(0)
    print("Value after clearing the multi-dimensional array: ", arr[0, 0, 0])
