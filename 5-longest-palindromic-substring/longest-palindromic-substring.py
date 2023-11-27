class Solution:
    def longestPalindrome(self, s: str) -> str:
        # 만약 팰린드롬이라면 확장, 아니면 스킵
        def expand(left: int, right: int) -> str:
            # left >= 0 and right <= len(s) idx 범위 조건
            # s[left] == s[right -1] 실제 조건 = 팰린드롬인가?
            while left >= 0 and right <= len(s) and s[left] == s[right - 1]:
                left, right = left - 1, right + 1
            return s[left + 1:right - 1]

        # skip 가능하면 skip
        if len(s) < 0 or s == s[::-1]:
            return s

        # 슬라이딩 윈도우처럼 한칸씩 넘어감
        result = ''
        for i in range(len(s) - 1):
            result = max(result,
                        expand(i, i+1),
                        expand(i, i+2),
                        key=len) # max를 결정하는 기준(key)이 길이(len())

        return result

# 팰린드롬 풀이
# 투 포인트 사용 - 2개, 3개 범위의 문자열을 읽는 포인터 2개
# 슬라이딩 윈도우처럼 왼 -> 오 로 이동 - 1
# 투 포인터 중 하나에서 catch 시 좌우 사이즈를 늘려가면서 확인 - 2
