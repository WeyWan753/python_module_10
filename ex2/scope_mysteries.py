from collections.abc import Callable


def mage_counter() -> Callable:
    count = 0
    def counter() -> int:
        nonlocal count
        count += 1
        return count
    return counter


def spell_accumulator(initial_power: int) -> Callable:
    def accumulator() -> int:
        nonlocal initial_power
        initial_power += 10
        return initial_power
    return accumulator


def enchantment_factory(enchantment_type: str) -> Callable:
    def inner(item_name: str) -> str:
        return f"{enchantment_type} {item_name}"
    return inner


def memory_vault() -> dict[str, Callable]:
    memory = {}
    def store(key, value) -> None:
        #nonlocal memory
        memory[key] = value

    def recall(key):
        #nonlocal memory
        return memory.get(key, "Memory not found")

    return{1: store, 2: recall}



if __name__ == "__main__":
    c = mage_counter()
    print(c())
    print(c())
    print(c())

    acc = spell_accumulator(20)
    print(acc())
    print(acc())
    print(acc())

    enchant_flame = enchantment_factory("flame")
    print(enchant_flame("sword"))

    enchant_looting = enchantment_factory("looting")
    print(enchant_looting("axe"))

    dct = memory_vault()
    store = dct[1]
    recall = dct[2]

    store("123","hello")
    print(recall("1233"))
