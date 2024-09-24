from typing import Any, Callable, Self
from types import LambdaType
import inspect

class DoesntReturnNone(Exception):
    pass
class NotImplementedType(Exception):
    pass
class HasNoParameterAnnotation(Exception):
    pass

class Action(Callable):
    __callable_object: Callable
    def __init__(self, callable_object: Callable) -> None:
        if isinstance(callable_object,Action):
            action: Action = callable_object
            self.__callable_object = action.__callable_object
            return
        try:
            signature: inspect.Signature = inspect.signature(callable_object)
        except:
            raise NotImplementedType("The direct conversion of type " + str(callable_object.__class__.__name__) + " to Action is not implemented")
        if callable_object.__name__ == "<lambda>":
            self.__callable_object = callable_object
            return
        if not self.__is_signature_with_annotation(signature):
            raise HasNoParameterAnnotation("A callable_object has no parameter annatation")
        if not self.__is_signature_with_None_return(signature):
            raise DoesntReturnNone("A callable_object has no a None type return")
        self.__callable_object = callable_object
        return

    def __call__(self, *args):
        self.__callable_object(*args)

    def __eq__(self, other: object):
        if not isinstance(other, Action):
            raise NotImplementedType("The equal comporation is not imlemented of class " + str(other.__class__.__name__) + " and " + Action.__class__.__name__)
        else:
            other_action: Action = other
            return other_action.__callable_object == self.__callable_object

    @property
    def signature(self) -> inspect.Signature:
        return inspect.signature(self.__callable_object)
    
    @property
    def is_lambda(self) -> bool:
        return self.__callable_object.__name__ == "<lambda>"
    
    def __is_signature_with_annotation(self, signature: inspect.Signature) -> bool:
        parameters: list[inspect.Parameter] = list(signature.parameters.values())
        for i in range(len(parameters)):
            if parameters[i].annotation == inspect._empty:
                return False
        return True
    
    def __is_signature_with_None_return(self, signature: inspect.Signature) -> bool:
        if signature.return_annotation != None:
            return False
        return True


if __name__ == "__main__":
    def divide_test(func: Callable):
        def wrapper(test_number: int):
            func(test_number)
            print("_"*10)
        wrapper.__name__ = func.__name__
        return wrapper

    @divide_test
    def successful_no_parameter_test(test_number: int):
        def f()->None:
            print("Successful test", test_number)
        a1: Action = Action(f)
        a1()
    
    @divide_test
    def successful_parameter_test(test_number: int):
        def f(test_number: int)->None:
            print("Successful test", test_number)
        a1: Action = Action(f)
        a1(test_number)
    
    @divide_test
    def failure_parameter_test_no_None_return_type_annotation(test_number: int):
        def f(test_number: int):
            print("Successful test", test_number)
        a1: Action = Action(f)
        a1(test_number)
        
    @divide_test
    def failure_parameter_test_no_parameter_annotation(test_number: int):
        def f(test_number) -> None:
            print("Successful test", test_number)
        a1: Action = Action(f)
        a1(test_number)
    
    @divide_test
    def failure_parameter_test_no_signature_type(test_number: int):
        f = 5
        a1: Action = Action(f)
        a1(test_number)

    @divide_test
    def successful_lambda_test(test_number: int):
        f = lambda x: print("Successful test", x)
        a1: Action = Action(f)
        a1(test_number)
    
    @divide_test
    def successful_using_list_test(test_number: int):
        def f1(test_number: int) -> None:
            print("Successful test", test_number, 1)
        def f2(test_number: int) -> None:
            print("Successful test", test_number, 2)
        def f3(test_number: int) -> None:
            print("Successful test", test_number, 3)
        l: list[Action] = [Action(f1),Action(f2),Action(f3)]
        l.remove(Action(f2))
        for action in l:
            action(test_number)
        
    @divide_test
    def failure_using_list_test(test_number: int):
        def f1(test_number: int) -> None:
            print("Successful test", test_number, 1)
        def f2(test_number: int) -> None:
            print("Successful test", test_number, 2)
        def f3(test_number: int) -> None:
            print("Successful test", test_number, 3)
        l: list[Action] = [Action(f1),f2,Action(f3)]
        l.remove(Action(f2))
        for action in l:
            action(test_number)

    tests = [
        successful_no_parameter_test,
        successful_parameter_test,
        failure_parameter_test_no_None_return_type_annotation,
        failure_parameter_test_no_parameter_annotation,
        failure_parameter_test_no_signature_type,
        successful_using_list_test,
        failure_using_list_test,
        successful_lambda_test
    ]

    for test_number in range(len(tests)):
        try:
            tests[test_number](test_number + 1)
        except Exception as e:
            divide_test(lambda test_number:print("At test", test_number + 1, "got exception with follow text:\n", e))(test_number)