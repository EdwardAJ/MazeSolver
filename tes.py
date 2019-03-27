import string

namaFile = input("Nama File : ")
file = open(namaFile, 'r')
i = 0
arr = []

for baris in file:
    x = baris[:len(baris)-1]
    arr.append(x)

def bfs(arr, temp, i, j, ifinal, jfinal):
    arr[i] = arr[i][:j] + '2' + arr[i][j+1:]
    print(arr)
    if ((i == ifinal) and (j == jfinal)):
        temp.append([i,j])
        return temp
    else:
        if (arr[i][j+1] == '0'):
            temp.append([i,j])
            return bfs(arr, temp, i, j+1, ifinal, jfinal)
        elif (arr[i+1][j] == '0'):
            temp.append([i,j])
            return bfs(arr, temp, i+1, j, ifinal, jfinal)
        elif (arr[i][j-1] == '0'):
            temp.append([i,j])
            return bfs(arr, temp, i, j-1, ifinal, jfinal)
        elif (arr[i-1][j] == '0'):
            temp.append([i,j])
            return bfs(arr, temp, i-1, j-1, ifinal, jfinal)
        else:
            temp = [[]]
            return (temp)

temp = []
temp = bfs(arr,temp,1,0,2,1)
print(temp)

# text = 'abcdefg'
# new = list(text)
# new[6] = 'W'
# ''.join(new)
# print(new)
