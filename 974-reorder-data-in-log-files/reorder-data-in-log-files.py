class Solution:
    def reorderLogFiles(self, logs: list[str]) -> list[str]:
        letters, dights = [], []
        for log in logs:
            if log.split()[1].isalpha():
                letters.append(log)
            else:
                dights.append(log)
        letters.sort(key=lambda x: (x.split()[1:], x.split()[0]))
        
        return letters + dights

# 앞의 dig{n}, let{n} 같은건 식별자
# 1. 문자 로그가 모든 숫자 로그보다 먼저
# 2. 문자 로그 내용 순으로 정렬, 문자가 같으면 식별자 순
# 3. 숫자 로그는 입력 순서대로