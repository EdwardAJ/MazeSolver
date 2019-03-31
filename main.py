from colorama import init, Fore, Back, Style
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
    count = 0
    #isNotEmpty
    while (queue_infoMat):
        count = count + 1
        #proses elemen pertama dan hapus elemen pertama dalam queue
        path = queue_infoMat[0];  del queue_infoMat[0]

        mat_visited[path.i][path.j] = True
        if (path.i == i_goal and path.j == j_goal):
            print("Iterasi BFS: " , count)
            return path
        else:
            #cek bawah
            if(not isIndexOutOfRange(path.i+1,path.j,mat)):
                if (mat[path.i+1][path.j] == '0' and mat_visited[path.i+1][path.j] == False):
                    #mat_visited[path.i][path.j] = True
                    queue_infoMat.append(InfoArrElement((path.i+1),(path.j),path,0))
            #cek kanan
            if(not isIndexOutOfRange(path.i,path.j+1,mat)):
                if (mat[path.i][path.j+1] == '0' and mat_visited[path.i][path.j+1] == False):
                    #mat_visited[path.i][path.j] = True
                    queue_infoMat.append(InfoArrElement((path.i),(path.j+1),path,0))
            #cek atas
            if(not isIndexOutOfRange(path.i-1,path.j,mat)):
                if (mat[path.i-1][path.j] == '0' and mat_visited[path.i-1][path.j] == False):
                    #mat_visited[path.i][path.j] = True
                    queue_infoMat.append(InfoArrElement((path.i-1),(path.j),path,0))
            #cek kiri
            if(not isIndexOutOfRange(path.i,path.j-1,mat)):
                if (mat[path.i][path.j-1] == '0' and mat_visited[path.i][path.j-1] == False):
                    #mat_visited[path.i][path.j] = True
                    queue_infoMat.append(InfoArrElement((path.i),(path.j-1),path,0))


def Astar(mat, mat_visited, i_awal , j_awal, i_goal, j_goal):
    g_cost = 0
    h_cost = manhattanCost(i_awal,j_awal,i_goal,j_goal)
    cost = g_cost + h_cost
    #deklarasi kelas path
    path = InfoArrElement(i_awal, j_awal, None, cost)
    queue_infoMat.append(path)

    count = 0

    #isNotEmpty
    while (queue_infoMat):
        queue_infoMat.sort(key=lambda path: path.cost)
        count = count + 1

        #proses elemen pertama dan hapus elemen pertama dalam queue
        path = queue_infoMat[0];  del queue_infoMat[0]
        mat_visited[path.i][path.j] = True

        if (path.i == i_goal and path.j == j_goal):
            print("Iterasi A-Star: " , count)
            return path
        else:
            #cek bawah
            if(not isIndexOutOfRange(path.i+1,path.j,mat)):
                if (mat[path.i+1][path.j] == '0' and mat_visited[path.i+1][path.j] == False):
                    g_cost = path.cost - manhattanCost(path.i,path.j,i_goal,j_goal) +1
                    h_cost = manhattanCost(path.i+1,path.j,i_goal,j_goal)
                    cost = g_cost + h_cost
                    #mat_visited[path.i][path.j] = True
                    queue_infoMat.append(InfoArrElement((path.i+1),(path.j),path,cost))
            #cek kanan
            if(not isIndexOutOfRange(path.i,path.j+1,mat)):
                if (mat[path.i][path.j+1] == '0' and mat_visited[path.i][path.j+1] == False):
                    g_cost = path.cost - manhattanCost(path.i,path.j,i_goal,j_goal) +1
                    h_cost = manhattanCost(path.i,path.j+1,i_goal,j_goal)
                    cost = g_cost + h_cost
                    #mat_visited[path.i][path.j] = True
                    queue_infoMat.append(InfoArrElement((path.i),(path.j+1),path,cost))
            #cek atas
            if(not isIndexOutOfRange(path.i-1,path.j,mat)):
                if (mat[path.i-1][path.j] == '0' and mat_visited[path.i-1][path.j] == False):
                    g_cost = path.cost - manhattanCost(path.i,path.j,i_goal,j_goal) +1
                    h_cost = manhattanCost(path.i-1,path.j,i_goal,j_goal)
                    cost = g_cost + h_cost
                    #mat_visited[path.i][path.j] = True
                    queue_infoMat.append(InfoArrElement((path.i-1),(path.j),path,cost))
            #cek kiri
            if(not isIndexOutOfRange(path.i,path.j-1,mat)):
                if (mat[path.i][path.j-1] == '0' and mat_visited[path.i][path.j-1] == False):
                    g_cost = path.cost - manhattanCost(path.i,path.j,i_goal,j_goal) +1
                    h_cost = manhattanCost(path.i,path.j-1,i_goal,j_goal)
                    cost = g_cost + h_cost
                    #mat_visited[path.i][path.j] = True
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
    jarak = 0 ; jarak2 = 0
    #pilihan untuk memasukkan maze dari file external atau dari keyboard.
    #inisialisasi mat, yaitu list of list.
    mat = [] #buat bfs
    mat2 = [] #buat a-star
    namaFile = input(str("Nama File : "))
    getMazeFromFile(mat, namaFile) #buat bfs
    getMazeFromFile(mat2, namaFile) #buat a-star

    print("MAZE AWAL :")
    visualizationAwal(mat) #gambar mazenya yg awal belom dikerjain

    #inisialisasi mat_visited, yaitu list of list berisi boolean visitedTrue atau visitedFalse.
    mat_visitedBFS = [[False]*len(mat[0]) for idx_baris in range(len(mat))]
    mat_visitedAstar = [[False]*len(mat[0]) for idx_baris in range(len(mat))]

    #cari posisi jalan masuk
    for idx_baris in range(len(mat)):
        if (mat[idx_baris][0] == '0'):
            i_awal = idx_baris
            j_awal = 0
            break

    for idx_kolom in range(len(mat[0])):
        if (mat[0][idx_kolom] == '0'):
            i_awal = 0
            j_awal = idx_kolom
            break

    #cari posisi jalan keluar
    for idx_baris in range(len(mat)):
        if (mat[idx_baris][len(mat[idx_baris])-1] == '0'):
            j_goal = len(mat[idx_baris])-1
            i_goal = idx_baris
            break


    for idx_kolom in range(len(mat[0])):
        if (mat[len(mat)-1][idx_kolom] == '0'):
            i_goal = len(mat)-1
            j_goal = idx_kolom
            break

    #lakukan BFS
    path = BFS(mat, mat_visitedBFS, i_awal , j_awal, i_goal, j_goal)
    #Dapatkan Path BFS
    jarak1 = getPath(mat,path,jarak)

    queue_infoMat.clear()
    jarak_2 = 0
    #lakukan A-Star
    path2 = Astar(mat2, mat_visitedAstar, i_awal , j_awal, i_goal, j_goal)
    #Dapatkan Path A-Star
    jarak2 = getPath(mat2,path2,jarak_2)

    queue_infoMat.clear()
    if (mat[i_awal][j_awal] == '2'):
        print("BFS :")
        visualization(mat, i_awal, i_goal, j_awal, j_goal)
        print("jarak adalah:")
        print(jarak1)
        print("A-STAR :")
        visualization(mat2, i_awal, i_goal, j_awal, j_goal)
        print("jarak adalah:")
        print(jarak2)
    else:
        print("TIDAK ADA SOLUSI")

def getPath(mat, path,jarak):
    while (path != None):
        #Jalan yang sudah dikunjungi diganti dengan 2
        mat[path.i][path.j] = '2'
        path = path.parent
        jarak = jarak + 1
    return jarak-1


def visualization(mat, i_awal, i_goal, j_awal, j_goal):
    init(convert=True)
    for i in range(0, len(mat)):
        for j in range(0, len(mat[0])):
            if (mat[i][j] == '2'):
                if (i == i_awal and j == j_awal):
                    print(Back.RED + "S", end = ' ')
                elif (i == i_goal and j == j_goal):
                    print(Back.RED + "F", end = ' ')
                else:
                    print(Back.CYAN + " ", end = ' ')
                print(Style.RESET_ALL, end = '')
            elif (mat[i][j] == '0'):
                print(Back.BLACK + " ", end = ' ')
                print(Style.RESET_ALL, end = '')
            elif (mat[i][j] == '1'):
                print(Back.WHITE + " ", end = ' ')
                print(Style.RESET_ALL, end = '')
        print()
    print()

def visualizationAwal(mat):
    init(convert=True)
    for i in range(0, len(mat)):
        for j in range(0, len(mat[0])):
            if (mat[i][j] == '0'):
                print(Back.BLACK + " ", end = ' ')
                print(Style.RESET_ALL, end = '')
            elif (mat[i][j] == '1'):
                print(Back.WHITE + " ", end = ' ')
                print(Style.RESET_ALL, end = '')
        print()
    print()

if __name__ == '__main__':
    main()
