import arcade

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "ClickRaid Redux"

class ClickRaid(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

        arcade.set_background_color(arcade.csscolor.BLACK)

    def setup(self):
        self.set_mouse_visible(False)
        self.cursor_sprite = arcade.Sprite("images/cursor.png")
        self.cursor_sprite.center_x = 50
        self.cursor_sprite.center_y = 50

    def on_draw(self):
        arcade.start_render()
        self.cursor_sprite.draw()

    def on_mouse_motion(self, x, y, dx, dy):
        self.cursor_sprite.center_x = x
        self.cursor_sprite.center_y = y

window = ClickRaid()
window.setup()
arcade.run()