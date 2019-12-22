def maximum(table,key,value,n):
    for_maxes = []
    maximum = [0,0]
    hs = key % n
    massive = table[hs-1:hs+1]
    for itr in massive:
        if itr[0:1] == value[0:1]:
            for_maxes.append([itr[3],min(itr[1],itr[2] + value[2])])
    if for_maxes:
        return(max(for_maxes,key = lambda x: x[1]))
    else:
        return maximum

def hash_value(rects,i):
    sort_rects = sorted(rects, reverse = True)
    square = sort_rects[0]*sort_rects[1]
    return [square, sort_rects + [i]]
    
def hash_table(n):
    return [[] for i in range(n)]

def insert(table,key,value,n):
    square = value[0]
    dim = value[2]
    pos = False 
    hs = key%n
    a = [i for i in range(len(table[hs]))]
    ttable = zip(a,table[hs])
    for index, item in ttable:
        if item[0] == square:
            if item[2] < dim:
                del table[hs][index]
                table.append(value)
                pos = True
                break
    if pos == False:
            table[hs].append(value)
    return 0

def main() :
    
    diameter = 0
    count = 0
    
    n = int(input())
    rects = []
    hash_tbl = hash_table(n)
    for i in range(n):
        rects.append(list((map(int,input().split()))))
        
        if max(rects[i]) <= diameter:
            continue
            
        values = hash_value(rects[i],i)
        maxx = maximum(hash_tbl,values[0],values[1],n)
        if maxx[1] > diameter:
            diameter = maxx[1]
            #count+=1
            
        if diameter < min(rects[i]):
            diameter = min(rects[i])
            count+=1
        insert(hash_tbl,values[0],values[1],n) 
    print (count)
    
    
if __name__== "__main__":
    main()