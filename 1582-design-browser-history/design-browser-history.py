class Node:
    def __init__(self, prev=None, next=None, val=0):
        self.prev = prev
        self.next = next
        self.val = val


class BrowserHistory:
    def __init__(self, homepage: str):
        new_node = Node(val=homepage)
        self.head = new_node
        self.curr = new_node

    def visit(self, url: str) -> None:
        new_node = Node(val=url)
        new_node.prev = self.curr
        self.curr.next = new_node
        self.curr = new_node

    def back(self, steps: int) -> str:
        while steps > 0 and self.curr.prev is not None:
            steps -= 1
            self.curr = self.curr.prev
        return self.curr.val

    def forward(self, steps: int) -> str:
        while steps > 0 and self.curr.next is not None:
            steps -= 1
            self.curr = self.curr.next
        return self.curr.val

# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)