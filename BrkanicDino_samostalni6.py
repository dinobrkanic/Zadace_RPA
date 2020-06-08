import random
import os
from pogodibrojerror import pogodibrojerror
class PogodiBroj:
    def __init__(self):
        self.number = random.randint(1, 100)
        self.count = 0

    def display_title_bar(self):
        print("\t**************************************************")
        print("\t*******Pogađanje broja*********")
        print("\t*************************************************")

    def get_user_choice(self):
        print("\n[1] Igraj pogađanje broja.")
        print("[x] Izlaz.")
        return input("Što želite napraviti?")

    def start_game(self):
        while True:
            while True:
                choice = input("Pogodi broj")
                if choice[0] in range (1, 101)
                    break
            if choice[0] < self.number:
                print("Vaš broj je manji od traženog broja")
                count = count + 1
            elif choice[0] > self.number:
                print("Vaš broj je veći od traženog broja")
                count = count + 1
            elif choice[0] == self.number:
                print("Pogodak! Točno!")
                game = PogodiBroj()
                game.play()
            if count == 10:
                print("Potrošili ste sve pokušaje, traženi broj je: {}".format(self.number)
                game = PogodiBroj()
                game.play()  
    
    def play(self):
        choice = ''
        self.display_title_bar
        while choice != 'x'
            choice = self.get_user_choice()
            self.display_title_bar()
            if choice == '1':
                def.start_game()
            elif choice == 'x':
                print("\n Hvala na igri. Pozdrav!")
            else:
                print("Hvatanje izuzetaka")

if __name__ == "__main__":
    game = PogodiBroj()
    game.play()