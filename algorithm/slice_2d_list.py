# title: 2차원 리스트 슬라이싱
# src: https://programming119.tistory.com/169

arr = [
	[1, 1, 0, 0, 0, 0, 1, 1],
	[1, 1, 0, 0, 0, 0, 1, 1],
	[0, 0, 0, 0, 1, 1, 0, 0],
	[0, 0, 0, 0, 1, 1, 0, 0],
	[1, 0, 0, 0, 1, 1, 1, 1],
	[0, 1, 0 ,0, 1, 1, 1, 1],
	[0, 0, 1, 1, 1, 1, 1, 1],
	[0, 0, 1, 1, 1, 1, 1, 1]
]

# 4*4의 서브배열 추출
sub_arr1 = [row[0:4] for row in arr[0:4]]
sub_arr2 = [row[4:8] for row in arr[0:4]]
sub_arr3 = [row[0:4] for row in arr[4:8]]
sub_arr4 = [row[4:8] for row in arr[4:8]]