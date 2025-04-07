"""File to define River class."""

from exercises.ex04.fish import Fish
from exercises.ex04.bear import Bear


class River:
    day: int
    bears: list[Bear]
    fish: list[Fish]

    def __init__(self, num_fish: int, num_bears: int):
        """New River with num_fish Fish and num_bears Bears"""
        self.day: int = 0
        self.fish: list[Fish] = []
        self.bears: list[Bear] = []
        # populate the river with fish and bears
        for _ in range(0, num_fish):
            self.fish.append(Fish())
        for _ in range(0, num_bears):
            self.bears.append(Bear())

    def check_ages(self):
        kept_fish = []
        for fish in self.fish:
            if fish.age <= 3:
                kept_fish.append(fish)
        self.fish = kept_fish
        kept_bears = []
        for bears in self.bears:
            if bears.age <= 5:
                kept_bears.append(bears)
        self.bears = kept_bears
        return None

    def bears_eating(self):
        if len(self.fish) >= 5:
            for bear in self.bears:
                bear.eat(3)
                self.remove_fish(3)
        return None

    def remove_fish(self, amount: int):
        if amount > len(self.fish):
            amount = len(self.fish)
        while amount > 0:
            self.fish.pop(0)
            amount -= 1

    def check_hunger(self):
        surviving_bears = []
        for bears in self.bears:
            if bears.hunger_score >= 0:
                surviving_bears.append(bears)
        self.bears = surviving_bears
        return None

    def repopulate_fish(self):
        num_fish = len(self.fish)
        num_new_fish = (num_fish // 2) * 4
        new_fish_count = 0
        while new_fish_count < num_new_fish:
            new_unique_fish = Fish()
            self.fish.append(new_unique_fish)
        return None

    def repopulate_bears(self):
        num_bears = len(self.bears)
        num_new_bears = num_bears // 2
        new_bear_count = 0
        while new_bear_count < num_new_bears:
            new_bear = Bear()
            self.bears.append(new_bear)
        return None

    def view_river(self):
        print(f"~~~ Day {self.day}: ~~~")
        print(f"Fish population: {len(self.fish)}")
        print(f"Bear population: {len(self.bears)}")
        return None

    def one_river_day(self):
        """Simulate one day of life in the river"""
        # Increase day by 1
        self.day += 1
        # Simulate one day for all Bears
        for bear in self.bears:
            bear.one_day()
        # Simulate one day for all Fish
        for fish in self.fish:
            fish.one_day()
        # Simulate Bear's eating
        self.bears_eating()
        # Remove hungry Bear's from River
        self.check_hunger()
        # Remove old Fish and Bear's from River
        self.check_ages()
        # Simulate Fish repopulation
        self.repopulate_fish()
        # Simulate Bear repopulation
        self.repopulate_bears()
        # Visualize River
        self.view_river()

    def one_river_week(self):
        self.one_river_day()
        self.one_river_day()
        self.one_river_day()
        self.one_river_day()
        self.one_river_day()
        self.one_river_day()
        self.one_river_day()
