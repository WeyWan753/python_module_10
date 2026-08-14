from collections.abc import Callable


def heal(target: str, power: int) -> str:
    return f"Heal restores {target} for {power} HP"


def fireball(target: str, power: int) -> str:
    return f"Hit {target} with a fireball of power {power}"


def spell_combiner(spell1: Callable, spell2: Callable) -> Callable:
    return lambda target, power: (spell1(target, power), spell2(target, power))


def power_amplifier(base_spell: Callable, multiplier: int) -> Callable:
    return (
        lambda target, power: f"original: {power}, amplified: " +
        base_spell(target, power * multiplier)
    )


def conditional_caster(condition: Callable, spell: Callable) -> Callable:
    return (
        lambda target, power: "Condition satisfied: " + spell(target, power)
        if condition(target, power)
        else "Conditions not met: Spell fizzled"
    )


def spell_sequence(spells: list[Callable]) -> Callable:
    return (
        lambda target, power:
        [spell(target, power) for spell in spells]
    )


if __name__ == "__main__":
    print("Testing spell combiner...")
    combined = spell_combiner(heal, fireball)
    print(", ".join([x for x in combined("Ali", 2)]))
    print()

    print("Testing power amplifier...")
    amplified = power_amplifier(fireball, 3)
    print(amplified("Ali", 2))
    print()

    print("Testing conditional caster...")
    conditional_t = conditional_caster(lambda target, power: True, fireball)
    conditional_f = conditional_caster(lambda target, power: False, fireball)
    print("Condition: True")
    print(conditional_t("Ali", 4))
    print("condition: False")
    print(conditional_f("Ali", 4))
    print()

    print("Testing spell sequence...")
    sequence = spell_sequence([heal, fireball])
    result = sequence("Ali", 4)
    print(", ".join([f"{i + 1}) {result[i]}" for i in range(len(result))]))
