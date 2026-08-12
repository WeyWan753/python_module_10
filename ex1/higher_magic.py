from collections.abc import Callable


def heal(target: str, power: int) -> str:
    return f"Heal restores {target} for {power} HP"


def fireball(target: str, power: int) -> str:
    return f"Hit {target} with a fireball of power {power}"


def spell_combiner(spell1: Callable, spell2: Callable) -> Callable:
    return lambda target, power: (spell1(target, power), spell2(target, power))


def power_amplifier(base_spell: Callable, multiplier: int) -> Callable:
    return lambda target, power: base_spell(target, power * multiplier)


def conditional_caster(condition: Callable, spell: Callable) -> Callable:
    return (
        lambda target, power: spell(target, power)
        if condition(target, power)
        else "Spell fizzled"
    )


if __name__ == "__main__":
    combined = spell_combiner(heal, fireball)
    print(combined("Ali", 2))

    amplified = power_amplifier(fireball, 3)
    print(amplified("Ali", 2))

    condition = lambda target, power: True if target == "Ali" and power == 2 else False
    conditional = conditional_caster(condition, fireball)
    print(conditional("Ali", 3))
