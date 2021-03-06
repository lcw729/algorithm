# 이진 검색 알고리즘

from typing import Sequence, Any


def binary_search(a: Sequence, key: Any) -> int:
    pl, pr = 0, len(a)-1 # 검색 범위 맨 앞 원소 인덱스, 검색 범위 맨 끝 원소 인덱스

    while True:
        pc = (pl + pr) // 2 # 중앙 원소의 인덱스
        if a[pc] == key: # 검색 성공
            return pc
        elif a[pc] < key: 
            pl = pc + 1 # 검색 범위를 뒤쪽 절반으로 좁힘
        else:
            pr = pc - 1 # 검색 범위를 앞쪽 절반으로 좁힘
        
        if pl > pr:
            break
        return -1 # 검색 실패
    
if __name__ == '__main__':

    num = int(input('원소 수를 입력하세요.: '))
    x = [None] * num

    print('배열 데이터를 오름차순으로 입력하세요.')

    x[0] = int(input('x[0]: '))

    for i in range(1, num):
        while True:
            x[i] = int(input(f'x[{i}]: '))
            if x[i] >= x[i-1]:
                break
    
    k = int(input('검색할 값을 입력하세요.: '))

    idx = binary_search(x, k)

    if idx == -1:
        print('검색값을 갖는 원소가 존재하지 않습니다.')
    else:
        print(f'검색값은 a[{idx}]에 존재합니다.')

        
