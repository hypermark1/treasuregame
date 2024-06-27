import random

class TreasureMap:
    def __init__(self, width=10, height=10):
        self.width = width
        self.height = height
        self.treasure_location = self.generate_treasure_location()

    def generate_treasure_location(self):
        x = random.randint(1, self.width)
        y = random.randint(1, self.height)
        return (x, y)

    def check_treasure(self, x, y):
        return self.treasure_location == (x, y)

    def get_hint(self, x, y):
        tx, ty = self.treasure_location
        distance = abs(tx - x) + abs(ty - y)
        return distance

class Player:
    def __init__(self):
        self.attempts = 0
        self.coordinates = []
        self.max_attempts = 7

    def choose_coordinates(self, x, y):
        self.coordinates.append((x, y))
        self.attempts += 1

class Game:
    def __init__(self, player, treasure_map):
        self.player = player
        self.treasure_map = treasure_map

    def start(self):
        print("Welcome to the treasure hunt game!")
        print(f"The treasure is hidden in a {self.treasure_map.width}x{self.treasure_map.height} grid.")
        print(
            f"Enter coordinates in the range x: 1-{self.treasure_map.width} and y: A-{chr(ord('A') + self.treasure_map.height - 1)}, (ex. 1, A).")
        print("You have 7 attempts and you will be given hints to find the treasure.")
        print("The hints will tell you how many steps away you are from the treasure.")
        print("Good luck!")
        while True:
            print(f"Attempt {self.player.attempts + 1}")
            x, y = self.get_user_input()
            self.player.choose_coordinates(x, y)
            if self.treasure_map.check_treasure(x, y):
                print(f"Congratulations! You found the treasure! Attempts: {self.player.attempts}")
                print("Your promocode is 'TREASUREHUNT'.")
                break
            elif self.player.attempts == self.player.max_attempts:
                print("All attempts are used. The treasure has not been found.")
                break
            else:
                hint = self.treasure_map.get_hint(x, y)
                print(f"You are {hint} steps away from the treasure.")

    def get_user_input(self):
        while True:
            try:
                raw_input = input("Enter coordinates (x, y): ")
                x, y = raw_input.split(",")
                x = int(x)
                y = ord(y.upper()) - ord('A') + 1
                if 1 <= x <= self.treasure_map.width and 1 <= y <= self.treasure_map.height:
                    return x, y
                else:
                    print("Coordinates are out of bounds. Please try again.")
            except ValueError:
                print(
                    "Invalid input. Please enter a number for x, followed by a comma, and then a letter for y. For example: '5, C'")

if __name__ == "__main__":
    player = Player()
    treasure_map = TreasureMap()
    game = Game(player, treasure_map)
    game.start()
