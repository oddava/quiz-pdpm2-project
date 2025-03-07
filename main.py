from exercises import SavolManager
from game import Oyin

def main():
    manager = SavolManager()
    savollar = manager.load_questions()
    oyin = Oyin("John", savollar)

    oyin.start_game("Matematika")
    oyin.save_result()
    oyin.show_ranking()


if __name__ == "__main__":
    main()