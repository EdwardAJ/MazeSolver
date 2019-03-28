#fungsi DFS void
def dfs(mat, path_temp, i, j, ifinal, jfinal):
    #BASIS : current array index = goal (pintu keluar) index
    if ((i == ifinal) and (j == jfinal)):
        path_temp.append([i,j])
        path_final = path_temp
        path_temp.remove([i,j])
        #return path_temp
    #REKURSI : cari kanan, atas, kiri, bawah.
    else:
        if (path_temp[i][j+1] == '0'):
            path_temp.append([i,j])
            dfs(mat, path_temp, i, j+1, ifinal, jfinal)
        elif (path_temp[i+1][j] == '0'):
            path_temp.append([i,j])
            dfs(mat, path_temp, i+1, j, ifinal, jfinal)
        elif (path_temp[i][j-1] == '0'):
            path_temp.append([i,j])
            dfs(mat, path_temp, i, j-1, ifinal, jfinal)
        elif (path_temp[i-1][j] == '0'):
            path_temp.append([i,j])
            dfs(mat, path_temp, i-1, j-1, ifinal, jfinal)
        else:
            #tidak melakukan apa-apa.
            #path_temp = []
            #return (path_temp)
