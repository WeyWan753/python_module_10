import functools


def spell_timer(func: Callable) -> Callable:
    @functools.wraps(func)
    def wrapper():
        print("Casting function_name...")
        x = func()
        print("Spell completed in 2.123 seconds")
        return x
    return wrapper


@spell_timer
def test():
    """this is doc string for test"""
    return f"doing the thing"


def power_validator(min_power: int) -> Callable:
    pass



if __name__ == "__main__":
    print(test())

