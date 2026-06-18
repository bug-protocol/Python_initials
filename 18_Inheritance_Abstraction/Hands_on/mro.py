# Let's consider a simple inheritance

class A:
    def show(self):
        print("A")

class B(A):
    pass

obj = B()
obj.show()  # => it outputs A why because B doesn't have any show 
# so the flow goes like  B => A  => object. It finds A with a show method and hence prints the output.

print(B.mro())

# [<class '__main__.B'>, <class '__main__.A'>, <class 'object'>]

# Now Let's consider a multiple inheritance

class A:
    def show(self):
        print("A")

class B:
    # def show(self):
    #     print("B")
    pass

# class C(A,B):
#     pass

# now this one gives A when we do obj.show because ordering is something like (A, B)
# hence C.mro() is gonna give us
# [<class '__main__.C'>, <class '__main__.A'>, <class '__main__.B'>, <class 'object'>]


# Now let's change the order

class C(B, A):
    pass
# now this one gives B when we do obj.show because ordering is something like (B, A)
# hence C.mro() is gonna give us
# [<class '__main__.C'>, <class '__main__.B'>, <class '__main__.A'>, <class 'object'>]


obj = C()

obj.show()
print(C.mro())


# Hence when C(A, B) A gets the priority
# when C(B, A) B gets the priority

# Also even if the priority is C(A, B) but A doesn't contain the required method like show() it'll go look for this in B



# Here we are going to call parent method manually
class A:
    def show(self):
        print("A")

class B:
    def show(self):
        print("B")

class C(A,B):
    def show(self):
        B.show(self)

obj = C()
obj.show()

# Here we know the order of calling is C -> A -> B, 
# but when C is called -> it invokes the method of B
# hence here we bypassed MRO and hence we can use method of B



# Using super() method

# it invokes the next object of invoked method in mro order

class A:
    def show(self):
        print("A")
        super().show()

class B:
    def show(self):
        print("B")

class C(A, B):
    def show(self):
        print("C")
        super().show()

obj = C()
obj.show()

# We get output as 
# C
# A

# If we use super().show() on the already used method

# we get output as
# C
# A
# B






