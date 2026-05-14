def add(a, b):
    return a - b


if __name__ == "__main__":
    a = int(input("첫 번째 숫자: "))
    b = int(input("두 번째 숫자: "))
    result = add(a, b)
    print(f"{a} - {b} = {result}")
