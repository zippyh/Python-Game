# Zippyh
# must run pip install kivy-garden and garden install joystick in terminal for the program to work
# This program works best in PyCharm
from random import randint

from kivy.app import App
from kivy.garden.joystick import Joystick
from kivy.properties import NumericProperty
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.vector import Vector

num = 199

level = 1

enemy_num = [1, ]

bullet_num = 1
button_press = 0

enabled1 = 1
enabled2 = 1
enabled3 = 1

enemies = 1

num_trig1 = 0

reps = 0


class Player(Label):
    angle = NumericProperty(0)


class Enemy(Label):
    # not actually useful, just needed to put something here
    hi = 1


class Bullet(Label):
    # not actually useful, just needed to put something here
    hi = 1


class Level(Label):
    # not actually useful, just needed to put something here
    hi = 1


class DemoApp(App):

    def build(self):
        self.root = FloatLayout()
        self.level = Level()
        # code for the fire button
        self.fire_button = Button(text='Fire!')
        self.fire_button.size_hint = None, None
        self.fire_button.size = 150, 100
        self.fire_button.center_x = 700
        self.fire_button.center_y = 75
        self.root.add_widget(self.level)
        # code for the player
        self.player = Player()
        self.player.size = 50, 50
        self.root.add_widget(self.player)
        self.root.add_widget(self.fire_button)
        # code for each enemy
        self.enemy = Enemy()
        self.root.add_widget(self.enemy)
        self.enemy.font_size = 100
        self.enemy.color = (1, 0, 0, 1)
        self.enemy.text = 'o'
        self.enemy.center_x = randint(1, 799)
        self.enemy.center_y = randint(1, 599)
        self.enemy2 = Enemy()
        self.root.add_widget(self.enemy2)
        self.enemy2.font_size = 100
        self.enemy2.color = (1, 0, 0, 1)
        self.enemy2.text = 'o'
        self.enemy2.center_x = 1000
        self.enemy2.center_y = 1000
        self.enemy3 = Enemy()
        self.root.add_widget(self.enemy3)
        self.enemy3.font_size = 100
        self.enemy3.color = (1, 0, 0, 1)
        self.enemy3.text = 'o'
        self.enemy3.center_x = 1000
        self.enemy3.center_y = 1000
        # code for each bullet
        self.bullet1 = Bullet()
        self.root.add_widget(self.bullet1)
        self.bullet1.font_size = 10
        self.bullet1.text = 'o'
        self.bullet1.center_x = 1000
        self.bullet1.center_y = 1000
        self.bullet2 = Bullet()
        self.root.add_widget(self.bullet2)
        self.bullet2.font_size = 10
        self.bullet2.text = 'o'
        self.bullet2.center_x = 1000
        self.bullet2.center_y = 1000
        self.bullet3 = Bullet()
        self.root.add_widget(self.bullet3)
        self.bullet3.font_size = 10
        self.bullet3.text = 'o'
        self.bullet3.center_x = 1000
        self.bullet3.center_y = 1000
        self.bullet4 = Bullet()
        self.root.add_widget(self.bullet4)
        self.bullet4.font_size = 10
        self.bullet4.text = 'o'
        self.bullet4.center_x = 1000
        self.bullet4.center_y = 1000
        self.bullet5 = Bullet()
        self.root.add_widget(self.bullet5)
        self.bullet5.font_size = 10
        self.bullet5.text = 'o'
        self.bullet5.center_x = 1000
        self.bullet5.center_y = 1000
        self.bullet6 = Bullet()
        self.root.add_widget(self.bullet6)
        self.bullet6.font_size = 10
        self.bullet6.text = 'o'
        self.bullet6.center_x = 1000
        self.bullet6.center_y = 1000
        self.bullet7 = Bullet()
        self.root.add_widget(self.bullet7)
        self.bullet7.font_size = 10
        self.bullet7.text = 'o'
        self.bullet7.center_x = 1000
        self.bullet7.center_y = 1000
        self.bullet8 = Bullet()
        self.root.add_widget(self.bullet8)
        self.bullet8.font_size = 10
        self.bullet8.text = 'o'
        self.bullet8.center_x = 1000
        self.bullet8.center_y = 1000
        self.bullet9 = Bullet()
        self.root.add_widget(self.bullet9)
        self.bullet9.font_size = 10
        self.bullet9.text = 'o'
        self.bullet9.center_x = 1000
        self.bullet9.center_y = 1000
        self.bullet10 = Bullet()
        self.root.add_widget(self.bullet10)
        self.bullet10.font_size = 10
        self.bullet10.text = 'o'
        self.bullet10.center_x = 1000
        self.bullet10.center_y = 1000
        self.bullet11 = Bullet()
        self.root.add_widget(self.bullet11)
        self.bullet11.font_size = 10
        self.bullet11.text = 'o'
        self.bullet11.center_x = 1000
        self.bullet11.center_y = 1000
        self.bullet12 = Bullet()
        self.root.add_widget(self.bullet12)
        self.bullet12.font_size = 10
        self.bullet12.text = 'o'
        self.bullet12.center_x = 1000
        self.bullet12.center_y = 1000
        self.bullet13 = Bullet()
        self.root.add_widget(self.bullet13)
        self.bullet13.font_size = 10
        self.bullet13.text = 'o'
        self.bullet13.center_x = 1000
        self.bullet13.center_y = 1000
        self.bullet14 = Bullet()
        self.root.add_widget(self.bullet14)
        self.bullet14.font_size = 10
        self.bullet14.text = 'o'
        self.bullet14.center_x = 1000
        self.bullet14.center_y = 1000
        self.bullet15 = Bullet()
        self.root.add_widget(self.bullet15)
        self.bullet15.font_size = 10
        self.bullet15.text = 'o'
        self.bullet15.center_x = 1000
        self.bullet15.center_y = 1000
        self.bullet16 = Bullet()
        self.root.add_widget(self.bullet16)
        self.bullet16.font_size = 10
        self.bullet16.text = 'o'
        self.bullet16.center_x = 1000
        self.bullet16.center_y = 1000
        self.bullet17 = Bullet()
        self.root.add_widget(self.bullet17)
        self.bullet17.font_size = 10
        self.bullet17.text = 'o'
        self.bullet17.center_x = 1000
        self.bullet17.center_y = 1000
        self.bullet18 = Bullet()
        self.root.add_widget(self.bullet18)
        self.bullet18.font_size = 10
        self.bullet18.text = 'o'
        self.bullet18.center_x = 1000
        self.bullet18.center_y = 1000
        self.bullet19 = Bullet()
        self.root.add_widget(self.bullet19)
        self.bullet19.font_size = 10
        self.bullet19.text = 'o'
        self.bullet19.center_x = 1000
        self.bullet19.center_y = 1000
        self.bullet20 = Bullet()
        self.root.add_widget(self.bullet20)
        self.bullet20.font_size = 10
        self.bullet20.text = 'o'
        self.bullet20.center_x = 1000
        self.bullet20.center_y = 1000
        self.root.padding = 50
        joystick = Joystick(size_hint=(0.1, 0.1), outer_size=1, inner_size=0.75, pad_size=0.5, outer_line_width=0.01,
                            inner_line_width=0.01,
                            pad_line_width=0.01)
        joystick.bind(pad=self.update_coordinates)
        self.root.add_widget(joystick)

    def fire_button_press(self, instance):
        global bullet_num
        if bullet_num == 1:
            x_bvel = x_float * 20
            y_bvel = y_float * 20
            self.bullet1.center_x = self.player.center_x
            self.bullet1.center_y = self.player.center_y
            self.bullet1.velocity = (x_bvel, y_bvel)
            bullet_num = bullet_num + 1
        elif bullet_num == 2:
            x_b2vel = x_float * 20
            y_b2vel = y_float * 20
            self.bullet2.center_x = self.player.center_x
            self.bullet2.center_y = self.player.center_y
            self.bullet2.velocity = (x_b2vel, y_b2vel)
            bullet_num = bullet_num + 1
        elif bullet_num == 3:
            x_b3vel = x_float * 20
            y_b3vel = y_float * 20
            self.bullet3.center_x = self.player.center_x
            self.bullet3.center_y = self.player.center_y
            self.bullet3.velocity = (x_b3vel, y_b3vel)
            bullet_num = bullet_num + 1
        elif bullet_num == 4:
            x_b4vel = x_float * 20
            y_b4vel = y_float * 20
            self.bullet4.center_x = self.player.center_x
            self.bullet4.center_y = self.player.center_y
            self.bullet4.velocity = (x_b4vel, y_b4vel)
            bullet_num = bullet_num + 1
        elif bullet_num == 5:
            x_b5vel = x_float * 20
            y_b5vel = y_float * 20
            self.bullet5.center_x = self.player.center_x
            self.bullet5.center_y = self.player.center_y
            self.bullet5.velocity = (x_b5vel, y_b5vel)
            bullet_num = bullet_num + 1
        elif bullet_num == 6:
            x_b6vel = x_float * 20
            y_b6vel = y_float * 20
            self.bullet6.center_x = self.player.center_x
            self.bullet6.center_y = self.player.center_y
            self.bullet6.velocity = (x_b6vel, y_b6vel)
            bullet_num = bullet_num + 1
        elif bullet_num == 7:
            x_b7vel = x_float * 20
            y_b7vel = y_float * 20
            self.bullet7.center_x = self.player.center_x
            self.bullet7.center_y = self.player.center_y
            self.bullet7.velocity = (x_b7vel, y_b7vel)
            bullet_num = bullet_num + 1
        elif bullet_num == 8:
            x_b8vel = x_float * 20
            y_b8vel = y_float * 20
            self.bullet8.center_x = self.player.center_x
            self.bullet8.center_y = self.player.center_y
            self.bullet8.velocity = (x_b8vel, y_b8vel)
            bullet_num = bullet_num + 1
        elif bullet_num == 9:
            x_b9vel = x_float * 20
            y_b9vel = y_float * 20
            self.bullet9.center_x = self.player.center_x
            self.bullet9.center_y = self.player.center_y
            self.bullet9.velocity = (x_b9vel, y_b9vel)
            bullet_num = bullet_num + 1
        elif bullet_num == 10:
            x_b10vel = x_float * 20
            y_b10vel = y_float * 20
            self.bullet10.center_x = self.player.center_x
            self.bullet10.center_y = self.player.center_y
            self.bullet10.velocity = (x_b10vel, y_b10vel)
            bullet_num = bullet_num + 1
        elif bullet_num == 11:
            x_b11vel = x_float * 20
            y_b11vel = y_float * 20
            self.bullet11.center_x = self.player.center_x
            self.bullet11.center_y = self.player.center_y
            self.bullet11.velocity = (x_b11vel, y_b11vel)
            bullet_num = bullet_num + 1
        elif bullet_num == 12:
            x_b12vel = x_float * 20
            y_b12vel = y_float * 20
            self.bullet12.center_x = self.player.center_x
            self.bullet12.center_y = self.player.center_y
            self.bullet12.velocity = (x_b12vel, y_b12vel)
            bullet_num = bullet_num + 1
        elif bullet_num == 13:
            x_b13vel = x_float * 20
            y_b13vel = y_float * 20
            self.bullet13.center_x = self.player.center_x
            self.bullet13.center_y = self.player.center_y
            self.bullet13.velocity = (x_b13vel, y_b13vel)
            bullet_num = bullet_num + 1
        elif bullet_num == 14:
            x_b14vel = x_float * 20
            y_b14vel = y_float * 20
            self.bullet14.center_x = self.player.center_x
            self.bullet14.center_y = self.player.center_y
            self.bullet14.velocity = (x_b14vel, y_b14vel)
            bullet_num = bullet_num + 1
        elif bullet_num == 15:
            x_b15vel = x_float * 20
            y_b15vel = y_float * 20
            self.bullet15.center_x = self.player.center_x
            self.bullet15.center_y = self.player.center_y
            self.bullet15.velocity = (x_b15vel, y_b15vel)
            bullet_num = bullet_num + 1
        elif bullet_num == 16:
            x_b16vel = x_float * 20
            y_b16vel = y_float * 20
            self.bullet16.center_x = self.player.center_x
            self.bullet16.center_y = self.player.center_y
            self.bullet16.velocity = (x_b16vel, y_b16vel)
            bullet_num = bullet_num + 1
        elif bullet_num == 17:
            x_b17vel = x_float * 20
            y_b17vel = y_float * 20
            self.bullet17.center_x = self.player.center_x
            self.bullet17.center_y = self.player.center_y
            self.bullet17.velocity = (x_b17vel, y_b17vel)
            bullet_num = bullet_num + 1
        elif bullet_num == 18:
            x_b18vel = x_float * 20
            y_b18vel = y_float * 20
            self.bullet18.center_x = self.player.center_x
            self.bullet18.center_y = self.player.center_y
            self.bullet18.velocity = (x_b18vel, y_b18vel)
            bullet_num = bullet_num + 1
        elif bullet_num == 19:
            x_b19vel = x_float * 20
            y_b19vel = y_float * 20
            self.bullet19.center_x = self.player.center_x
            self.bullet19.center_y = self.player.center_y
            self.bullet19.velocity = (x_b19vel, y_b19vel)
            bullet_num = bullet_num + 1
        elif bullet_num == 20:
            x_b20vel = x_float * 20
            y_b20vel = y_float * 20
            self.bullet20.center_x = self.player.center_x
            self.bullet20.center_y = self.player.center_y
            self.bullet20.velocity = (x_b20vel, y_b20vel)
            bullet_num = 1
        global button_press
        button_press = button_press + 1

    def update_coordinates(self, joystick, pad):
        global enabled1
        global enabled2
        global enabled3
        global enemies
        global reps
        self.level.font_size = 50
        self.level.center_x = 400
        self.level.center_y = 550
        global level
        self.level.text = 'Level: ' + str(level)
        global x_float
        x_float = float(str(pad[0])[0:5])
        global y_float
        y_float = float(str(pad[1])[0:5])
        self.player.font_size = 100
        self.player.text = 'o'
        self.player.center_x = 400 - 400 * (-1 * x_float)
        self.player.center_y = 300 - 300 * (-1 * y_float)
        self.fire_button.bind(on_press=self.fire_button_press)
        if button_press == 0:
            x_bvel = 0
            y_bvel = 0
            self.bullet1.velocity = (x_bvel, y_bvel)
            x_b2vel = 0
            y_b2vel = 0
            self.bullet2.velocity = (x_b2vel, y_b2vel)
            x_b3vel = 0
            y_b3vel = 0
            self.bullet3.velocity = (x_b3vel, y_b3vel)
            x_b4vel = 0
            y_b4vel = 0
            self.bullet4.velocity = (x_b4vel, y_b4vel)
            x_b5vel = 0
            y_b5vel = 0
            self.bullet5.velocity = (x_b5vel, y_b5vel)
            x_b6vel = 0
            y_b6vel = 0
            self.bullet6.velocity = (x_b6vel, y_b6vel)
            x_b7vel = 0
            y_b7vel = 0
            self.bullet7.velocity = (x_b7vel, y_b7vel)
            x_b8vel = 0
            y_b8vel = 0
            self.bullet8.velocity = (x_b8vel, y_b8vel)
            x_b9vel = 0
            y_b9vel = 0
            self.bullet9.velocity = (x_b9vel, y_b9vel)
            x_b10vel = 0
            y_b10vel = 0
            self.bullet10.velocity = (x_b10vel, y_b10vel)
            x_b11vel = 0
            y_b11vel = 0
            self.bullet11.velocity = (x_b11vel, y_b11vel)
            x_b12vel = 0
            y_b12vel = 0
            self.bullet12.velocity = (x_b12vel, y_b12vel)
            x_b13vel = 0
            y_b13vel = 0
            self.bullet13.velocity = (x_b13vel, y_b13vel)
            x_b14vel = 0
            y_b14vel = 0
            self.bullet14.velocity = (x_b14vel, y_b14vel)
            x_b15vel = 0
            y_b15vel = 0
            self.bullet15.velocity = (x_b15vel, y_b15vel)
            x_b16vel = 0
            y_b16vel = 0
            self.bullet16.velocity = (x_b16vel, y_b16vel)
            x_b17vel = 0
            y_b17vel = 0
            self.bullet17.velocity = (x_b17vel, y_b17vel)
            x_b18vel = 0
            y_b18vel = 0
            self.bullet18.velocity = (x_b18vel, y_b18vel)
            x_b19vel = 0
            y_b19vel = 0
            self.bullet19.velocity = (x_b19vel, y_b19vel)
            x_b20vel = 0
            y_b20vel = 0
            self.bullet20.velocity = (x_b20vel, y_b20vel)
        # makes each bullet move
        self.bullet1.pos = Vector(*self.bullet1.velocity) + self.bullet1.pos
        self.bullet2.pos = Vector(*self.bullet2.velocity) + self.bullet2.pos
        self.bullet3.pos = Vector(*self.bullet3.velocity) + self.bullet3.pos
        self.bullet4.pos = Vector(*self.bullet4.velocity) + self.bullet4.pos
        self.bullet5.pos = Vector(*self.bullet5.velocity) + self.bullet5.pos
        self.bullet6.pos = Vector(*self.bullet6.velocity) + self.bullet6.pos
        self.bullet7.pos = Vector(*self.bullet7.velocity) + self.bullet7.pos
        self.bullet8.pos = Vector(*self.bullet8.velocity) + self.bullet8.pos
        self.bullet9.pos = Vector(*self.bullet9.velocity) + self.bullet9.pos
        self.bullet10.pos = Vector(*self.bullet10.velocity) + self.bullet10.pos
        self.bullet11.pos = Vector(*self.bullet11.velocity) + self.bullet11.pos
        self.bullet12.pos = Vector(*self.bullet12.velocity) + self.bullet12.pos
        self.bullet13.pos = Vector(*self.bullet13.velocity) + self.bullet13.pos
        self.bullet14.pos = Vector(*self.bullet14.velocity) + self.bullet14.pos
        self.bullet15.pos = Vector(*self.bullet15.velocity) + self.bullet15.pos
        self.bullet16.pos = Vector(*self.bullet16.velocity) + self.bullet16.pos
        self.bullet17.pos = Vector(*self.bullet17.velocity) + self.bullet17.pos
        self.bullet18.pos = Vector(*self.bullet18.velocity) + self.bullet18.pos
        self.bullet19.pos = Vector(*self.bullet19.velocity) + self.bullet19.pos
        self.bullet20.pos = Vector(*self.bullet20.velocity) + self.bullet20.pos
        global num
        num = num + 1
        if level == 1:
            if num >= 200:
                num = 0
                global x_vel
                x_vel = randint(-10, 10)
                global y_vel
                y_vel = randint(-10, 10)
                self.enemy.velocity = (x_vel, y_vel)
            # code that makes the enemy move
            self.enemy.pos = Vector(*self.enemy.velocity) + self.enemy.pos
            # if the enemy goes out of bounds they are brought back in bounds
            if self.enemy.center_x >= 800 or self.enemy.center_y >= 600 or self.enemy.center_x <= 0 or self.enemy.center_y <= 0:
                if self.enemy.center_x >= 800:
                    self.enemy.center_x = 790
                if self.enemy.center_y >= 600:
                    self.enemy.center_y = 590
                if self.enemy.center_x <= 0:
                    self.enemy.center_x = 10
                if self.enemy.center_y <= 0:
                    self.enemy.center_y = 10
                x_vel = x_vel * -1.2
                y_vel = y_vel * -1.2
                self.enemy.velocity = (x_vel, y_vel)
            # if the enemy is hit the level progresses
            if self.enemy.center_x - 50 < self.bullet1.center_x < self.enemy.center_x + 25 and self.enemy.center_y - 25 < self.bullet1.center_y < self.enemy.center_y + 25 or self.enemy.center_x - 50 < self.bullet2.center_x < self.enemy.center_x + 25 and self.enemy.center_y - 25 < self.bullet2.center_y < self.enemy.center_y + 25 or self.enemy.center_x - 50 < self.bullet3.center_x < self.enemy.center_x + 25 and self.enemy.center_y - 25 < self.bullet3.center_y < self.enemy.center_y + 25 or self.enemy.center_x - 50 < self.bullet4.center_x < self.enemy.center_x + 25 and self.enemy.center_y - 25 < self.bullet4.center_y < self.enemy.center_y + 25 or self.enemy.center_x - 50 < self.bullet5.center_x < self.enemy.center_x + 25 and self.enemy.center_y - 25 < self.bullet5.center_y < self.enemy.center_y + 25 or self.enemy.center_x - 50 < self.bullet6.center_x < self.enemy.center_x + 25 and self.enemy.center_y - 25 < self.bullet6.center_y < self.enemy.center_y + 25 or self.enemy.center_x - 50 < self.bullet7.center_x < self.enemy.center_x + 25 and self.enemy.center_y - 25 < self.bullet7.center_y < self.enemy.center_y + 25 or self.enemy.center_x - 50 < self.bullet8.center_x < self.enemy.center_x + 25 and self.enemy.center_y - 25 < self.bullet8.center_y < self.enemy.center_y + 25 or self.enemy.center_x - 50 < self.bullet9.center_x < self.enemy.center_x + 25 and self.enemy.center_y - 25 < self.bullet9.center_y < self.enemy.center_y + 25 or self.enemy.center_x - 50 < self.bullet10.center_x < self.enemy.center_x + 25 and self.enemy.center_y - 25 < self.bullet10.center_y < self.enemy.center_y + 25 or self.enemy.center_x - 50 < self.bullet11.center_x < self.enemy.center_x + 25 and self.enemy.center_y - 25 < self.bullet11.center_y < self.enemy.center_y + 25 or self.enemy.center_x - 50 < self.bullet12.center_x < self.enemy.center_x + 25 and self.enemy.center_y - 25 < self.bullet12.center_y < self.enemy.center_y + 25 or self.enemy.center_x - 50 < self.bullet13.center_x < self.enemy.center_x + 25 and self.enemy.center_y - 25 < self.bullet13.center_y < self.enemy.center_y + 25 or self.enemy.center_x - 50 < self.bullet14.center_x < self.enemy.center_x + 25 and self.enemy.center_y - 25 < self.bullet14.center_y < self.enemy.center_y + 25 or self.enemy.center_x - 50 < self.bullet15.center_x < self.enemy.center_x + 25 and self.enemy.center_y - 25 < self.bullet15.center_y < self.enemy.center_y + 25 or self.enemy.center_x - 50 < self.bullet16.center_x < self.enemy.center_x + 25 and self.enemy.center_y - 25 < self.bullet16.center_y < self.enemy.center_y + 25 or self.enemy.center_x - 50 < self.bullet17.center_x < self.enemy.center_x + 25 and self.enemy.center_y - 25 < self.bullet17.center_y < self.enemy.center_y + 25 or self.enemy.center_x - 50 < self.bullet18.center_x < self.enemy.center_x + 25 and self.enemy.center_y - 25 < self.bullet18.center_y < self.enemy.center_y + 25 or self.enemy.center_x - 50 < self.bullet19.center_x < self.enemy.center_x + 25 and self.enemy.center_y - 25 < self.bullet19.center_y < self.enemy.center_y + 25 or self.enemy.center_x - 50 < self.bullet20.center_x < self.enemy.center_x + 25 and self.enemy.center_y - 25 < self.bullet20.center_y < self.enemy.center_y + 25:
                enemies = enemies + 1
                num = num - 200
                self.enemy.center_x = 400
                self.enemy.center_y = 300
                level = level + 1
            # if the player is hit the game ends
            if self.player.center_x - 50 < self.enemy.center_x < self.player.center_x + 25 and self.player.center_y - 25 < self.enemy.center_y < self.player.center_y + 25:
                self.root.remove_widget(self.player)
                self.level.text = 'Game Over!'
                self.root.remove_widget(joystick)
        # code for second level
        if level == 2:
            if num >= 200:
                reps = reps + 1
                num = 0
                x_vel = randint(-10, 10)
                y_vel = randint(-10, 10)
                global x_vel2
                x_vel2 = 0
                global y_vel2
                y_vel2 = 0
                self.enemy2.velocity = (x_vel2, y_vel2)
                if enabled1 == 1:
                    self.enemy.velocity = (x_vel, y_vel)
                enemy_num.append(randint(1, 10000))
                if enabled2 == 1:
                    if len(enemy_num) == 2:
                        self.enemy2.center_x = randint(1, 799)
                        self.enemy2.center_y = randint(1, 599)
                if len(enemy_num) > 1:
                    x_vel2 = randint(-10, 10)
                    y_vel2 = randint(-10, 10)
                    if enabled2 == 1:
                        self.enemy2.velocity = (x_vel2, y_vel2)
            if enabled1 == 1:
                self.enemy.pos = Vector(*self.enemy.velocity) + self.enemy.pos
            if enabled2 == 1:
                if len(enemy_num) > 1:
                    self.enemy2.pos = Vector(*self.enemy2.velocity) + self.enemy2.pos
                    if self.enemy2.center_x >= 800 or self.enemy2.center_y >= 600 or self.enemy2.center_x <= 0 or self.enemy2.center_y <= 0:
                        if self.enemy2.center_x >= 800:
                            self.enemy2.center_x = 790
                        if self.enemy2.center_y >= 600:
                            self.enemy2.center_y = 590
                        if self.enemy2.center_x <= 0:
                            self.enemy2.center_x = 10
                        if self.enemy2.center_y <= 0:
                            self.enemy2.center_y = 10
                        x_vel2 = x_vel2 * -1.2
                        y_vel2 = y_vel2 * -1.2
                        self.enemy2.velocity = (x_vel2, y_vel2)
            if enabled1 == 1:
                if self.enemy.center_x >= 800 or self.enemy.center_y >= 600 or self.enemy.center_x <= 0 or self.enemy.center_y <= 0:
                    if self.enemy.center_x >= 800:
                        self.enemy.center_x = 790
                    if self.enemy.center_y >= 600:
                        self.enemy.center_y = 590
                    if self.enemy.center_x <= 0:
                        self.enemy.center_x = 10
                    if self.enemy.center_y <= 0:
                        self.enemy.center_y = 10
                    x_vel = x_vel * -1.2
                    y_vel = y_vel * -1.2
                    self.enemy.velocity = (x_vel, y_vel)
            if self.enemy.center_x - 50 < self.bullet1.center_x < self.enemy.center_x + 25 and self.enemy.center_y - 25 < self.bullet1.center_y < self.enemy.center_y + 25 or self.enemy.center_x - 50 < self.bullet2.center_x < self.enemy.center_x + 25 and self.enemy.center_y - 25 < self.bullet2.center_y < self.enemy.center_y + 25 or self.enemy.center_x - 50 < self.bullet3.center_x < self.enemy.center_x + 25 and self.enemy.center_y - 25 < self.bullet3.center_y < self.enemy.center_y + 25 or self.enemy.center_x - 50 < self.bullet4.center_x < self.enemy.center_x + 25 and self.enemy.center_y - 25 < self.bullet4.center_y < self.enemy.center_y + 25 or self.enemy.center_x - 50 < self.bullet5.center_x < self.enemy.center_x + 25 and self.enemy.center_y - 25 < self.bullet5.center_y < self.enemy.center_y + 25 or self.enemy.center_x - 50 < self.bullet6.center_x < self.enemy.center_x + 25 and self.enemy.center_y - 25 < self.bullet6.center_y < self.enemy.center_y + 25 or self.enemy.center_x - 50 < self.bullet7.center_x < self.enemy.center_x + 25 and self.enemy.center_y - 25 < self.bullet7.center_y < self.enemy.center_y + 25 or self.enemy.center_x - 50 < self.bullet8.center_x < self.enemy.center_x + 25 and self.enemy.center_y - 25 < self.bullet8.center_y < self.enemy.center_y + 25 or self.enemy.center_x - 50 < self.bullet9.center_x < self.enemy.center_x + 25 and self.enemy.center_y - 25 < self.bullet9.center_y < self.enemy.center_y + 25 or self.enemy.center_x - 50 < self.bullet10.center_x < self.enemy.center_x + 25 and self.enemy.center_y - 25 < self.bullet10.center_y < self.enemy.center_y + 25 or self.enemy.center_x - 50 < self.bullet11.center_x < self.enemy.center_x + 25 and self.enemy.center_y - 25 < self.bullet11.center_y < self.enemy.center_y + 25 or self.enemy.center_x - 50 < self.bullet12.center_x < self.enemy.center_x + 25 and self.enemy.center_y - 25 < self.bullet12.center_y < self.enemy.center_y + 25 or self.enemy.center_x - 50 < self.bullet13.center_x < self.enemy.center_x + 25 and self.enemy.center_y - 25 < self.bullet13.center_y < self.enemy.center_y + 25 or self.enemy.center_x - 50 < self.bullet14.center_x < self.enemy.center_x + 25 and self.enemy.center_y - 25 < self.bullet14.center_y < self.enemy.center_y + 25 or self.enemy.center_x - 50 < self.bullet15.center_x < self.enemy.center_x + 25 and self.enemy.center_y - 25 < self.bullet15.center_y < self.enemy.center_y + 25 or self.enemy.center_x - 50 < self.bullet16.center_x < self.enemy.center_x + 25 and self.enemy.center_y - 25 < self.bullet16.center_y < self.enemy.center_y + 25 or self.enemy.center_x - 50 < self.bullet17.center_x < self.enemy.center_x + 25 and self.enemy.center_y - 25 < self.bullet17.center_y < self.enemy.center_y + 25 or self.enemy.center_x - 50 < self.bullet18.center_x < self.enemy.center_x + 25 and self.enemy.center_y - 25 < self.bullet18.center_y < self.enemy.center_y + 25 or self.enemy.center_x - 50 < self.bullet19.center_x < self.enemy.center_x + 25 and self.enemy.center_y - 25 < self.bullet19.center_y < self.enemy.center_y + 25 or self.enemy.center_x - 50 < self.bullet20.center_x < self.enemy.center_x + 25 and self.enemy.center_y - 25 < self.bullet20.center_y < self.enemy.center_y + 25:
                if reps > 1:
                    enabled1 = 2
                    self.enemy.center_x = 1000
                    self.enemy.center_y = 1000
            if self.enemy2.center_x - 50 < self.bullet1.center_x < self.enemy2.center_x + 25 and self.enemy2.center_y - 25 < self.bullet1.center_y < self.enemy2.center_y + 25 or self.enemy2.center_x - 50 < self.bullet2.center_x < self.enemy2.center_x + 25 and self.enemy2.center_y - 25 < self.bullet2.center_y < self.enemy2.center_y + 25 or self.enemy2.center_x - 50 < self.bullet3.center_x < self.enemy2.center_x + 25 and self.enemy2.center_y - 25 < self.bullet3.center_y < self.enemy2.center_y + 25 or self.enemy2.center_x - 50 < self.bullet4.center_x < self.enemy2.center_x + 25 and self.enemy2.center_y - 25 < self.bullet4.center_y < self.enemy2.center_y + 25 or self.enemy2.center_x - 50 < self.bullet5.center_x < self.enemy2.center_x + 25 and self.enemy2.center_y - 25 < self.bullet5.center_y < self.enemy2.center_y + 25 or self.enemy2.center_x - 50 < self.bullet6.center_x < self.enemy2.center_x + 25 and self.enemy2.center_y - 25 < self.bullet6.center_y < self.enemy2.center_y + 25 or self.enemy2.center_x - 50 < self.bullet7.center_x < self.enemy2.center_x + 25 and self.enemy2.center_y - 25 < self.bullet7.center_y < self.enemy2.center_y + 25 or self.enemy2.center_x - 50 < self.bullet8.center_x < self.enemy2.center_x + 25 and self.enemy2.center_y - 25 < self.bullet8.center_y < self.enemy2.center_y + 25 or self.enemy2.center_x - 50 < self.bullet9.center_x < self.enemy2.center_x + 25 and self.enemy2.center_y - 25 < self.bullet9.center_y < self.enemy2.center_y + 25 or self.enemy2.center_x - 50 < self.bullet10.center_x < self.enemy2.center_x + 25 and self.enemy2.center_y - 25 < self.bullet10.center_y < self.enemy2.center_y + 25 or self.enemy2.center_x - 50 < self.bullet11.center_x < self.enemy2.center_x + 25 and self.enemy2.center_y - 25 < self.bullet11.center_y < self.enemy2.center_y + 25 or self.enemy2.center_x - 50 < self.bullet12.center_x < self.enemy2.center_x + 25 and self.enemy2.center_y - 25 < self.bullet12.center_y < self.enemy2.center_y + 25 or self.enemy2.center_x - 50 < self.bullet13.center_x < self.enemy2.center_x + 25 and self.enemy2.center_y - 25 < self.bullet13.center_y < self.enemy2.center_y + 25 or self.enemy2.center_x - 50 < self.bullet14.center_x < self.enemy2.center_x + 25 and self.enemy2.center_y - 25 < self.bullet14.center_y < self.enemy2.center_y + 25 or self.enemy2.center_x - 50 < self.bullet15.center_x < self.enemy2.center_x + 25 and self.enemy2.center_y - 25 < self.bullet15.center_y < self.enemy2.center_y + 25 or self.enemy2.center_x - 50 < self.bullet16.center_x < self.enemy2.center_x + 25 and self.enemy2.center_y - 25 < self.bullet16.center_y < self.enemy2.center_y + 25 or self.enemy2.center_x - 50 < self.bullet17.center_x < self.enemy2.center_x + 25 and self.enemy2.center_y - 25 < self.bullet17.center_y < self.enemy2.center_y + 25 or self.enemy2.center_x - 50 < self.bullet18.center_x < self.enemy2.center_x + 25 and self.enemy2.center_y - 25 < self.bullet18.center_y < self.enemy2.center_y + 25 or self.enemy2.center_x - 50 < self.bullet19.center_x < self.enemy2.center_x + 25 and self.enemy2.center_y - 25 < self.bullet19.center_y < self.enemy2.center_y + 25 or self.enemy2.center_x - 50 < self.bullet20.center_x < self.enemy2.center_x + 25 and self.enemy2.center_y - 25 < self.bullet20.center_y < self.enemy2.center_y + 25:
                if reps > 1:
                    enabled2 = 2
                    self.enemy2.center_x = 1000
                    self.enemy2.center_y = 1000

            if self.player.center_x - 50 < self.enemy.center_x < self.player.center_x + 25 and self.player.center_y - 25 < self.enemy.center_y < self.player.center_y + 25:
                self.root.remove_widget(self.player)
                self.level.text = 'Game Over!'
                self.root.remove_widget(joystick)
            if self.player.center_x - 50 < self.enemy2.center_x < self.player.center_x + 25 and self.player.center_y - 25 < self.enemy2.center_y < self.player.center_y + 25:
                self.root.remove_widget(self.player)
                self.level.text = 'Game Over!'
                self.root.remove_widget(joystick)
            if enabled2 == 2 and enabled1 == 2:
                self.root.remove_widget(joystick)
                self.level.text = 'Congratulations'

        # unfinished code for third level
        """
        if level == 3:
            if num >= 200:
                num = 0
                x_vel = randint(-10, 10)
                y_vel = randint(-10, 10)
                x_vel2 = 0
                y_vel2 = 0
                global x_vel3
                x_vel3 = 0
                global y_vel3
                y_vel3 = 0
                self.enemy3.velocity = (x_vel3, y_vel3)
                self.enemy2.velocity = (x_vel2, y_vel2)
                self.enemy.velocity = (x_vel, y_vel)
                enemy_num.append(randint(1, 10000))
                if len(enemy_num) == 2:
                    self.enemy2.center_x = randint(1, 799)
                    self.enemy2.center_y = randint(1, 599)
                if len(enemy_num) > 1:
                    x_vel2 = randint(-10, 10)
                    y_vel2 = randint(-10, 10)
                    self.enemy2.velocity = (x_vel2, y_vel2)
                if len(enemy_num) == 3:
                    self.enemy3.center_x = randint(1, 799)
                    self.enemy3.center_y = randint(1, 599)
                if len(enemy_num) > 2:
                    x_vel3 = randint(-10, 10)
                    y_vel3 = randint(-10, 10)
                    self.enemy3.velocity = (x_vel3, y_vel3)

            self.enemy.pos = Vector(*self.enemy.velocity) + self.enemy.pos
            if len(enemy_num) > 1:
                self.enemy2.pos = Vector(*self.enemy2.velocity) + self.enemy2.pos

                if self.enemy2.center_x >= 800 or self.enemy2.center_y >= 600 or self.enemy2.center_x <= 0 or self.enemy2.center_y <= 0:
                    if self.enemy2.center_x >= 800:
                        self.enemy2.center_x = 790
                    if self.enemy2.center_y >= 600:
                        self.enemy2.center_y = 590
                    if self.enemy2.center_x <= 0:
                        self.enemy2.center_x = 10
                    if self.enemy2.center_y <= 0:
                        self.enemy2.center_y = 10
                    x_vel2 = x_vel2 * -1.2
                    y_vel2 = y_vel2 * -1.2
                    self.enemy2.velocity = (x_vel2, y_vel2)
            if len(enemy_num) > 2:
                self.enemy3.pos = Vector(*self.enemy3.velocity) + self.enemy3.pos
                if self.enemy3.center_x >= 800 or self.enemy3.center_y >= 600 or self.enemy3.center_x <= 0 or self.enemy3.center_y <= 0:
                    if self.enemy3.center_x >= 800:
                        self.enemy3.center_x = 790
                    if self.enemy3.center_y >= 600:
                        self.enemy3.center_y = 590
                    if self.enemy3.center_x <= 0:
                        self.enemy3.center_x = 10
                    if self.enemy3.center_y <= 0:
                        self.enemy3.center_y = 10
                    x_vel3 = x_vel3 * -1.2
                    y_vel3 = y_vel3 * -1.2
                    self.enemy3.velocity = (x_vel3, y_vel3)
            if self.enemy.center_x >= 800 or self.enemy.center_y >= 600 or self.enemy.center_x <= 0 or self.enemy.center_y <= 0:
                if self.enemy.center_x >= 800:
                    self.enemy.center_x = 790
                if self.enemy.center_y >= 600:
                    self.enemy.center_y = 590
                if self.enemy.center_x <= 0:
                    self.enemy.center_x = 10
                if self.enemy.center_y <= 0:
                    self.enemy.center_y = 10
                x_vel = x_vel * -1.2
                y_vel = y_vel * -1.2
                self.enemy.velocity = (x_vel, y_vel)
            if self.player.center_x - 50 < self.enemy.center_x < self.player.center_x + 25 and self.player.center_y - 25 < self.enemy.center_y < self.player.center_y + 25:
                self.root.remove_widget(self.player)
                self.level.text = 'Game Over!'
                self.root.remove_widget(joystick)
            if self.player.center_x - 50 < self.enemy2.center_x < self.player.center_x + 25 and self.player.center_y - 25 < self.enemy2.center_y < self.player.center_y + 25:
                self.root.remove_widget(self.player)
                self.level.text = 'Game Over!'
                self.root.remove_widget(joystick)
            if self.player.center_x - 50 < self.enemy3.center_x < self.player.center_x + 25 and self.player.center_y - 25 < self.enemy3.center_y < self.player.center_y + 25:
                self.root.remove_widget(self.player)
                self.level.text = 'Game Over!'
                self.root.remove_widget(joystick)
        """


DemoApp().run()
