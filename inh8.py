class Base:
    def __init__(self):
        print("Inside class Base default constructor")

class Derived(Base):
        pass

class Inh8:
    @staticmethod
    def main():
        obj = Derived()

Inh8.main()
