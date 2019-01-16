"""
method overriding: same name different functions
"""
class Bird:
    def sing(self, song):
        print("A bird sings " + song)
    
class Parrot(Bird):
    def sing(self, song):
        print("This parrot sings " + song)

bird = Bird()
parrot = Parrot()
bird.sing('velvet rope')
parrot.sing('electricity')