class ArrayOp:
    @staticmethod
    def addarreays(matrixa, matrixb):
        val = [0, 0, 0]
        i = 0
        while i < 3:
            val[i] = matrixa[i] + matrixb[i]
            i = i + 1
        return val

    @staticmethod
    def subarreays(matrixa, matrixb):
        val = [0, 0, 0]
        i = 0
        while i < 3:
            val[i] = matrixa[i] - matrixb[i]
            i = i + 1
        return val
