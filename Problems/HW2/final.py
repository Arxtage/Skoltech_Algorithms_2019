def hash_value(hashs,i):
        sp = sorted(hashs, reverse = True)
        square = sp[0]*sp[1]
        return [square, sp + [i]] 

def maximum(table,key,value,n):
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

def insert(table,key,value,n):
    square = value[0]
    dim = value[2]
    pos = False 
    hs = hashed(key,n)
    a = [i for i in range(len(table[hs]))]
    ttable = zip(a,table[hs])
    for index, item in ttable:
        if item[0] == square:
            if item[2] < dim:
                #delete(table,hs,index)
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

def first(n) :
    
    diameter = 0
    diameter1 = 0
    diameter2 = 0
    count = 0
    
    rects = []
    hash_tbl = hash_table(n)
    
    for i in range(n):
        rects.append(list((map(int,input().split()))))
        
        if max(rects[i]) <= diameter:
            continue
            
        values = hash_value(rects[i],i)

        maxx = maximum(hash_tbl,values[0],values[1],n)
        if maxx[1] > diameter:
            diameter1 = maxx[1]
            #count+=1
            #insert(hash_tbl,values[0],values[1],n)
            #continue
            
        if diameter < min(rects[i]):
            diameter2 = min(rects[i])
            #count+=1
        if max(diameter1, diameter2) > diameter:
            diameter = max(diameter1, diameter2)
            count+=1
        insert(hash_tbl,values[0],values[1],n)
    print (count)
    
def insert2(table,input,value):
    table[input]+=[value]
    
def second(n):
    hash_table = [[] for x in range(n*n)]
 
    radius = 0
    count = 0
    for index in range(1,n+1):
        rect= sorted(list((map(int,input().split()))))
    
        #diagonal = int((rect[1]**2 + rect[2]**2)**(1/2))
        diagonal = (rect[1]*rect[2])%n


        if hash_table[diagonal]:
            for box in sorted(hash_table[diagonal], key=lambda x: x[0],reverse=True):
                if rect[1:] == box[1:]:
                    composed_rect = [None]*3
                    composed_rect[0] = rect[0]+box[0]
                    composed_rect[1:] = rect[1:]
                    composed_rect = sorted(composed_rect)
                   
                    if radius < composed_rect[0]:
                        radius = composed_rect[0]
                        count+=1
                    break
                
                
        if radius < rect[0]:
            radius = rect[0]
            count+=1
        insert2(hash_table, diagonal, rect)
    print(count)
    
def main():
    n = int(input())
    #first_raw = sorted(list((map(int,input().split()))))
    #maxi = first_raw[0]
    if n<11:
        second(n)
    else:
        first(n)
if __name__== "__main__":
    main()