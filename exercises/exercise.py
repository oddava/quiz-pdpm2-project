class Savol:
    def __init__(self, matn, variantlar, togri_javob, kategoriya):
        self.matn : str = matn
        self.variantlar : list = variantlar
        self.togri_javob : int = togri_javob
        self.kategoriya : str = kategoriya

    def __str__(self):
        harflar = ['a', 'b', 'c', 'd']
        varianlar_str = '\n '.join(f"{h}) {v}" for h, v in zip(harflar, self.variantlar))

        return f"Savol: {self.matn}\n {varianlar_str}\n"

    def __repr__(self):
        return f"Savol(matn={self.matn})"