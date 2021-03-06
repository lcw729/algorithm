

class Heap:

    def __init__(self, L = []):
        self.A = L
    
    def __str__(self):
        return str(self.A)

    def __len__(self):
        return len(self.A)


    def heapify_down(self, k, n):
        while 2*k + 1 < n: # leaf node에 도달할 때까지
            LC, RC = 2*k + 1, 2*k + 2 # 왼쪽 자식 노드, 오른쪽 자식 노드
            if self.A[LC] > self.A[k]: # 왼쪽 자식 노드가 더 큰 경우
                m = LC 
            else:
                m = k 
            if RC < n and self.A[RC] > self.A[m]: # 오른쪽 자식 노드가 더 큰 경우
                m = RC
            if m != k:
                self.A[k], self.A[m] = self.A[m], self.A[k] 
                k = m # k는 m으로 번경 
            else:
                break

    def make_heap(self):
        n = len(self.A)
        for k in range(n-1, -1, -1):
            self.heapify_down(k, n)


    def heap_sort(self):
        n = len(self.A) 
        for k in range(len(self.A)-1, -1, -1):
            self.A[0], self.A[k] = self.A[k], self.A[0]
            n = n - 1
            self.heapify_down(0, n) # 0부터 n-1까지 재정렬
            
    def heapify_up(self, k):
        p = (k - 1) // 2
        while p >= 0:
            if self.A[p] <= self.A[k]:
                self.A[p], self.A[k] = self.A[k], self.A[p]
                k = p
                p = (k - 1) // 2
            else:
                break
        
    def insert(self, k):
        self.A.append(k)
        self.heapify_up(len(self.A)-1)

    def delete_max(self):
        if len(self.A) == 0:
            return None 
        key = self.A[0]
        self.A[0], self.A[len(self.A)-1] = self.A[len(self.A)-1], self.A[0]
        self.A.pop()
        self.heapify_down(0, len(self.A))
        return key


S = [int(x) for x in input().split()]
H = Heap(S)
H.make_heap()
H.insert(14)
H.insert(25)
H.delete_max()
print(H)