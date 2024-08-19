class A:
    def hablar(self):
        print("estoy hablando desde A")
        
class F(A):
    def hablar(self):
        print("estoy hablando desde F")        
        
class B(A):
    def hablar(self):
        print("estoy hablando desde B")    
        
class C(F):
    def hablar(self):
        print("estoy hablando desde C")
        
class D(B,C):
    def hablar(self):
        print("estoy hablando desde D")
        
d = D()
# C.hablar(d)
print(D.mro())                     