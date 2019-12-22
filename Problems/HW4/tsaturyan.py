import sys

def matching(match, mismatch, indel, thr, m, n, p):  
    score = [k*indel for k in range(0, m+1)]      
    for j in range(1, n + 1):
        s = sys.stdin.read(1) 
        d0 = 0
        for i in range(1, m + 1):
            i0 = score[i-1]
            j0 = score[i]
            val = max(d0 + (match if s == p[i-1] else mismatch),
                        j0 + indel,
                        i0 + indel)
            d0 = score[i]
            score[i] = val        
            if i == m:
                if score[i] >= thr:
                    print(j, score[i])
                    
def main():
    ma, mi, d, th = map(int, input().split())
    m, n = map(int, input().split())
    p = input()
    matching(ma, mi, d, th, m, n,p)
    
if __name__== "__main__":
    main()