import functools
from collections.abc import Callable
import time
from typing import Any


def spell_timer(func: Callable) -> Callable:
    @functools.wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        print(f"Casting {func.__name__}...")
        start = time.perf_counter()
        result = func(*args, **kwargs)
        time.sleep(1.3)
        elapsed = time.perf_counter() - start
        print(f"Spell completed in {elapsed:.3f} seconds")
        return result
    return wrapper


@spell_timer
def fireball(target: str, power: int) -> str:
    return f"Hit {target} with a fireball of power {power}"


def power_validator(min_power: int) -> Callable:
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            power = kwargs.get('power')
            if power is None:
                return "power keyword argument is not passed"
            if power < min_power:
                return "Insufficient power for this spell"
            return (func(*args, **kwargs))
        return wrapper
    return decorator


@power_validator(35)
def heal(target: str, power: int) -> str:
    return f"Heal restores {target} for {power} HP"


def retry_spell(max_attempts: int) -> Callable:
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            for i in range(max_attempts):
                try:
                    x = func(*args, **kwargs)
                    print(f"congrat, your function passed at {i + 1} attempts")
                    return (x)
                except Exception:
                    if i != max_attempts - 1:
                        print(f"Spell failed, retrying... "
                              f"(attempt {i + 1}/{max_attempts})")
                        time.sleep(1.2)
                    else:
                        print(f"Spell casting failed "
                              f"after {max_attempts} attempts")
                        print("Waaaaaaagh spelled !")
                        return (f"Spell casting failed "
                                f"after {max_attempts} attempts")
        return wrapper
    return decorator


class MageGuild:
    @staticmethod
    def validate_mage_name(name: str) -> bool:
        if not isinstance(name, str):
            return False
        return (
            len(name.replace(" ", "")) >= 3 and
            all(c.isalpha() or c.isspace() for c in name)
        )

    @power_validator(10)
    def cast_spell(self, spell_name: str, power: int) -> str:
        return f"Successfully cast {spell_name} with {power} power"


def main() -> None:
    print("Testing spell timer...")
    print("Result: " + fireball("Ali", 3))
    print()

    print("Testing power validator...")
    print(f"power: 30 < 35: {heal('Ali', power=30)}")
    print(f"power: 80 >= 35: {heal('Ali', power=80)}")
    print()

    print("Testing retrying spell...")

    x = 0

    @retry_spell(3)
    def test_retry_1() -> str:
        nonlocal x
        x += 1
        if x < 4:
            raise Exception()
        return "Success"

    print(f"result = {test_retry_1()}")
    print()

    x = 0

    @retry_spell(8)
    def test_retry_2() -> str:
        nonlocal x
        x += 1
        if x < 5:
            raise Exception()
        return "Success"

    print(f"result = {test_retry_2()}")
    print()

    print("Testing MageGuild...")
    mg = MageGuild()
    print(mg.validate_mage_name("ab c"))
    print(mg.validate_mage_name("b    c"))
    print(mg.cast_spell("fireball", power=15))
    print(mg.cast_spell("fireball", power=5))


if __name__ == "__main__":
    main()
