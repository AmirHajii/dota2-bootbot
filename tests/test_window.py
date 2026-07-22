from game_window import GameWindow

game = GameWindow("Dota 2")

if game.find():
    print("Dota 2 found")
    print("Title:", game.title)
    print("Left:", game.left)
    print("Top:", game.top)
    print("Width:", game.width)
    print("Height:", game.height)
else:
    print("Dota 2 is not running")