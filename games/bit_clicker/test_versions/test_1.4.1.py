class Player:
    def __init__(self):
        self.score = 0

    def increase_score(self):
        self.score += 10

    def display_score(self):
        print("Your score:", self.score)

player1 = Player()
player1.increase_score()
player1.display_score()
