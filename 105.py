
class base:
    @staticmethod
    def f1():
        print('base f1')
class derived(base):
    @staticmethod
    def f1(self):
        print('derived f1')
        super().f1()
d=derived()
b=base()
d.f1(d)
d.f1(derived)
derived.f1(d)
derived.f1(derived)
base.f1()
b.f1()

input()
