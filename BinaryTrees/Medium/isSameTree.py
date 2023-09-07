def my_solution(self, p, q) -> bool:
    if not p and not q:
        return True
    elif not p or not q:
        return False

    return p.val == q.val and (self.my_solution(p.left, q.left)) and (self.my_solution(p.right, q.right))
