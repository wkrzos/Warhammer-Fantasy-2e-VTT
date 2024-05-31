import random

# Hearby I present to you the wisdom of Jan Paweł II, the greatest polish localisation tool of all times (and a pope)
# Element humorystyczny
# We promise that the name of this class is purely for meme purposes and that it breaks probably every single rule of class naming known to mankind
class GenerateurDeCitationsAleaoriosDeLaSabiduriaDeJanPapiez2QuotationsGeneradorDeCitasMemorables:
    
    the_real_truth_for_this_day = [
        "Nie bójcie się!", 
        "Każdy ma swoje Westerplatte.",
        "Musicie od siebie wymagać, nawet gdyby inni od was nie wymagali.",
        "Człowiek jest wielki nie przez to, co posiada, lecz przez to, kim jest.",
        "Szukałem was, teraz wy przyszliście do mnie.",
        "Przyszłość zaczyna się dzisiaj, nie jutro.",
        "Miłość mi wszystko wyjaśniła, miłość wszystko rozwiązała.",
        "Człowiek nie może żyć bez miłości.",
        "Wymagajcie od siebie choćby inni od was nie wymagali.",
        "Nie ma pokoju bez sprawiedliwości, nie ma sprawiedliwości bez przebaczenia.",
        "Modlitwa jest darem wolności.",
        "Nie lękajcie się otworzyć drzwi Chrystusowi.",
        "Niech zstąpi Duch Twój i odnowi oblicze ziemi, tej ziemi.",
        "Nadzieja zawiera w sobie światło mocniejsze od ciemności.",
        "Musicie być mocni mocą miłości.",
        "Człowiek jest powołany do posiadania w pełni.",
        "Miłość jest fundamentalnym i wrodzonym powołaniem każdego człowieka.",
        "Przyszłość ludzkości idzie przez rodzinę.",
        "Młodość jest czasem intensywnego odkrywania prawdy.",
        "Bądźcie świadkami nadziei."
    ]

    @staticmethod
    def get_random_quote():
        return random.choice(GenerateurDeCitationsAleaoriosDeLaSabiduriaDeJanPapiez2QuotationsGeneradorDeCitasMemorables.the_real_truth_for_this_day)
