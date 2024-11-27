class Bird:
    def intro(self):
        print(f'There are many types og birds.')

    def flight(self):
        print(f'Most of the birds can fly but some cannot')

class Spparrow(Bird):
    def flight(self):
        print(f'Spparrow can fly')
    
class Ostrich(Bird):
    def flight(self):
        print(f'ostrich can not fly')

bird1 = Bird()
spparrow1 = Spparrow()
ostrich1 = Ostrich()

bird1.intro()
bird1.flight()

spparrow1.intro()
spparrow1.flight()

ostrich1.intro()
ostrich1.flight()


