class Matrix(object):
    def __init__(self, matrix_string):
        #Convert matrix_string to list of lists a 2D list
        self.matrix = []
        self.matrix = matrix_string.splitlines()
        self.matrix = [self.matrix[i].split() for i in range(0,len(self.matrix))]
        #Convert the str in list to int in list
        for i in range(0,len(self.matrix)):
            for j in range (0,len(self.matrix[i])):
                self.matrix[i][j] = int(self.matrix[i][j])
        print(self.matrix)

    def row(self, index):
        return self.matrix[index-1]

    def column(self, index):
        return [self.matrix[i][index-1] for i in range(0,len(self.matrix))]