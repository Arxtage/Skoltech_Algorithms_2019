def main():
    
    n, M = input().split()
    n = int(n)
    M = int(M)
    text = input().split()
    L =[len(word) for word in text]
    L.insert(0,None)
    
    index = [None for i in range(n+1)]
    penalty = [0 for i in range(n+1)]
    penalty_candidate = 0
    
    for i in reversed(range(0,n)):
    
        index_candidate = i+1
        wordlength_sum = L[i+1]
        penalty_candidate = (M-wordlength_sum)**2 +penalty[i+1]
        j=i+2
        while j <= n and j-i-1+wordlength_sum+L[j]<=M:
    
            wordlength_sum = wordlength_sum +L[j]
            if((M-j+i+1-wordlength_sum)**2+penalty[j]<penalty_candidate):
                index_candidate=j
                penalty_candidate = (M-j+i+1-wordlength_sum)**2+penalty[j]    
            j = j+1
        index[i] = index_candidate
        penalty[i] = penalty_candidate
        
    current_index = index[0]
    count=1
    while current_index<n:
        current_index = index[current_index]
        count+=1
    print(penalty[0],count)

if __name__== "__main__":
    main()