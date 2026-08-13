import functools
import operator
from collections.abc import Callable
from typing import Any


def spell_reducer(spells: list[int], operation: str) -> int:
    if len(spells) == 0:
        return 0
    allowed_operations = ["add", "multiply", "max", "min"]
    if operation not in allowed_operations:
        print("no such operation")
        return 0

    if operation == "add":
        return functools.reduce(operator.add, spells)

    elif operation == "multiply":
        return functools.reduce(operator.mul, spells)

    elif operation == "max":
        return functools.reduce(operator.max, spells)

    elif operation == "min":
        return functools.reduce(operation.min, spells)


def partial_enchanter(base_enchantment: Callable) -> dict[str, Callable]:
    return {'fire_enchant': functools.partial((base_enchantment), power=50, element="fire"), 'ice_enchant': functools.partial((base_enchantment), power=50, element    ="ice"), 'looting_enchant': functools.partial((base_enchantment), power=50, element    ="looting")}

def base_enchantment(power: int, element: str, target: str) -> str:
    return f"enchanted {target} with {element} enchantment of power {power}"


@functools.lru_cache(maxsize=None)
def memoized_fibonacci(n: int) -> int:
    if n == 0 or n == 1:
        return n
    return memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)


def spell_dispatcher() -> Callable[[Any], str]:
    @functools.singledispatch
    def process(spell: Any) -> str:
        return f"Default {spell}"

    @process.register
    def _(spell: int) -> str:
        return f"does {spell} damage"

    @process.register
    def _(spell: str) -> str:
        return f"{spell} enchant"

    @process.register
    def _(spells: list) -> str:
        return ",".join([process(spell) for spell in spells])

    return process



if __name__ == "__main__":
    print(spell_reducer([1, 2, 3, 4, 5], "a"))
    dct = partial_enchanter(base_enchantment)
    fire_enchant = dct["fire_enchant"]
    ice_enchant = dct["ice_enchant"]
    looting_enchant = dct["looting_enchant"]
    print(fire_enchant(target = "pickaxe"))
    print(memoized_fibonacci(900))
    print(memoized_fibonacci.cache_info())

    dispatcher = spell_dispatcher()
    print(dispatcher(3))
