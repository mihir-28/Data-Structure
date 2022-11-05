from arrayadt import *

class Array2D:
    def __init__(self, nrows, ncols):
        self._theRows = Array(nrows)
        for i in range(nrows):
            self._theRows[i] = Array(ncols)
    
    def numRows(self):
        return len(self._theRows)
    
    def numCols(self):
        return len(self._theRows[0])

    def clear (self, value):
        for r in range(self.numRows()):
            self._theRows[r].clear(value)
    
    def __getitem__(self, ndxTuple):
        assert len(ndxTuple) == 2, "Invalid number of array subscript"
        row = ndxTuple[0]
        col = ndxTuple[1]
        assert row >= 0 and row < self.numRows() and \
            col >= 0 and col < self.numCols(), \
                "Array subscript out of range"
        the1DArray = self._theRows[row]
        return the1DArray[col]

    def __setitem__(self, ndxTuple, value):
        assert len(ndxTuple) == 2, "Invalid number of array subscript"
        row = ndxTuple[0]
        col = ndxTuple[1]
        assert row >= 0 and row < self.numRows() and \
            col >= 0 and col < self.numCols(), \
                "Array subscript out of range"
        the1DArray = self._theRows[row]
        the1DArray[col] = value