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
        nonlocal memory
        memory[key] = value

    def recall(key):
        nonlocal memory
        return memory[key]

    store(1, store)
    store(2, recall)
    return(memory)



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

    memory = memory_vault()
    print(memory)
    memory[1](3, "naa")
    print(memory)
