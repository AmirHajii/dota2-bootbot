from game_window import GameWindow


def main():
    game = GameWindow()

    if not game.find("Dota 2"):
        print("Dota 2 is not running")
        return

    print("Title:", game.title)
    print("Left:", game.left)
    print("Top:", game.top)
    print("Width:", game.width)
    print("Height:", game.height)
    print("Handle:", game.handle)


if __name__ == "__main__":
    main()