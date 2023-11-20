class Fish:
    def __init__(self, name, age, species, size, preferred_food, is_aggressive, needed_space):
        self.__name = name
        self.__age = age
        self.__species = species
        self.__size = size
        self.__preferred_food = preferred_food
        self.__is_aggressive = is_aggressive
        self.__needed_space = needed_space

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    def get_species(self):
        return self.__species

    def get_size(self):
        return self.__size

    def get_peferred_food(self):
        return self.__preferred_food

    def get_is_aggressive(self):
        return self.__is_aggressive

    def get_needed_space(self):
        return self.__needed_space


class Aquarium:
    def __init__(self, total_volume):
        self.__total_volume = total_volume
        self.__free_space = total_volume
        self.__fish_list = []

    def add_fish(self, fish):
        if fish.get_is_aggressive():
            if not self.__fish_list:
                if self.__free_space >= fish.get_needed_space():
                    self.__fish_list.append(fish)
                    self.__free_space -= fish.get_needed_space()
                    print(f"Aggressive fish {fish.get_name()} added to the aquarium.")
                else:
                    print(f"Not enough space for aggressive fish {fish.get_name()} in the aquarium.")
            else:
                print(f"Can't add aggressive fish {fish.get_name()} to an aquarium with non-aggressive fish.")
        else:
            if not self.__fish_list:
                if self.__free_space >= fish.get_needed_space():
                    self.__fish_list.append(fish)
                    self.__free_space -= fish.get_needed_space()
                    print(f"Fish {fish.get_name()} added to the aquarium.")
                else:
                    print(f"Not enough space for fish {fish.get_name()} in the aquarium.")
            else:
                print(f"Can't add non-aggressive fish {fish.get_name()} to an aquarium with aggressive fish.")

    def get_largest_fish(self, n=3):
        sorted_fish = sorted(self.__fish_list, key=lambda x: x.get_size(), reverse=True)
        return sorted_fish[:n]


if __name__ == "__main__":
    fish1 = Fish("Goldie", 2, "Goldfish", 10, "Flakes", False, 5)
    fish2 = Fish("Sharky", 5, "Shark", 50, "Small fish", True, 30)
    fish3 = Fish("Nemo", 1, "Clownfish", 5, "Plankton", True, 3)
    fish4 = Fish("Bubbles", 3, "Angelfish", 8, "Pellets", False, 4)
    fish5 = Fish("Spike", 4, "Pufferfish", 12, "Shrimp", False, 10)
    fish6 = Fish("Dory", 2, "Blue Tang", 7, "Algae", True, 6)
    fish7 = Fish("Finny", 3, "Guppy", 6, "Flakes", False, 3)
    fish8 = Fish("Scales", 2, "Betta", 5, "Pellets", False, 4)

    aquarium1 = Aquarium(100)
    aquarium2 = Aquarium(100)
    aquarium3 = Aquarium(100)
    aquarium4 = Aquarium(100)

    aquarium1.add_fish(fish1)
    aquarium1.add_fish(fish2)
    aquarium2.add_fish(fish3)
    aquarium2.add_fish(fish4)
    aquarium3.add_fish(fish5)
    aquarium3.add_fish(fish6)
    aquarium4.add_fish(fish7)
    aquarium4.add_fish(fish8)

    print("Акваріум 1:")
    for fish in aquarium1.get_largest_fish():
        print(f"{fish.get_name()} - {fish.get_size()} cm")

    print("Акваріум 2:")
    for fish in aquarium2.get_largest_fish():
        print(f"{fish.get_name()} - {fish.get_size()} cm")

    print("Акваріум 3:")
    for fish in aquarium3.get_largest_fish():
        print(f"{fish.get_name()} - {fish.get_size()} cm")
    print("Акваріум 4:")
    for fish in aquarium4.get_largest_fish():
        print(f"{fish.get_name()} - {fish.get_size()} cm")