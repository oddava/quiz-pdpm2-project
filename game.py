import random


class Oyin:
    def __init__(self, foydalanuvchi_ism, savollar):
        self.foydalanuvchi_ism: str = foydalanuvchi_ism
        self.savollar = savollar
        self.ball: int = 0

    def start_game(self, kategoriya):
        print("O'yin boshlandi!")
        topic_questions = [x for x in self.savollar if x.kategoriya == kategoriya]
        topic_questions = random.sample(topic_questions, 5)

        for savol in topic_questions:
            answer = input(savol)
            ordered = dict(zip(["a", "b", "c", "d"], [0, 1, 2, 3]))
            try:
                if savol.togri_javob == ordered[answer]:
                    print("To'g'ri javob! +10")
                    self.ball += 10
                    continue
            except KeyError:
                print("Noto'gri tugma!")
                continue
            print("Javobingiz noto'gri")
        print(f"Tabriklaymiz! Siz jami {self.ball} ball to'pladingiz.")

    def save_result(self):
        new_ratings = []
        user_found = False

        with open("natijalar.txt", "r") as file:
            ratings = file.readlines()

        for rating in ratings:
            if not rating.strip():
                continue
            name, point = rating.strip().split("|")

            if name == self.foydalanuvchi_ism:
                new_ratings.append(f"{name}|{self.ball}")
                user_found = True
            else:
                new_ratings.append(rating.strip())
        if not user_found:
            new_ratings.append(f"{self.foydalanuvchi_ism}|{self.ball}")

        with open("natijalar.txt", "w") as file:
            file.write("\n".join(new_ratings) + "\n")

        print("Saqlandi!")

    def show_ranking(self):
        rankings = ""
        with open("natijalar.txt") as file:
            ratings = file.read()

        for rating in ratings.splitlines():
            if not rating:
                continue
            data = rating.split("|")
            name = data[0]
            point = data[1]
            rankings += f"{name} - {point}\n"

        print(rankings)