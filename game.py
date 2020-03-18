#Passport Collecting game - Player has unlimited time to collect passports on a screen


import arcade
import random

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 1000
SCREEN_HEADER = "Andy's Game Data 9"
SCALING = 10
RONALDINHO_SCALE = 0.5
PASSPORT_COUNT = 100
passport_scale = 0.01

class Game(arcade.Window):
#INITIALISE THE GAME#
    def __init__(self):
        super().__init__(SCREEN_HEIGHT,SCREEN_WIDTH,SCREEN_HEADER)
#DEFINING LISTS
        self.player_list = None
        self.passport_list = None

        self.player_sprite = None
        self.score = 0

        arcade.set_background_color(arcade.color.AERO_BLUE)

#SETTING UP ALL LISTS TO SPRITE LISTS#
    def setup(self):
        self.player_list = arcade.SpriteList()
        self.passport_list = arcade.SpriteList()

        self.player_sprite = arcade.Sprite("images/man.png", RONALDINHO_SCALE)
        self.player_sprite.center_y = 100
        self.player_sprite.center_x = 400

        self.player_list.append(self.player_sprite)
        #FOR LOOP SO EACH PASSPORT RANDOMLY PLACED ON THE SCREEN
        for x in range(PASSPORT_COUNT):
            PASSPORT = arcade.Sprite("images/passport.png", passport_scale)
            PASSPORT.center_x = random.randrange(SCREEN_WIDTH)
            PASSPORT.center_y = random.randrange(SCREEN_HEIGHT)

            self.passport_list.append(PASSPORT)

#COMMANDING PYTHON TO DRAW PASSPORTS AND PLAYER WHILST DISPLAYING END MESSAGE WHEN GAME FINISHES#
    def on_draw(self):
        arcade.start_render()
        self.passport_list.draw()
        self.player_list.draw()

        if self.score > 90:
            output = f"YOU'VE BEEN JAILED FOR IDENTITY FRAUD \n                  PRESS 'Q' to QUIT"
            arcade.draw_text(output, 200, 600, arcade.color.RED_DEVIL, 32)


        elif self.score == 10:
            output = f"COLLECT AS MANY PASSPORTS AS POSSIBLE!"
            arcade.draw_text(output, 60, 600, arcade.color.ANDROID_GREEN, 40)

#MOVING PLAYER_SPRITE WHEN MOUSE IS MOVED#

    def on_mouse_motion(self, x, y, dx, dy):
        self.player_sprite.center_x = x
        self.player_sprite.center_y = y

#ADDING FUNCTION TO QUIT WHEN Q IS PRESSED#

    def on_key_press(self, symbol: int, modifiers: int):
        if symbol == arcade.key.Q:
            arcade.close_window()

#UPDATING LIST WHEN PLAYER COLLIDES WITH PASSPORT#
    def on_update(self, delta_time):
        self.passport_list.update()
        passports_collected = arcade.check_for_collision_with_list(self.player_sprite, self.passport_list)

        for PASSPORT in passports_collected:
            PASSPORT.remove_from_sprite_lists()
            self.score +=1

#COMMANDING TO RUN GAME#
def main():
    window = Game()
    window.setup()
    arcade.run()

if __name__ == "__main__":
        main()







