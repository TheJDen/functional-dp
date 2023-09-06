# solution to Leetcode 509. Fibonacci number https://leetcode.com/problems/fibonacci-number/description/
def val(history):
    match history:
        case b, _:
            return b
        case (val,):
            return val

def prev(history):
    match history:
        case _, h:
            return h
        case _:
            return history

def make_nested_tuple(start, stop):
    if start == stop:
        return (start, ())
    return (start, make_nested_tuple(start + 1, stop))

# nested_tuple-specific catamorphism (fold)
def cata(f, start_val, nested_tuple):
    match nested_tuple:
        case (): # empty
            return start_val
        case num, remaining:
            return f(num, cata(f, start_val, remaining))

class Solution:
                
    def f(self, num, history):
        return val(history) + val(prev(history))

    def fib(self, n: int) -> int:
        if n < 2:
            return n

        return val(cata(
            lambda num, history: (self.f(num, history), history), 
            (1, (0,)), 
            make_nested_tuple(0, n - 2))
            )
