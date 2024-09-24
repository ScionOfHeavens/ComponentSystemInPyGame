from typing import Any, Callable, Self
import inspect

from Action import Action

class Event:
    __actions: list[Action]
    __args_types: list[type]
    def __init__(self, *args_types: list[type]) -> None:
        self.__actions = []
        self.__args_types = args_types
        
    def __call__(self, *args: Any) -> None:
        for action in self.__actions:
            action(*args)

    def __has_listener(self, action: Callable|Action):
        return self.__actions.count(action) != 0
    
    def add_listener(self, action: Callable|Action) -> None:
        if not isinstance(action, Action):
            action = Action(action)
        if action.is_lambda and self.__is_same_param_amount(action):
            self.__actions.append(action) 
            return
        if self.__is_action_in_same_sig(action):
            self.__actions.append(action)
            return
        raise Exception("Not same signature of action")

    def remove_listener(self, action: Callable|Action) -> None:
        if not isinstance(action, Action):
            action = Action(action)
        if self.__has_listener(action):
            self.__actions.remove(action)
        else:
            raise Exception("No such action") 

    def __iadd__(self, action: Callable|Action) -> Self:
        self.add_listener(action)
        return self
    def __isub__(self, action: Callable|Action) -> Self:
        self.remove_listener(action)
        return self
    
    def __is_same_param_amount(self, action: Action) -> bool:
        parameters: list[inspect.Parameter] = list(action.signature.parameters.values())
        if len(parameters) != len(self.__args_types):
            return False
        return True
    
    def __is_action_in_same_sig(self, action: Action) -> bool:
        if not self.__is_same_param_amount(action):
            return False
        parameters: list[inspect.Parameter] = list(action.signature.parameters.values())
        for i in range(len(parameters)):
            if parameters[i].annotation != self.__args_types[i]:
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
    def successful_test(test_number: int):
        def f(test_number: int) -> None:
            print("Successful test", test_number, 1)
        def g(test_number: int) -> None:
            print("Successful test", test_number, 2)
        h = lambda test_number: print("Successful test", test_number, 3)
        a1 = Action(f)
        a2 = Action(a1)
        e = Event(int)
        e += a1
        e += a2
        e += Action(g)
        e += h
        e -= Action(f)
        e -= h
        e(test_number)

    @divide_test
    def failure_test_with_other_signature(test_number: int):
        def f(test_number: str) -> None:
            print("Successful test", test_number, 1)
        def g(test_number: int) -> None:
            print("Successful test", test_number, 2)
        h = lambda test_number: print("Successful test", test_number, 2)
        a1 = Action(f)
        a2 = Action(a1)
        e = Event(int)
        e += a1
        e += a2
        e += Action(g)
        e += h
        e -= Action(f)
        e(test_number)
    
    @divide_test
    def failure_test_remove_not_existed_action(test_number: int):
        def f(test_number: int) -> None:
            print("Successful test", test_number, 1)
        def g(test_number: int) -> None:
            print("Successful test", test_number, 2)
        h = lambda test_number: print("Successful test", test_number, 2)
        a1 = Action(f)
        a2 = Action(a1)
        e = Event(int)
        e += a1
        e += a2
        e += Action(g)
        e -= h
        e(test_number)

    tests =[
        successful_test,
        failure_test_with_other_signature,
        failure_test_remove_not_existed_action
    ]
    
    for test_number in range(len(tests)):
        try:
            tests[test_number](test_number + 1)
        except Exception as e:
            divide_test(lambda test_number:print("At test", test_number + 1, "got exception with follow text:\n", e))(test_number)

    