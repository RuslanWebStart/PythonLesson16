# Урок 16


# Задача 1

class CashRegister:
    
    def __init__(self, money):

        self.money = float(money)

    def top_up(self, x):
        self.money += x
        print('В кассу добавленно:',x)

    def count_1000(self):
        print('В кассе всего:',int(self.money))

    def take_away(self,x):
        if x <= self.money:
            self.money -+ x
            print('Из кассы взяли:',x)
            print('В кассе осталось:',self.money)
        else:
            print('В кассе нет столько')


cashRegister1 = CashRegister(1000)
cashRegister1.top_up(100)
cashRegister1.count_1000()
cashRegister1.take_away(300)

# Задача 2

class Turtle:
    def __init__(self, x=0, y=0, s=1):

        self.x = x  
        self.y = y  
        self.s = s  

    def go_up(self):
        self.y += self.s
        print('go up:',self.y)

    def go_down(self):
        self.y -= self.s
        print('go down:',self.y)

    def go_left(self):
        self.x -= self.s
        print('go left:',self.x)

    def go_right(self):
        self.x += self.s
        print('go right:',self.x)

    def evolve(self):
        self.s += 1
        print('evolve:',self.s)

    def degrade(self):
        if self.s > 1:
            self.s -= 1
            print('degrade:',self.s)
        else:
            print('s не может быть меньше или равно 0')

    def count_moves(self, x2, y2):

        dx = x2 - self.x
        dy = y2 - self.y

        steps_x = (dx / self.s) + (1 if dx % self.s != 0 and dx != 0 else 0)
        steps_y = (dy / self.s) + (1 if dy % self.s != 0 and dy != 0 else 0)

        steps_x = int(steps_x) + (1 if steps_x > int(steps_x) else 0)
        steps_y = int(steps_y) + (1 if steps_y > int(steps_y) else 0)

        if steps_x > steps_y:
            return steps_x
        else:
           return steps_y
          


turtle = Turtle()
turtle.go_up()
turtle.go_right()
print('Вывод минимального количества действий до позиции',turtle.count_moves(5, 5))