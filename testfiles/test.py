def b(n: int):
    if n == 0:
        return
    return b(n-1)

def c(nums: List[int]) -> int:
    return 0

def a(param1: int, param2: List[int]) -> bool:
    b(param1)
    c(param2)
    return True
