import arcade
import arcade.gui

# Game will be in 720p
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
SCREEN_TITLE = "Project Run Game"

# Main menu view
class mainMenuView(arcade.View):
    def __init__(self):
        super().__init__()
        self.manager = arcade.gui.UIManager()
        self.manager.enable()

        # Create layout for buttons
        self.anchor_layout = self.manager.add(arcade.gui.UIAnchorLayout())

        # Start game button
        start_button = arcade.gui.UIFlatButton(text="Press start to begin!", height=100, width=200)
        @start_button.event("on_click")
        def on_click_begin(event):
            game_view = gameView()
            game_view.setup()
            self.window.show_view(game_view)

        # Quit game button
        quit_button = arcade.gui.UIFlatButton(text="Quit Game", height=100, width=200)
        @quit_button.event("on_click")
        def on_click_quit(event):
            arcade.exit()

        # Add buttons to layout
        self.anchor_layout.add(
            child=start_button,
            anchor_x="center_x",
            anchor_y="center_y",
            align_y=50,
        )
        self.anchor_layout.add(
            child=quit_button,
            anchor_x="center_x",
            anchor_y="center_y",
            align_y=-50,
        )

    def on_draw(self):
        """Render main menu"""
        self.clear()  # Clear screen properly
        arcade.set_background_color(arcade.color.RED)
        self.manager.draw()  # Draw UI Manager

    def on_hide_view(self):
        """Disable UI Manager when switching views"""
        self.manager.disable()

# Game view
class gameView(arcade.View):
    def __init__(self):
        super().__init__()
        self.player_sprite = None  # Player sprite
        self.player_score = 0  # Player score

    def setup(self):
        """Set up game starting with a player sprite"""
        self.player_sprite = arcade.SpriteCircle(20, arcade.color.CHERRY)
        self.player_sprite.center_x = SCREEN_WIDTH // 2
        self.player_sprite.center_y = SCREEN_HEIGHT // 2

    def on_draw(self):
        """Render game screen"""
        self.clear()  # Clear screen properly
        arcade.set_background_color(arcade.color.BLACK)
        
        # Draw player sprite and score text
        self.player_sprite.draw()
        arcade.draw_text(f"Score: {self.player_score}", 10, SCREEN_HEIGHT - 30,
                         arcade.color.WHITE, font_size=20)

    def on_key_press(self, key, modifiers):
        """Handle key press events"""
        if key == arcade.key.UP:
            self.player_sprite.change_y = 5
        elif key == arcade.key.DOWN:
            self.player_sprite.change_y = -5
        elif key == arcade.key.LEFT:
            self.player_sprite.change_x = -5
        elif key == arcade.key.RIGHT:
            self.player_sprite.change_x = 5
        elif key == arcade.key.ESCAPE:
            menu_view = mainMenuView()
            self.window.show_view(menu_view)

    def on_key_release(self, key, modifiers):
        """Handle key release events"""
        if key in [arcade.key.UP, arcade.key.DOWN]:
            self.player_sprite.change_y = 0
        if key in [arcade.key.LEFT, arcade.key.RIGHT]:
            self.player_sprite.change_x = 0

    def on_update(self, delta_time):
        """Update game logic"""
        self.player_sprite.update()

# Run program
def main():
    window = arcade.Window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    menu_view = mainMenuView()
    window.show_view(menu_view)
    arcade.run()

if __name__ == "__main__":
    main()
