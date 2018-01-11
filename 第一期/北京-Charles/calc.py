# -*- coding:utf-8 -*-

class Calc:
	def __init__(self, a, b ):
        self.a = a
        self.b = b
    def add(self):
        return self.a + self.b


if __name__ == "__main__":
    a = int(input("shuru 1 :"))
    b = int(input("shuru 2 :"))

    calc = Calc(a,b)
