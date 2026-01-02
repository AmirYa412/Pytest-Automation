class Integers:

    @staticmethod
    def add(x, y):
        try:
            return x + y
        except Exception as e:
            raise Exception(e)

    @staticmethod
    def divide(x, y):
        try:
            return x/y
        except ZeroDivisionError as e:
            raise ZeroDivisionError(e)