# ch3
### ch3 목표! 검색 알고리즘 이해하기 

#### 검색의 종류
* a. 배열 검색
  * 선형 검색 : 무작위로 늘어놓는 데이터 집합에서 검색을 수행한다.
  * 이진 검색 : 일정한 규칙으로 늘어놓는 데이터 집합에서 아주 빠른 검색을 수행한다.
  * 해시법 : 추가, 삭제가 자주 일어나는 데이터 집합에서 아주 빠른 검색을 수행한다.
    - 체인법 : 같은 해시값 데이터를 연결 리스트로 연결하는 방법이다.
    - 오픈 주소법 : 데이터를 위한 해시값이 출동할 때 재해시하는 방법이다.
* b. 연결 리스트 검색
* c. 이진 검색 트리 검색

+ 선택할 수 있는 알고리즘이 다양한 경우에 용도, 목적, 실행 속도, 자료구조 등 여러 사항을 고려해서 선택해야한다.

#### 선형 검색
* 직선 모양으로 늘어선 배열에서 검색하는 경우에 원하는 키값을 가진 원소를 찾을 때까지 맨 앞부터 스캔하여 순서대로 검색하는 알고리즘이다.
* 선형 검색의 종료 조건
    - 검색할 값을 찾지 못하고 배열의 맨 끝까지 지나간 경우 --  검색 실패
    - 검색할 값과 같은 원소를 찾는 경우 -- 검색 성공

#### 보초법
* <h5>선형 검색은 반복할 때마다 2가지 종료 조건을 체크한다. 단순한 판단이지만 이 과정을 계속 반복하면 종료 조건을 검사하는 비용을 무시할 수 없다.</h5>
* <h5>보초법은 이 비용을 반으로 줄이는 방식이다.</h5>
* <h5>검색하고자 하는 키값을 배열의 맨끝에 저장한다.</h5>
* <h5>결국에는 배열을 끝까지 확인하는 과정에서 자신과 같은 원소가 존재하게 된다.</h5>
* <h5>종료시 인덱스 카운터용 변수가 len(a)와 동일한지 그렇지 않은지만 판단하면된다. [ssearch_sentinel.py]참고</h5>
* <h5>검색 실패의 경우, 매번 검사하던 조건문이 필요없어지므로 if문 판단 횟수는 절반으로 줄었다.</h5>

#### 이진 검색
* 원소가 오름차순이나 내림차순으로 정렬된 배열에서 더 효율적으로 검색할 수 있는 알고리즘이다.
* 맨 앞, 맨 끝, 중앙의 인덱스를 각각 pl, pr, pc라고 하자
    * a[pc] < key : 중앙에서 오른쪽으로 한 칸 이동하여 새로운 왼쪽 끝 pl로 지정하고, 검색 범위를 뒤쪽 절반으로 좁힌다.
    * a[pc] > key : 중앙에서 왼쪽으로 한 칸 이동하여 새로운 오른쪽 끝 pr로 지정하고, 검색 범위를 앞쪽 절반으로 좁힌다.

* 이진 검색의 종료 조건
1. a[pc]와 key가 일치하는 경우
2. 검색 범위가 더 이상 없는 경우

#### 복잡도
* 시간 복잡도 : 실행하는 데 필요한 시간을 평가한다.
    * 전체 복잡도는 차원이 가장 높은 복잡도를 선택하는 것이다. 
    * O(1) + O(n) + O(n) + O(1) = O(max(1, n, n, 1)) = O(n)
* 공간 복잡도 : 메모리와 파일 공간이 얼마나 필요한지 평가한다.

##### 선형 검색의 시간 복잡도 [seq_search()함수]
def seq_search(a: Sequence,key: Any) -> Any:
    i = 0               -- O(1)
    while i < n:        -- O(n)
        if a[i] == key: -- O(n)
            return i    -- O(1)
        i += 1          -- O(n)
    return -1           -- O(1)


##### 이진 검색의 시간 복잡도
pl = 0 # 검색 범위 맨 앞 원소 인덱스                -- O(1)
pr = len(a)-1 # 검색 범위 맨 끝 원소 인덱스         -- O(1)
while True:
    pc = (pl + pr) // 2 # 중앙 원소의 인덱스      -- O(logn)
    if a[pc] == key: # 검색 성공                -- O(logn)
        return pc                             -- O(1)
    elif a[pc] < key:                         -- O(logn)
        pl = pc + 1 # 검색 범위를 뒤쪽 절반으로 좁힘 -- O(logn)
    else:                                     -- O(logn)
        pr = pc - 1 # 검색 범위를 앞쪽 절반으로 좁힘 -- O(logn)
    
    if pl > pr:                               -- O(logn)
        break                                 
    return -1 # 검색 실패                       -- O(1)

* O(logN)인 이유
1. 첫 시행 후에는 반이 버려져서 N/2
2. 두 번째 시행 후에는 또 그 반이 버려져서 1/2 x 2/N
3. 세 번째 시행 후에는 또 그 반이 버려져서 1/2 x 1/2 x 2/N
4. 매 시행마다 탐색할 자료의 개수가 반씩 줄어든다. 즉, k번 시행 후에는 (1/2)^k x N개가 남는다.
5. 이렇게 계속해서 탐색을 반복하다보면 최악의 경우, 남은 자료가 1개가 된다. (1/2)^k x N = 1 이다.
6. 양변에 2^k를 곱하고 양변에 로그를 취해주면 k = logN
7. 여기서 k는 시행 횟수를 의미하므로 시간복잡도는 O(logN)


> 2021/03/17 ch3 ~ 이진 검색

