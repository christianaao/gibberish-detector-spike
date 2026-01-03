# Please note that this code does not work, and has only been uploaded for educational purposes

from gibberishpy.scanner import GibberishScanner


def build_model():
    scanner = GibberishScanner()
    scanner.build_model(corpus_path="philosophy.model", n_gram_size=2)
    scanner.save_model("transition_matrix_2d.tm", encoding="utf-8")


def scan_gibberish():
    scanner = GibberishScanner()
    scanner.load_model(path="transition_matrix_2d.tm")
    additive_cum_proba, multiplicative_cum_proba = scanner.scan("ldfjgnkdfjnd")
    print(additive_cum_proba)
    print(multiplicative_cum_proba)


# build_model()
# scan_gibberish()
