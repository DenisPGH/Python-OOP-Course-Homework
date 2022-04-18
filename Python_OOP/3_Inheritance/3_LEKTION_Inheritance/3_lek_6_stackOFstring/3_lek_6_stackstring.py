""" Create a class Stack that can store only strings and has the following functionality:
•	Instance attribute: data: list
•	Method: push(element) – adds an element at the end of the stack
•	Method: pop() – removes and returns the last element in the stack
•	Method: top() - returns a reference to the topmost element of the stack
•	Method: is_empty() - returns boolean True/False
•	Override the string method to return the stack data in the format:
"[{element(N)}, {element(N-1)} ... {element(0)}]"
"""

class Stack():
    def __init__(self):
        self.data=[]

    def push(self,element):
        self.data.append(element)

    def pop(self):
        if self.data:
            return self.data.pop()


    def top(self):
        if self.data:
            return self.data[0]

    # is_empty() - returns boolean True/False
    def is_empty(self):
        if self.data :
            return False
        else:
            return True

    # [{element(N)}, {element(N-1)} ... {element(0)}]"
    def __str__(self):
        result_list=self.data.copy()
        result="["
        while result_list:
            if len(result_list)>1:
                result+= f"{result_list.pop()}, "
            else:
                result += f"{result_list.pop()}"

        result+="]"
        return result


# stack=Stack()
# print(stack.push("apple"))
# print(stack.push("carrot"))
# print(stack)
# print(stack.pop()) # carrot
# print(stack.top()) # apple



