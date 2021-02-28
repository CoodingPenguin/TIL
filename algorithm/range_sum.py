# title: 연속적으로 나열된 N개의 수가 있을 때, 특정 구간의 모든 수를 합한 값을 구하는 문제 (= 구간 합)
# src: 이것이 취업을 위한 코딩테스트다 p.481
# time: O(NM) (N=요소수, M=쿼리수)

N = 5                       # arr의 길이
arr = [10, 20, 30, 40, 50]  # 정렬된 리스트
prefix_sum = [0]            # 0부터 i까지의 구간합을 저장하는 리스트
for i in range(N):
    prefix_sum.append(prefix_sum[-1]+arr[i])

# 예시 쿼리
l1, r1 = 3, 4
l2, r2 = 1, 5
l3, r3 = 2, 4

print(f"{l1} ~ {r1} 까지의 구간합:", prefix_sum[r1]-prefix_sum[l1-1])
print(f"{l2} ~ {r2} 까지의 구간합:", prefix_sum[r2]-prefix_sum[l2-1])
print(f"{l3} ~ {r3} 까지의 구간합:", prefix_sum[r3]-prefix_sum[l3-1])
