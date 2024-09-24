from Component import Component

class Componentable:
    __components: list[Component]
    def __init__(self) -> None:
        self.__components = []

    def add_component(self, component: Component):
        self.__components.append(component)
        component.get_component = lambda type: self.get_component(type)
        
    def get_component(self, component_type: Component) -> Component:
        for component in self.__components:
            if type(component) == component_type:
                return component
            
    def get_components(self) -> list[Component]:
        return self.__components.copy()