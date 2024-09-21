def invMod(a,mod):
    if a==0:
        return 0
    for i in range(1,mod):
        if(a*i%mod==1):
            return i    
    return 0

def inv_matrix(matrix , mod):
    dim= len(matrix)
    
    idMat=[]
    for i in range(dim):
        row=[]
        for j in range(dim):
            if(i==j):
                row.append(1)
            else:
                row.append(0)

        idMat.append(row)
    
    M = matrix
    for i in range(dim):
        for x in idMat[i]:
            M[i].append(x)

    
    Mcpy= matrix
    ToReducedRowEchelonForm(Mcpy,mod)
    #should be == idMat

    for i in range(dim):
        for j in range(dim):
            if Mcpy[i][j]!= idMat[i][j]:
                raise Exception("Matrix isn't invertible ")
                quit()

    ToReducedRowEchelonForm(M,mod)
    invMat=[]

    for x in range(0,dim):
        row=[]
        for y in range(dim,2*dim):
            row.append(M[x][y])
        
        invMat.append(row)

    return invMat



def ToReducedRowEchelonForm( M,mod):
    if not M: return
    lead = 0
    rowCount = len(M)
    columnCount = len(M[0])
    for r in range(rowCount):
        if lead >= columnCount:
            return
        i = r
        while invMod(M[i][lead],mod) == 0:
            i += 1
            if i == rowCount:
                i = r
                lead += 1
                if columnCount == lead:
                    return
        M[i],M[r] = M[r],M[i]
        lv = M[r][lead]
        
        M[r] = [ mrx * invMod(lv,mod)%mod for mrx in M[r]]
        
        for i in range(rowCount):
            if i != r:
                lv = M[i][lead]
                M[i] = [ (iv - lv*rv)%mod for rv,iv in zip(M[r],M[i])]
        lead += 1
