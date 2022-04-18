"""Create a class called store_results. It should be used as a decorator and store information
 about the executed functions in a file called results.txt in the
  format: "Function {func_name} was add called. Result: {func_result}"""
import functools


class store_results:
    def __init__(self,funk):
        self.funk = funk
        functools.update_wrapper(self,funk) # not neccerery!!!!!!!!

    def __call__(self,*args):
        res=f"Function '{self.funk.__name__}' was called. Result: {self.funk(*args)}\n"
        print(f"Function '{self.funk.__name__}' was called. Result: {self.funk(*args)}")
        with open("result.txt","a") as result:
            result.write(res)





@store_results
def add(a, b):
    return a + b

@store_results
def mult(a, b):
    return a * b

add(2, 2)
mult(6, 4)
