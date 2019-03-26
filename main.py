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



#program utama
def main():
    #pilihan untuk memasukkan maze dari file external atau dari keyboard.
    print("Ketik 0 untuk file eksternal, Ketik 1 dari keyboard: ")
    input_param = int(input())
    if (input_param == 0):
        baris = int (input("Masukkan jumlah baris dari Map: "))
        kolom = int (input("Masukkan jumlah kolom dari Map: "))
        #inisialisasi mat, yaitu list of list.
        mat = [[] for idx_baris in range(baris)]
        getMazeFromKeyboard(mat,baris,kolom)
        print(mat)
    elif (input_param == 1):



if __name__ == '__main__':
    main()
