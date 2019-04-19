import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

class SelfTest:
    def function1():
        print("function1 called!")

    def function2(self):
        #print(id(self))
        print("function2 called!")

f = SelfTest()
#print(dir(f))

#f.function1()
#f.function2()

print(id(f))
f.function2()

print(SelfTest.__dict__)
print(SelfTest.function1())
