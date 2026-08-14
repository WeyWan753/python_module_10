import functools


def power_validator(min_power: int) -> Callable:
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            power = args[1]
            if power < min_power:
                return f"insufficient power for this spell"
            return(func(*args, **kwargs))
        return wrapper
    return decorator


class MageGuild:
    @staticmethod
    def validate_mage_name(name: str) -> bool:
        if not isinstance(name ,str):
            return False
        return len(name.replace(" ","")) >= 3 and all(c.isalpha() or c.isspace() for c in name)

    @power_validator(50)
    def cast_spell(self, spell_name: str, power: int) -> str:
        """MEGANIGGA"""
        return f"casted {spell_name} at {power} power"




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
import time
def retry_spell(max_attempts: int) -> Callable:
    def decorator(func):
        def actual_function(*args, **kwargs):
            for i in range(max_attempts):
                try:
                    x = func(*args, **kwargs)
                    print(f"congrat, your function passed at {i + 1} attempts")
                    return(x)
                except Exception as e:
                    if i != max_attempts - 1:
                        print(f"Spell failed, retrying... (attempt {i + 1}/{max_attempts})")
                        time.sleep(1)
                    else:
                        print(f"Spell casting failed after {max_attempts} attempts")
        return actual_function
    return decorator


x = 0
@retry_spell(5)
def test_retry():
    global x
    x += 1
    if x < 4:
        raise Exception()
    return "GIGANIGGA"




if __name__ == "__main__":
    test_retry()
