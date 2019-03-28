#Tugas Kecil Strategi Algoritma 2019

#fungsi mendapat maze dari keyboard
#parameter : list of list mat, int baris, int kolom
def getMazeFromKeyboard(mat,baris,kolom):
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

#kelas InfoArrElement, menyimpan posisi elemen,  "bapak" dari elemen, dan cost.
class InfoArrElement:
    #constructor InfoArrElement
    def __init__(self, x,y, parent, cost):
        #posisi
        self.x = x
        self.y = y
        #bapak dari elemen
        self.parent = parent
        #cost
        self.cost = cost


#queue, variabel global, menyimpan status parent
infoMat = []

def BFS(mat, x_awal , y_awal, x_goal, y_goal):
    path = InfoArrElement(x_awal, y_awal, -1, 0)
    infoMat.append(path)
    #cek apakah infoMat empty
    while (not all (infoMat)):
        #hapus element queue
        del infoMat[0]
        if (x_awal == x_goal && y_awal == y_goal):
            return infoMat
        else:
            #cek kanan
            if (mat[x_awal+1][y_awal] == '0'):
                x_awal = x_awal +1
                infoMat.append(InfoArrElement(x_awal,y_awal,path,0))
            #cek bawah
            if (mat[x_awal][y_awal+1] == '0'):
                y_awal = y_awal +1
                infoMat.append(InfoArrElement(x_awal,y_awal,path,0))
            #cek kiri
            if (mat[x_awal-1][y_awal] == '0'):
                x_awal = x_awal -1
                infoMat.append(InfoArrElement(x_awal,y_awal,path,0))
            #cek atas
            if (mat[x_awal][y_awal-1] == '0'):
                y_awal = y_awal -1
                infoMat.append(InfoArrElement(x_awal,y_awal,path,0))



#Program Utama
def main():
    #pilihan untuk memasukkan maze dari file external atau dari keyboard.
    print("Ketik 1 untuk file eksternal, Ketik 0 dari keyboard: ")
    input_param = int(input())
    baris = 0
    if (input_param == 0):
        baris = int (input("Masukkan jumlah baris dari Map: "))
        kolom = int (input("Masukkan jumlah kolom dari Map: "))
        #inisialisasi mat, yaitu list of list.
        mat = [[] for idx_baris in range(baris)]
        getMazeFromKeyboard(mat,baris,kolom)
        print(mat)
    elif (input_param == 1):
        namaFile = input(str("Nama File : "))
        mat = []
        getMazeFromFile(mat, namaFile)
        print(mat)

if __name__ == '__main__':
    main()
