import functools
import operator
from collections.abc import Callable
from typing import Any


def spell_reducer(spells: list[int], operation: str) -> int:
    if len(spells) == 0:
        return 0
    allowed_operations: dict[str, Callable] = {
        'add': operator.add,
        'multiply': operator.mul,
        'max': max,
        'min': min
    }
    if allowed_operations.get(operation) is None:
        print("no such operation")
        return 0
    return functools.reduce(allowed_operations[operation], spells)


def partial_enchanter(base_enchantment: Callable) -> dict[str, Callable]:
    return {
        'fire_enchant': functools.partial(base_enchantment,
                                          power=50,
                                          element="fire"),
        'ice_enchant': functools.partial(base_enchantment,
                                         power=50,
                                         element="ice"),
        'looting_enchant': functools.partial(base_enchantment,
                                             power=50,
                                             element="looting")
    }


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
        return f"Unknown spell type {type(spell)}"

    @process.register
    def _(spell: int) -> str:
        return f"Damage spell: {spell} damage"

    @process.register
    def _(spell: str) -> str:
        return f"Enchantment: {spell}"

    @process.register
    def _(spells: list) -> str:
        return f"Multi-cast: {len(spells)} spells"

    return process


if __name__ == "__main__":
    print("Testing spell reducer...")
    x = [26, 44, 39, 10, 19, 14]
    print(f"Sum: {spell_reducer(x, 'add')}")
    print(f"Product: {spell_reducer(x, 'multiply')}")
    print(f"Max: {spell_reducer(x, 'max')}")
    print()

    print("Testing partial enchanter...")
    dct = partial_enchanter(base_enchantment)
    fire_enchant = dct["fire_enchant"]
    ice_enchant = dct["ice_enchant"]
    looting_enchant = dct["looting_enchant"]
    print(fire_enchant(target="pickaxe"))
    print(ice_enchant(target="sword"))
    print(looting_enchant(target="axe"))
    print()

    print("Testing memoized fibonacci...")
    print(f"Fib(0): {memoized_fibonacci(0)}")
    print(f"Fib(1): {memoized_fibonacci(1)}")
    print(f"Fib(10): {memoized_fibonacci(10)}")
    print(f"Fib(15): {memoized_fibonacci(15)}")
    print(memoized_fibonacci.cache_info())
    print()

    print("Testing spell dispatcher...")
    dispatcher = spell_dispatcher()
    print(dispatcher(42))
    print(dispatcher('fireball'))
    print(dispatcher(()))
