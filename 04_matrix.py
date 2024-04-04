from random import randint as r

def nxn_matrix_create(n):
    M=[]
    for sor in range(n):
        row=[]
        for oszlop in range(n):
            row.append(0)
        M.append(row)
    return M
def M_fill(M):
    n=len(M)
    for sor in range(n):
        row=[]
        for oszlop in range(n):
            M[sor][oszlop] = r(1,101)


def M_manual_fill(M):
    n=len(M)
    for sor in range(n):
        for oszlop in range(n):
            M[sor][oszlop] = (int(input("Milyen számot tegyek a " + str(sor) + ". sor " + str(oszlop) + ". oszlopban lévő elemére?: ")))


def M_addition(M1, M2):
    n = len(M1)
    additionM = []
    for sor in range(n):
            temp = []
            for oszlop in range(n):
                temp.append((M1[sor][oszlop]) + (M2[sor][oszlop]))
            additionM.append(temp)
    return additionM



def M_skalarszorzat(M, n): #n a skalár, amivel szorzunk
    n=len(M)
    skalarM=[]
    for sor in range(n):
        temp=[]
        for oszlop in range(n):
            temp.append(n*M[sor][oszlop])
        skalarM.append(temp)
    return skalarM

def M_print(M):
    n=len(M)
    for sor in range(n):
        temp=[]
        for oszlop in range(n):
            temp.append(M[sor][oszlop])
        print(temp)


def M_multip(M1, M2):
  M = nxn_matrix_create(len(M1))
  for i in range(len(M1)):
    for j in range(len(M2[0])):
      for k in range(len(M1[0])):
        M[i][j] += M1[i][k] * M2[k][j]
  return M

def M_transp(M):
    n = len(M)
    TM=nxn_matrix_create(n)
    for i in range(n):
        for j in range(n):
            TM[j][i]=M[i][j]
    return TM

def gauss_elimination(M):
    n = len(M)

    for i in range(n):
        # Search for maximum in this column
        maxEl = abs(M[i][i])
        maxRow = i
        for k in range(i+1, n):
            if abs(M[k][i]) > maxEl:
                maxEl = abs(M[k][i])
                maxRow = k

        # Swap maximum row with current row
        M[maxRow], M[i] = M[i], M[maxRow]

        # Make all rows below this one 0 in current column
        for k in range(i+1, n):
            c = -M[k][i]/M[i][i]
            for j in range(i, n+1):
                if i == j:
                    M[k][j] = 0
                else:
                    M[k][j] += c * M[i][j]

    # Solve equation Ax=b for an upper triangular matrix A
    x = [0 for i in range(n)]
    for i in range(n-1, -1, -1):
        x[i] = M[i][n]/M[i][i]
        for k in range(i-1, -1, -1):
            M[k][n] -= M[k][i] * x[i]
def M_DET(M):
    # Alap eset: egydimenziós mátrix determinánsa
    if len(M) == 1:
        return M[0][0]
    n = len(M)
    det = 0
    # Ha a mátrix csak 2x2-es, csak keresztbe szorzunk, és a balról jobbra lévő szorzatot negáljuk
    if n == 2:
        return M[0][0]*M[1][1] - M[0][1]*M[1][0]

    # Minden más esetben
    for i in range(n):
        # Az első sor i. elemének előjelét változtatjuk és megszorozzuk a rész determinánsával
        elojel = pow(-1,i)
        M_resz = []
        for sor in M[1:]:
            SubMatrix_sor = []
            for j, elem in enumerate(sor):
                if j != i:
                    SubMatrix_sor.append(elem)
            M_resz.append(SubMatrix_sor)
        s_det = M_DET(M_resz)
        det += elojel * M[0][i] * s_det

    return det

n=int(input("Hányszor hányas mátrixot szeretnél? (csak négyzet mátrix lehetséges): "))
matrix1=nxn_matrix_create(n)
matrix2=nxn_matrix_create(n)

valasz=input("Szeretnéd te megadni az értékeket? Ellenkező esetben random számokkal töltöm fel 1 és 100 között (igen/nem): ")
if valasz=="nem":
    M_fill(matrix1)
    M_fill(matrix2)
elif valasz=="igen":
    M_manual_fill(matrix1)
    M_manual_fill(matrix2)

print("Az 1-es mátrix: \n")
M_print(matrix1)
print("\n A 2-es mátrix: \n")
M_print(matrix2)
print("\n A 2 mátrix összegének mátrixa: \n")
M_print(M_addition(matrix1,matrix2))
print("\n Az 1-es mátrix transzponáltja: \n")
M_print(M_transp(matrix1))

print("\n Az 1-es mátrix skalárszorzata 5-tel: \n")
M_print(M_skalarszorzat(matrix1,5))

print("\n Az 1-es és 2-es mátrix szorzata: \n")
M_print(M_multip(matrix1,matrix2))

print("\n Az 1-es mátrix determinánsa: \n")
print(M_DET(matrix1))
