from arrayadt import Array

class MultiArray:
    def __init__(self, *dimensions):
        assert len(dimensions) > 1, "The multi array must have 2 or more dimensions."
        self._dims = dimensions
        size = 1
        for d in dimensions:
            assert d > 0, "Dimensions must be > 0."
            size *= d
        self._elements = Array(size)
        self._factors = Array(len(dimensions))
        self._computeFactors()

    def numDims(self):
        return len(self._dims)

    def length(self, dim):
        assert dim > 1 and dim < len(self._dims), \
            "Dimension component out of range."
        return self._dims[dim - 1]

    def clear(self, value):
        self._elements.clear(value)

    def __getitem__(self, ndxTuple):
        assert len(ndxTuple) == self.numDims(), \
            "Invalid # of array subscripts."
        index = self._computeIndex(ndxTuple)
        assert index is not None, "Array subscript out of range."
        return self._elements[index]

    def __setitem__(self, ndxTuple, value):
        assert len(ndxTuple) == self.numDims(), \
            "Invalid # of array subscripts."
        index = self._computeIndex(ndxTuple)
        assert index is not None, "Array subscript out of range."
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
        for j in range(self.numDims()):
            self._factors[j] = 1
            for k in range(j + 1, self.numDims()):
                self._factors[j] *= self.numDims[k]