import json
from .exercise import Savol


class SavolManager:
    @staticmethod
    def load_questions():
        try:
            with open("savollar.json") as savollar:
                savollar = json.load(savollar)
                savollar_obj = []
                for savol in savollar:
                    savollar_obj.append(
                        Savol(savol["matn"], savol["variantlar"], savol["togri_javob"], savol["kategoriya"]))
                return savollar_obj

        except FileNotFoundError:
            print("Error: File not found")
            return False
