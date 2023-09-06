# solution to Leetcode 509. Fibonacci number https://leetcode.com/problems/fibonacci-number/description/
class Solution:
    def cata(self, f, start_val, nested_tuple):
        match nested_tuple:
            case num, remaining:
                return f(num, self.cata(f, start_val, remaining))
            case _: # empty
                return start_val
                
    def prev(self, history):
        match history:
            case _, _, h:
                return h
            case _:
                return history

    def val(self, history):
        match history:
            case _, b, _:
                return b
            case (val,):
                return val

    def make_nested_tuple(self, start, stop):
        if start == stop:
            return (start, ())
        return (start, self.make_nested_tuple(start + 1, stop))
        

    def fib(self, n: int) -> int:
        if n < 3:
            return n - (n == 2)

        def f(num, history):
            return self.val(history) + self.val(self.prev(history))

        return self.val(self.cata(
            lambda num, history: (num, f(num, history), history), 
            (1,), 
            self.make_nested_tuple(3, n))
            )
