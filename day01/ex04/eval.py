class Evaluator:
    """String weight evaluator"""

    @staticmethod
    def check_args(coefs, words):
        if len(coefs) != len(words):
            return(False)
        if not isinstance(coefs, list):
            return(False)
        if not isinstance(words, list):
            return(False)
        try:
            coefs = list(map(float, coefs))
        except Exception:
            return(False)
        if not all(isinstance(x, str) for x in words):
            return(False)
        return(True)

    @staticmethod
    def zip_evaluate(coefs, words):
        if not Evaluator.check_args(coefs, words):
            return(-1)
        zipped = zip(coefs, words)
        return(sum([x[0] * len(x[1]) for x in zipped]))

    @staticmethod
    def enumerate_evaluate(coefs, words):
        if not Evaluator.check_args(coefs, words):
            return(-1)
        enumerated = [coef * len(words[i]) for i, coef in enumerate(coefs)]
        return(sum(enumerated))


if __name__ == '__main__':
    words = ["Le", "Lorem", "Ipsum", "est", "simple"]
    coefs = [1.0, 2.0, 1.0, 4.0, 0.5]
    # words = ["Le", "Lorem", "Ipsum", "n'", "est", "pas", "simple"]
    # coefs = [0.0, -1.0, 1.0, -12.0, 0.0, 42.42]
    # words = []
    # coefs = []
    print(Evaluator.zip_evaluate(coefs, words))
    print(Evaluator.enumerate_evaluate(coefs, words))
