def hash_value(hashs,i):
        sp = sorted(hashs, reverse = True)
        square = sp[0]*sp[1]
        return [square, sp + [i]] 

def search_max(table,key,value,n):
    maximum = [0,0]
    massive = lookup(table,key,n)
    for itr in massive:
        if itr[0] == value[0]:
            return [itr[3],min(itr[1],itr[2] + value[2])]
    return maximum

def hash_table(n):
    return [[] for i in range(n)]

def hashed(key,n):
    return key % n

def ins(table,key,value,n):
    
    square = value[0]
    dim = value[2]
    pos = False 
    hs = hashed(key,n)
    a = [i for i in range(len(table[hs]))]
    ttable = zip(a,table[hs])
    for index, item in ttable:
        if item[0] == square:
            if item[2] < dim:
                delete(table,hs,index)
                table.append(value)
                pos = True
                break
    if pos == False:
            table[hs].append(value)
    return 0

def lookup(table,key,n):
    hs = hashed(key,n)
    return table[hs]

def delete(table,hs,index):
    del table[hs][index]
    return 0

def main() :
    count = 0
    n = int(input())
    hashs = []
    for i in range(n):
        hashs.append(list((map(int,input().split()))))
        
    radius = 0
    radius1 = 0
    radius2 = 0
    
    hash_tbl = hash_table(n)
    for i in range(n):
        if radius <= min(hashs[i]):
            radius1 = min(hashs[i])
            
        if max(hashs[i]) <= radius:
            continue    
        values = hash_value(hashs[i],i)
        maxx = search_max(hash_tbl,values[0],values[1],n)
        if maxx[1] > radius:
            radius2 = maxx[1]
        if max(radius1, radius2) > radius:
            radius = max(radius1, radius2)
            count+=1
        ins(hash_tbl,values[0],values[1],n)
    print(count)    
    
if __name__== "__main__":
    main()