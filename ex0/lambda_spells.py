def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    return sorted(artifacts, key=lambda artifact: artifact['power'],
                  reverse=True)


def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    return list(filter(lambda mage: mage['power'] >= min_power, mages))


def spell_transformer(spells: list[str]) -> list[str]:
    return list(map(lambda spell: "* " + spell + " *", spells))


def mage_stats(mages: list[dict]) -> dict:
    max_power = round(max(map(lambda mage: mage['power'], mages)), 2)
    min_power = round(min(map(lambda mage: mage['power'], mages)), 2)
    avg_power = round(
        sum(map(lambda mage: mage['power'], mages)) / len(mages), 2
    )
    return {
        'max_power': max_power,
        'min_power': min_power,
        'avg_power': avg_power
    }


if __name__ == "__main__":
    artifacts = [
        {'name': 'Water Chalice', 'power': 110, 'type': 'focus'},
        {'name': 'Storm Crown', 'power': 68, 'type': 'focus'},
        {'name': 'Lightning Rod', 'power': 113, 'type': 'focus'},
        {'name': 'Shadow Blade', 'power': 87, 'type': 'accessory'}
    ]
    mages = [
        {'name': 'Rowan', 'power': 90, 'element': 'earth'},
        {'name': 'Phoenix', 'power': 90, 'element': 'fire'},
        {'name': 'Morgan', 'power': 74, 'element': 'water'},
        {'name': 'Nova', 'power': 89, 'element': 'lightning'},
        {'name': 'River', 'power': 73, 'element': 'fire'}
    ]
    spells = ['freeze', 'shield', 'tsunami', 'flash']

    print("-----data-----")
    print()
    print(f"artifacts: {artifacts}")
    print()
    print(f"mages: {mages}")
    print()
    print(f"spells: {spells}")
    print()
    print("-----data-----")
    print()

    print("Testing artifact sorter...")
    print(" comes before ".join(
        [f"{artifact['name']} ({artifact['power']} power)"
         for artifact in artifact_sorter(artifacts)]
    ))
    print()

    print("Testing power filter...")
    print(" ".join([f"{mage['name']} ({mage['power']} power >= 88)"
          for mage in power_filter(mages, 88)]))
    print()

    print("Testing spell transformer...")
    print(" ".join(spell_transformer(spells)))
    print()

    print("Testing mage stats...")
    print("\n".join([f"{key}: {value}"
          for key, value in mage_stats(mages).items()]))
