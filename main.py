#Tugas Kecil Strategi Algoritma 2019

#fungsi mendapat maze dari keyboard
#parameter : list of list mat, int baris, int kolom
def getMazeFromKeyboard(mat,baris,kolom):
    #Isi list of list
    for idx_baris in range (baris):
        elemen = input(str())
        mat[idx_baris] = list (map (int, str(elemen))
        )
#fungsi mendapat maze dari file
#parameter : list of list mat
def getMazeFromFile(mat):
    namaFile = input("Nama File : ")
    file = open(namaFile, 'r')
    for baris in file:
        x = baris[:len(baris)-1]
        mat.append(list(x))


#program utama
def main():
    #pilihan untuk memasukkan maze dari file external atau dari keyboard.
    print("Ketik 1 untuk file eksternal, Ketik 0 dari keyboard: ")
    input_param = int(input())
    if (input_param == 0):
        baris = int (input("Masukkan jumlah baris dari Map: "))
        kolom = int (input("Masukkan jumlah kolom dari Map: "))
        #inisialisasi mat, yaitu list of list.
        mat = [[] for idx_baris in range(baris)]
        getMazeFromKeyboard(mat,baris,kolom)
        print(mat)
    elif (input_param == 1):
        mat = []
        getMazeFromFile(mat)
        print(mat)

# def bfs(arr, temp, i, j, ifinal, jfinal):
#     arr[i] = arr[i][:j] + '2' + arr[i][j+1:]
#     print(arr)
#     if ((i == ifinal) and (j == jfinal)):
#         temp.append([i,j])
#         return temp
#     else:
#         if (arr[i][j+1] == '0'):
#             temp.append([i,j])
#             return bfs(arr, temp, i, j+1, ifinal, jfinal)
#         elif (arr[i+1][j] == '0'):
#             temp.append([i,j])
#             return bfs(arr, temp, i+1, j, ifinal, jfinal)
#         elif (arr[i][j-1] == '0'):
#             temp.append([i,j])
#             return bfs(arr, temp, i, j-1, ifinal, jfinal)
#         elif (arr[i-1][j] == '0'):
#             temp.append([i,j])
#             return bfs(arr, temp, i-1, j-1, ifinal, jfinal)
#         else:
#             temp = []
#             return (temp)

if __name__ == '__main__':
    main()
