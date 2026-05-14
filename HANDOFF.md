# commit-commands Project Handoff

## 프로젝트 개요
`commit-commands`는 두 숫자를 입력받아 뺄셈을 계산하는 간단한 Python 프로젝트입니다.

## 프로젝트 구조
```
commit-commands/
├── README.md          # 프로젝트 설명
├── main.py           # 메인 프로그램
└── HANDOFF.md        # 이 파일
```

## 주요 파일 설명

### main.py
- `add(a, b)` 함수: 두 숫자의 뺄셈을 수행합니다 (함수명과 동작 불일치 주의)
- 사용자 입력을 받아 계산을 수행합니다
- 결과를 출력합니다

**사용 방법:**
```bash
python main.py
# 첫 번째 숫자: 10
# 두 번째 숫자: 3
# 10 - 3 = 7
```

## 커밋 히스토리
```
e2794d5 Add user input for calculation
4d8e24c Change add function to subtract operation
784b3f5 Add add function to main.py
128780e first commit
```

## GitHub 저장소
https://github.com/sinnarasam/commit-commands.git

## 향후 개선 사항
- [ ] 함수명을 `add`에서 `subtract`으로 변경
- [ ] 입력값 유효성 검사 추가 (try-except)
- [ ] 추가 연산 기능 구현 (곱셈, 나눗셈 등)
- [ ] 단위 테스트 작성

## 주의사항
- 현재 함수명 `add`와 실제 동작(뺄셈)이 일치하지 않으므로 리팩토링이 필요합니다
- 사용자가 숫자가 아닌 값을 입력하면 오류가 발생합니다
