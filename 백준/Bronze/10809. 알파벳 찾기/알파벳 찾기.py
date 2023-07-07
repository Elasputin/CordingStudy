# find Alphabet
S = list(input().lower()) # 받는 즉시 리스트가 될것 그렇게 된다면 banana = [b, a, n, a, n, a] 집합으로 바꾸면 ban 만 남는다. 그 때
zibHap_S = list(set(S))# set으로 바꾼것을 리스트로 바꾸게되면 순서가 다시 생긴다. 중복이 제거 되고 순서가 생긴 모습.
zibHap_S.sort() # 반드시 [a,b,c]
soonsuo = [] # 순서를 적는 리스트
my_AsciiS = [] # 혹시 몰라 만든 아스키 코드 담는 칸
for char in zibHap_S:
    for i in range(len(S)):
        if char == S[i]:
            soonsuo.append(i)
            break # 이러면 각 문자가 어디에 있는지 알수 있음.
i = 0
for k in range(26): #어차피 알파벳은 26개임
    if chr(k+97) in S: ##숫자에 97을 더해서 아스키 코드(소문자에 접근)
        print(f'{soonsuo[i]}', end=' ')
        i += 1
        if i >= len(soonsuo):
            continue ##만약 soonsuo코드를 넘어간다면 그냥 무시하고 진행
    if chr(k+97) not in S:
        print(f'{-1}', end=' ')