from collections.abc import Callable
from typing import Any


def mage_counter() -> Callable:
    count = 0

    def counter() -> int:
        nonlocal count
        count += 1
        return count
    return counter


def spell_accumulator(initial_power: int) -> Callable:
    def accumulator(add: int) -> int:
        nonlocal initial_power
        initial_power += add
        return initial_power
    return accumulator


def enchantment_factory(enchantment_type: str) -> Callable:
    def inner(item_name: str) -> str:
        return f"{enchantment_type} {item_name}"
    return inner


def memory_vault() -> dict[str, Callable]:
    memory = {}

    def store(key: str, value: Any) -> None:
        memory[key] = value

    def recall(key: str) -> Any:
        return memory.get(key, "Memory not found")

    return {"store": store, "recall": recall}


if __name__ == "__main__":
    print("Testing mage counter...")
    c_a = mage_counter()
    c_b = mage_counter()
    for i in range(2):
        print(f"counter_a call {i + 1}: {c_a()}")
    for i in range(1):
        print(f"counter_b call {i + 1}: {c_b()}")
    print()

    print("Testing spell accumalator...")
    acc = spell_accumulator(100)
    print(f"Base 100, add 20: {acc(20)}")
    print(f"Base 100, add 30: {acc(30)}")
    print()

    print("Testing enchantment factory...")
    enchant_flame = enchantment_factory("flame")
    print(enchant_flame("sword"))
    enchant_looting = enchantment_factory("looting")
    print(enchant_looting("axe"))
    print()

    print("Testing memory vault...")
    dct = memory_vault()
    store = dct["store"]
    recall = dct["recall"]
    print("Store 'secret' = 42")
    store('secret', 42)
    print(f"Recall 'secret': {recall('secret')}")
    print(f"Recall 'unknown': {recall('unknown')}")
