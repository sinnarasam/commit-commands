def add(a, b):
    """두 숫자를 더하는 함수"""
    return a + b


if __name__ == "__main__":
    while True:
        try:
            num1 = float(input("첫 번째 숫자를 입력하세요: "))
            num2 = float(input("두 번째 숫자를 입력하세요: "))
            result = add(num1, num2)
            print(f"\n결과: {num1} + {num2} = {result}\n")

            while True:
                choice = input("다시 계산하려면 '재시작'을 입력하세요. 종료하려면 'q'를 입력하세요: ").strip()
                if choice == "재시작":
                    break
                elif choice == "q":
                    print("프로그램을 종료합니다.")
                    exit()
                else:
                    print("'재시작' 또는 'q'를 입력해주세요.")
        except ValueError:
            print("오류: 숫자를 입력해주세요.\n")
