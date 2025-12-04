class Evaluator:
    @staticmethod
    def zip_evaluate(coefs, words):
        if len(coefs) != len(words):
            return -1
        total = 0
        for coefs, words in zip(coefs, words):
            total += coefs * len(words)
            return total

    @staticmethod
    def enumerate_evaluate(coefs, words):
        if len(coefs) != len(words):
            return -1
        total = 0
        for i, words in enumerate(words):
            total += coefs[i] * len(words)
        return total