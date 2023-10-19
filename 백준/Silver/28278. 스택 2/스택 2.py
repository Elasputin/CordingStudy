import sys
input = sys.stdin.readline
N = int(input())
stack = []

for _ in range(N):
    command = input().rstrip()
    # 1. push
    if len(command) > 2:  ## 여기 코드를 고쳐야한다.
        num = int(command[2:])
        stack.append(num)
    # 2. pop
    elif command == "2":
        print(stack.pop() if stack else -1)
    # 3. size
    elif command == "3":
        print(len(stack))
    # 4. empty
    elif command == "4":
        print(1 if not stack else 0)
    # 5. top
    elif command == "5":
        print(stack[-1] if stack else -1)


