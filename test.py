class Foo:
    def __init__(self, **kwargs):
        self.a = kwargs.pop('a', 1)
        print(self.a)

args = {'a':3}
Foo(**args)
Foo()