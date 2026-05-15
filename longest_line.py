def find_longest_line_length(filename):
    """파일에서 가장 긴 줄의 길이를 반환합니다"""
    max_length = 0

    try:
        with open(filename, 'r', encoding='utf-8') as file:
            for line in file:
                line_length = len(line.rstrip('\n'))
                max_length = max(max_length, line_length)
    except FileNotFoundError:
        print(f"오류: '{filename}' 파일을 찾을 수 없습니다")
        return -1
    except Exception as e:
        print(f"오류: {e}")
        return -1

    return max_length


if __name__ == "__main__":
    result = find_longest_line_length("add_numbers.py")
    print(f"가장 긴 줄의 길이: {result}")

    result2 = find_longest_line_length("longest_line.py")
    print(f"이 파일의 가장 긴 줄의 길이: {result2}")
