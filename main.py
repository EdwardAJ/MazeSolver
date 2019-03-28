#import matplotlib.pyplot as plt
#Tugas Kecil Strategi Algoritma 2019
#kelas InfoArrElement, menyimpan posisi elemen,  "bapak" dari elemen, dan cost.
class InfoArrElement:
    #constructor InfoArrElement
    def __init__(self, i,j, parent, cost):
        #posisi
        self.i = i
        self.j = j
        #bapak dari elemen
        self.parent = parent
        #cost
        self.cost = cost

#fungsi mendapat maze dari keyboard
#parameter : list of list mat, int baris, int kolom
def getMazeFromKeyboard(mat,baris):
    #Isi list of list
    for idx_baris in range (baris):
        elemen = input(str()) #splitting string to char
        mat[idx_baris] = list (str(elemen))

#fungsi mendapat maze dari file
#parameter : list of list mat
def getMazeFromFile(mat, namaFile):
    file = open(namaFile, 'r')
    for fileContent_Line in file:
        #splitting string to char
        element = fileContent_Line[:len(fileContent_Line)-1]
        mat.append(list(element))

#queue, variabel global, menyimpan status parent dan cost
queue_infoMat = []
#fungsi BFS, menggunakan struktur data queue
def BFS(mat, mat_visited, i_awal , j_awal, i_goal, j_goal):
    path = InfoArrElement(i_awal, j_awal, None, 0)
    queue_infoMat.append(path)
    #isNotEmpty
    while (queue_infoMat):
        #proses elemen pertama dan hapus elemen pertama dalam queue
        path = queue_infoMat[0];  del queue_infoMat[0]

        #print(str(path.i) + "," + str(path.j))
        if (path.i == i_goal and path.j == j_goal):
            mat_visited[path.i][path.j] = True
            return path
        else:
            #cek bawah
            if(not isIndexOutOfRange(path.i+1,path.j,mat)):
                if (mat[path.i+1][path.j] == '0' and mat_visited[path.i+1][path.j] == False):
                    mat_visited[path.i][path.j] = True
                    queue_infoMat.append(InfoArrElement((path.i+1),(path.j),path,0))
            #cek kanan
            if(not isIndexOutOfRange(path.i,path.j+1,mat)):
                if (mat[path.i][path.j+1] == '0' and mat_visited[path.i][path.j+1] == False):
                    mat_visited[path.i][path.j] = True
                    queue_infoMat.append(InfoArrElement((path.i),(path.j+1),path,0))
            #cek atas
            if(not isIndexOutOfRange(path.i-1,path.j,mat)):
                if (mat[path.i-1][path.j] == '0' and mat_visited[path.i-1][path.j] == False):
                    mat_visited[path.i][path.j] = True
                    queue_infoMat.append(InfoArrElement((path.i-1),(path.j),path,0))
            #cek kiri
            if(not isIndexOutOfRange(path.i,path.j-1,mat)):
                if (mat[path.i][path.j-1] == '0' and mat_visited[path.i][path.j-1] == False):
                    mat_visited[path.i][path.j] = True
                    queue_infoMat.append(InfoArrElement((path.i),(path.j-1),path,0))


def Astar(mat, mat_visited, i_awal , j_awal, i_goal, j_goal):
    g_cost = 0
    h_cost = manhattanCost(i_awal,j_awal,i_goal,j_goal)
    cost = g_cost + h_cost
    path = InfoArrElement(i_awal, j_awal, None, cost)
    queue_infoMat.append(path)
    #isNotEmpty
    while (queue_infoMat):
        #queue_infoMat.sort(key = path.cost)
        #proses elemen pertama dan hapus elemen pertama dalam queue
        path = queue_infoMat[0];  del queue_infoMat[0]
        #print(str(path.i) + "," + str(path.j))
        if (path.i == i_goal and path.j == j_goal):
            mat_visited[path.i][path.j] = True
            return path
        else:
            #cek bawah
            if(not isIndexOutOfRange(path.i+1,path.j,mat)):
                if (mat[path.i+1][path.j] == '0' and mat_visited[path.i+1][path.j] == False):
                    g_cost = path.cost - manhattanCost(path.i,path.j,i_goal,j_goal) +1
                    h_cost = manhattanCost(path.i+1,path.j,i_goal,j_goal)
                    cost = g_cost + h_cost
                    mat_visited[path.i][path.j] = True
                    queue_infoMat.append(InfoArrElement((path.i+1),(path.j),path,cost))
            #cek kanan
            if(not isIndexOutOfRange(path.i,path.j+1,mat)):
                if (mat[path.i][path.j+1] == '0' and mat_visited[path.i][path.j+1] == False):
                    g_cost = path.cost - manhattanCost(path.i,path.j,i_goal,j_goal) +1
                    h_cost = manhattanCost(path.i+1,path.j,i_goal,j_goal)
                    cost = g_cost + h_cost
                    mat_visited[path.i][path.j] = True
                    queue_infoMat.append(InfoArrElement((path.i),(path.j+1),path,cost))
            #cek atas
            if(not isIndexOutOfRange(path.i-1,path.j,mat)):
                if (mat[path.i-1][path.j] == '0' and mat_visited[path.i-1][path.j] == False):
                    g_cost = path.cost - manhattanCost(path.i,path.j,i_goal,j_goal) +1
                    h_cost = manhattanCost(path.i+1,path.j,i_goal,j_goal)
                    cost = g_cost + h_cost
                    mat_visited[path.i][path.j] = True
                    queue_infoMat.append(InfoArrElement((path.i-1),(path.j),path,cost))
            #cek kiri
            if(not isIndexOutOfRange(path.i,path.j-1,mat)):
                if (mat[path.i][path.j-1] == '0' and mat_visited[path.i][path.j-1] == False):
                    g_cost = path.cost - manhattanCost(path.i,path.j,i_goal,j_goal) +1
                    h_cost = manhattanCost(path.i+1,path.j,i_goal,j_goal)
                    cost = g_cost + h_cost
                    mat_visited[path.i][path.j] = True
                    queue_infoMat.append(InfoArrElement((path.i),(path.j-1),path,cost))

def manhattanCost(i,j,i_goal,j_goal):
    cost = abs(i_goal - i) + abs(j_goal - j)
    return cost

def isIndexOutOfRange(i,j,mat):
    if (i >= 0 and i < len(mat) and j >= 0 and j < len(mat[0])):
        return False
    else:
        return True

#Program Utama
def main():
    #pilihan untuk memasukkan maze dari file external atau dari keyboard.
    print("Ketik 1 untuk file eksternal, Ketik 0 dari keyboard: ")
    input_param = int(input())
    #inisialisasi mat, yaitu list of list.
    mat = []
    if (input_param == 0):
        baris = int (input("Masukkan jumlah baris dari Map: "))
        getMazeFromKeyboard(mat,baris)
    elif (input_param == 1):
        namaFile = input(str("Nama File : "))
        getMazeFromFile(mat, namaFile)
    #inisialisasi mat_visited, yaitu list of list berisi boolean visitedTrue atau visitedFalse.
    mat_visitedBFS = [[False]*len(mat[0]) for idx_baris in range(len(mat))]
    mat_visitedAstar = [[False]*len(mat[0]) for idx_baris in range(len(mat))]
    #cari posisi jalan masuk
    for idx_baris in range(len(mat)):
        if (mat[idx_baris][0] == '0'):
            i_awal = idx_baris ; j_awal = 0
            break
    #cari posisi jalan keluar
    for idx_baris in range(len(mat)):
        if (mat[idx_baris][len(mat[idx_baris])-1] == '0'):
            j_goal = len(mat[idx_baris])-1 ; i_goal = idx_baris
            break
    #lakukan BFS
    path = BFS(mat, mat_visitedBFS, i_awal , j_awal, i_goal, j_goal)
    #Dapatkan Path
    while (path != None):
        mat[path.i][path.j] = 2
        path = path.parent

    for i in range (len(mat)):
        for j in range (len(mat[0])):
            print(mat[i][j], end = ' ')
        print()
        print()

    path2 = Astar(mat, mat_visitedAstar, i_awal , j_awal, i_goal, j_goal)

if __name__ == '__main__':
    main()
