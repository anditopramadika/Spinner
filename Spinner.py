
List_awal = [[1,2,3],[4,5,6],[7,8,9]]

def counterClockwise(List_awal):
    transposed = [[row[i] for row in List_awal] for i in range(len(List_awal[0]))]
    revTransposed = transposed[::-1]
    return(revTransposed)

print(counterClockwise(List_awal))