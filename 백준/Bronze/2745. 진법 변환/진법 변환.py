N, B = input().split()
N = ''.join(reversed(N)) #N을 거꾸로 입력해서 조인하여 문자열로 바꾸기
B = int(B) # B를 int로 변환

number = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
result = 0
for i in range(len(N)-1, -1 , -1): # 시작 위치 입력받은 숫자의 길이-1 부터 0까지 줄어가면서
    result += number.index(N[i]) * (B**i)
print(result)
