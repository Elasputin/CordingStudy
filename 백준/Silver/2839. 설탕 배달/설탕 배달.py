sugar = int(input())
su3 = 0  # 3kg 봉지
while sugar >= 0:
    if sugar % 5 == 0:
        print(sugar // 5 + su3)
        break #while문조건 전에 탈출
    else:
        sugar -= 3
        su3 += 1
if sugar < 0:
    print(-1)
