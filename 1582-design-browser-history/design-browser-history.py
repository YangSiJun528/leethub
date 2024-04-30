class BrowserHistory:

    def __init__(self, homepage: str):
        self.arr = [homepage] + [''] * 5000
        self.cur_pointer = 0
        self.max_pointer = 0

    def visit(self, url: str) -> None:
        self.cur_pointer += 1
        self.max_pointer = self.cur_pointer
        self.arr[self.cur_pointer] = url

    def back(self, steps: int) -> str:
        self.cur_pointer = max((self.cur_pointer - steps), 0)
        return self.arr[self.cur_pointer]
        
    def forward(self, steps: int) -> str:
        self.cur_pointer = min((self.cur_pointer + steps), self.max_pointer)
        return self.arr[self.cur_pointer]
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)