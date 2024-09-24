from __future__ import annotations
from typing import Callable, Type

class Component:
    def on_enable(self) -> None:
        pass

    def start(self) -> None:
        pass

    def update(self) -> None:
        pass

    get_component: Callable[[Type], Component] = None