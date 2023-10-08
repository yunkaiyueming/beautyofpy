class Test:

    def __init__(self, foo):
        self.__foo = foo

    def __bar(self):
        print(self.__foo)
        print('__bar')

    def __say(self):
        print(self.__foo)
        print("__say")

def main():
    test = Test('hello')

    test._Test__say()  ##增加 _Test_ 来访问私有属性 

    # AttributeError: 'Test' object has no attribute '__bar'
    test.__bar()
    # AttributeError: 'Test' object has no attribute '__foo'
    print(test.__foo)


if __name__ == "__main__":
    main()