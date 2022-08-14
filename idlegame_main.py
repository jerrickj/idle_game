import pygame
import pygame_gui
from game_data import *


class IdleGame:
    def __init__(self) -> None:

        # Define Main Stored Game Variables; these are the variables that are saved to the game save file
        self.PLAYER_STARTING_MONEY = 40
        self.player_money = self.PLAYER_STARTING_MONEY
        self.player_level = 1
        self.level_up_cost = 25000  # Change this to increase the cost of leveling up

        # Set up default and starting values for player money increase per tick
        self.constant_money_increase = (
            0.1  # This is the default amount of money that is added with no purchases
        )
        self.total_money_per_tick = (
            self.constant_money_increase
        )  # This is the total amount of money that is added to the player's money every tick

        # Set auto buy variables
        self.auto_buy = False
        self.AUTO_BUY_PRICE = 2500

        # Names, prices, values (per tick (self.fps)), and quantities of items the player has
        self.ITEM_1 = (
            self.ITEM_NAME,
            self.ITEM_1_PRICE,
            self.ITEM_1_VALUE,
            self.ITEM_1_QUANTITY,
        ) = (
            "ITEM_1",
            20,
            0.01,
            0,
        )
        self.ITEM_2 = (
            self.ITEM_NAME,
            self.ITEM_2_PRICE,
            self.ITEM_2_VALUE,
            self.ITEM_2_QUANTITY,
        ) = (
            "ITEM_2",
            50,
            0.05,
            0,
        )
        self.ITEM_3 = (
            self.ITEM_NAME,
            self.ITEM_3_PRICE,
            self.ITEM_3_VALUE,
            self.ITEM_3_QUANTITY,
        ) = (
            "ITEM_3",
            100,
            0.15,
            0,
        )
        self.ITEM_4 = (
            self.ITEM_NAME,
            self.ITEM_4_PRICE,
            self.ITEM_4_VALUE,
            self.ITEM_4_QUANTITY,
        ) = (
            "ITEM_4",
            200,
            0.40,
            0,
        )
        self.ITEM_5 = (
            self.ITEM_NAME,
            self.ITEM_5_PRICE,
            self.ITEM_5_VALUE,
            self.ITEM_5_QUANTITY,
        ) = (
            "ITEM_5",
            400,
            1.0,
            0,
        )
        self.ITEM_6 = (
            self.ITEM_NAME,
            self.ITEM_6_PRICE,
            self.ITEM_6_VALUE,
            self.ITEM_6_QUANTITY,
        ) = (
            "ITEM_6",
            800,
            2.50,
            0,
        )
        self.ITEM_7 = (
            self.ITEM_NAME,
            self.ITEM_7_PRICE,
            self.ITEM_7_VALUE,
            self.ITEM_7_QUANTITY,
        ) = (
            "ITEM_7",
            1600,
            6.20,
            0,
        )
        self.ITEM_8 = (
            self.ITEM_NAME,
            self.ITEM_8_PRICE,
            self.ITEM_8_VALUE,
            self.ITEM_8_QUANTITY,
        ) = (
            "ITEM_8",
            3200,
            2.50,
            0,
        )
        self.ITEM_9 = (
            self.ITEM_NAME,
            self.ITEM_9_PRICE,
            self.ITEM_9_VALUE,
            self.ITEM_9_QUANTITY,
        ) = (
            "ITEM_9",
            6400,
            6.00,
            0,
        )
        self.ITEM_10 = (
            self.ITEM_NAME,
            self.ITEM_10_PRICE,
            self.ITEM_10_VALUE,
            self.ITEM_10_QUANTITY,
        ) = (
            "ITEM_10",
            12800,
            15.00,
            0,
        )
        self.ITEM_11 = (
            self.ITEM_NAME,
            self.ITEM_11_PRICE,
            self.ITEM_11_VALUE,
            self.ITEM_11_QUANTITY,
        ) = (
            "ITEM_11",
            25600,
            35.00,
            0,
        )
        self.ITEM_12 = (
            self.ITEM_NAME,
            self.ITEM_12_PRICE,
            self.ITEM_12_VALUE,
            self.ITEM_12_QUANTITY,
        ) = (
            "ITEM_12",
            51200,
            75.00,
            0,
        )

        self.items = [
            self.ITEM_1,
            self.ITEM_2,
            self.ITEM_3,
            self.ITEM_4,
            self.ITEM_5,
            self.ITEM_6,
            self.ITEM_7,
            self.ITEM_8,
            self.ITEM_9,
            self.ITEM_10,
            self.ITEM_11,
            self.ITEM_12,
        ]

        # self.items_dict = dict()
        # for index, item in enumerate(self.items):
        #     self.items_dict[f"{item[0]}"] = item

        self.AUTO_BUY_FUNCS = [
            (self.buy_item_1_button_pressed, self.ITEM_1_VALUE),
            (self.buy_item_2_button_pressed, self.ITEM_2_VALUE),
            (self.buy_item_3_button_pressed, self.ITEM_3_VALUE),
            (self.buy_item_4_button_pressed, self.ITEM_4_VALUE),
            (self.buy_item_5_button_pressed, self.ITEM_5_VALUE),
            (self.buy_item_6_button_pressed, self.ITEM_6_VALUE),
            (self.buy_item_7_button_pressed, self.ITEM_7_VALUE),
            (self.buy_item_8_button_pressed, self.ITEM_8_VALUE),
            (self.buy_item_9_button_pressed, self.ITEM_9_VALUE),
            (self.buy_item_10_button_pressed, self.ITEM_10_VALUE),
            (self.buy_item_11_button_pressed, self.ITEM_11_VALUE),
            (self.buy_item_12_button_pressed, self.ITEM_12_VALUE),
        ]

        pygame.init()
        pygame.display.set_caption("Idle Clicker")

        self.window_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        self.background = pygame.Surface((WINDOW_WIDTH, WINDOW_HEIGHT))
        self.background.fill(pygame.Color("#111111"))

        self.manager = pygame_gui.UIManager((WINDOW_WIDTH, WINDOW_HEIGHT))

        self.player_level_label = pygame_gui.elements.UILabel(
            relative_rect=pygame.Rect(
                (
                    OUTER_BORDER_WIDTH,
                    OUTER_BORDER_WIDTH,
                ),
                (PLAYER_MONEY_LABEL_WIDTH, PLAYER_MONEY_LABEL_HEIGHT),
            ),
            text=f"Player Level: {self.player_level}",
            manager=self.manager,
        )

        self.player_level_up_button = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect(
                (
                    OUTER_BORDER_WIDTH,
                    OUTER_BORDER_WIDTH + PLAYER_MONEY_LABEL_HEIGHT + BUTTON_PADDING,
                ),
                (FUNCTION_BUTTON_WIDTH, FUNCTION_BUTTON_HEIGHT),
            ),
            text=f"Level Up: -${self.level_up_cost}",
            manager=self.manager,
            tool_tip_text="This button will level up your player and increase your money per tick by 150%",
        )

        self.auto_buy_button = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect(
                (
                    OUTER_BORDER_WIDTH,
                    OUTER_BORDER_WIDTH
                    + (PLAYER_MONEY_LABEL_HEIGHT * 2)
                    + (BUTTON_PADDING * 2),
                ),
                (FUNCTION_BUTTON_WIDTH, FUNCTION_BUTTON_HEIGHT),
            ),
            text="Auto Buy",
            manager=self.manager,
            tool_tip_text="This button will buy affordable items automatically",
            visible=False,
        )
        self.auto_buy_button.visible = False

        self.player_money_label = pygame_gui.elements.UILabel(
            relative_rect=pygame.Rect(
                (PLAYER_MONEY_LABEL_X_POS, PLAYER_MONEY_LABEL_Y_POS),
                (PLAYER_MONEY_LABEL_WIDTH, PLAYER_MONEY_LABEL_HEIGHT),
            ),
            text=f"Player Money: {self.player_money}",
            manager=self.manager,
        )

        self.money_increase_label = pygame_gui.elements.UILabel(
            relative_rect=pygame.Rect(
                (
                    WINDOW_WIDTH // 2
                    - (PLAYER_MONEY_LABEL_WIDTH // 2)
                    + PLAYER_MONEY_LABEL_WIDTH,
                    OUTER_BORDER_WIDTH,
                ),
                (PLAYER_MONEY_LABEL_WIDTH, PLAYER_MONEY_LABEL_HEIGHT),
            ),
            text=f"(+{self.total_money_per_tick} per tick)",
            manager=self.manager,
        )

        # Create a UI element for each item in the shop
        self.buy_item_1_button = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect(
                (OUTER_BORDER_WIDTH, BUTTON_ROW_1_Y_POS),
                (ITEM_BUTTON_WIDTH, ITEM_BUTTON_HEIGHT),
            ),
            text=f"${self.shorten_number(self.ITEM_1_PRICE)}: +{self.ITEM_1_VALUE}",
            manager=self.manager,
        )

        # self.buy_item_1_button = self.CreateItemButton(
        #     self.manager,
        # )

        self.buy_item_2_button = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect(
                (
                    OUTER_BORDER_WIDTH + BUTTON_PADDING + ITEM_BUTTON_WIDTH,
                    BUTTON_ROW_1_Y_POS,
                ),
                (ITEM_BUTTON_WIDTH, ITEM_BUTTON_HEIGHT),
            ),
            text=f"${self.shorten_number(self.ITEM_2_PRICE)}: +{self.ITEM_2_VALUE}",
            manager=self.manager,
        )

        self.buy_item_3_button = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect(
                (
                    OUTER_BORDER_WIDTH + (BUTTON_PADDING * 2) + (ITEM_BUTTON_WIDTH * 2),
                    BUTTON_ROW_1_Y_POS,
                ),
                (ITEM_BUTTON_WIDTH, ITEM_BUTTON_HEIGHT),
            ),
            text=f"${self.shorten_number(self.ITEM_3_PRICE)}: +{self.ITEM_3_VALUE}",
            manager=self.manager,
        )

        self.buy_item_4_button = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect(
                (
                    OUTER_BORDER_WIDTH + (BUTTON_PADDING * 3) + (ITEM_BUTTON_WIDTH * 3),
                    BUTTON_ROW_1_Y_POS,
                ),
                (ITEM_BUTTON_WIDTH, ITEM_BUTTON_HEIGHT),
            ),
            text=f"${self.shorten_number(self.ITEM_4_PRICE)}: +{self.ITEM_4_VALUE}",
            manager=self.manager,
        )

        self.buy_item_5_button = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect(
                (
                    OUTER_BORDER_WIDTH + (BUTTON_PADDING * 4) + (ITEM_BUTTON_WIDTH * 4),
                    BUTTON_ROW_1_Y_POS,
                ),
                (ITEM_BUTTON_WIDTH, ITEM_BUTTON_HEIGHT),
            ),
            text=f"${self.shorten_number(self.ITEM_5_PRICE)}: +{self.ITEM_5_VALUE}",
            manager=self.manager,
        )

        self.buy_item_6_button = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect(
                (
                    OUTER_BORDER_WIDTH + (BUTTON_PADDING * 5) + (ITEM_BUTTON_WIDTH * 5),
                    BUTTON_ROW_1_Y_POS,
                ),
                (ITEM_BUTTON_WIDTH, ITEM_BUTTON_HEIGHT),
            ),
            text=f"${self.shorten_number(self.ITEM_6_PRICE)}: +{self.ITEM_6_VALUE}",
            manager=self.manager,
        )
        # Buttons 7 - 12 are only visible if the player has leveled enough to buy them
        self.buy_item_7_button = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect(
                (OUTER_BORDER_WIDTH, BUTTON_ROW_2_Y_POS),
                (ITEM_BUTTON_WIDTH, ITEM_BUTTON_HEIGHT),
            ),
            text=f"${self.shorten_number(self.ITEM_7_PRICE)}: +{self.ITEM_7_VALUE}",
            manager=self.manager,
            visible=False,
        )

        self.buy_item_8_button = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect(
                (
                    OUTER_BORDER_WIDTH + BUTTON_PADDING + ITEM_BUTTON_WIDTH,
                    BUTTON_ROW_2_Y_POS,
                ),
                (ITEM_BUTTON_WIDTH, ITEM_BUTTON_HEIGHT),
            ),
            text=f"${self.shorten_number(self.ITEM_8_PRICE)}: +{self.ITEM_8_VALUE}",
            manager=self.manager,
            visible=False,
        )

        self.buy_item_9_button = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect(
                (
                    OUTER_BORDER_WIDTH + (BUTTON_PADDING * 2) + (ITEM_BUTTON_WIDTH * 2),
                    BUTTON_ROW_2_Y_POS,
                ),
                (ITEM_BUTTON_WIDTH, ITEM_BUTTON_HEIGHT),
            ),
            text=f"${self.shorten_number(self.ITEM_9_PRICE)}: +{self.ITEM_9_VALUE}",
            manager=self.manager,
            visible=False,
        )

        self.buy_item_10_button = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect(
                (
                    OUTER_BORDER_WIDTH + (BUTTON_PADDING * 3) + (ITEM_BUTTON_WIDTH * 3),
                    BUTTON_ROW_2_Y_POS,
                ),
                (ITEM_BUTTON_WIDTH, ITEM_BUTTON_HEIGHT),
            ),
            text=f"${self.shorten_number(self.ITEM_10_PRICE)}: +{self.ITEM_10_VALUE}",
            manager=self.manager,
            visible=False,
        )

        self.buy_item_11_button = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect(
                (
                    OUTER_BORDER_WIDTH + (BUTTON_PADDING * 4) + (ITEM_BUTTON_WIDTH * 4),
                    BUTTON_ROW_2_Y_POS,
                ),
                (ITEM_BUTTON_WIDTH, ITEM_BUTTON_HEIGHT),
            ),
            text=f"${self.shorten_number(self.ITEM_11_PRICE)}: +{self.ITEM_11_VALUE}",
            manager=self.manager,
            visible=False,
        )

        self.buy_item_12_button = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect(
                (
                    OUTER_BORDER_WIDTH + (BUTTON_PADDING * 5) + (ITEM_BUTTON_WIDTH * 5),
                    BUTTON_ROW_2_Y_POS,
                ),
                (ITEM_BUTTON_WIDTH, ITEM_BUTTON_HEIGHT),
            ),
            text=f"${self.shorten_number(self.ITEM_12_PRICE)}: +{self.ITEM_12_VALUE}",
            manager=self.manager,
            visible=False,
        )

        self.main()

    class CreateItemButton:
        def __init__(
            self,
            manager,
            item_name,
            item_price,
            item_value,
            x_pos,
            y_pos,
            width,
            height,
        ):
            super().__init__()
            self.item_name = item_name
            self.item_price = item_price
            self.item_value = item_value
            self.item_button = pygame_gui.elements.UIButton(
                relative_rect=pygame.Rect(
                    (x_pos, y_pos),
                    (width, height),
                ),
                text=f"{self.item_name}: -${self.item_price}",
                manager=manager,
                tool_tip_text=f"This button will buy {self.item_name} for {self.item_price}",
            )

    class Menu:
        def __init__(self, screen):
            self.screen = screen
            self.screen_rect = screen.get_rect()
            self.menu_items = []
            self.font = pygame.font.SysFont(None, 48)
            self.prep_menu()

    # Shorten input to 2 decimal places
    def truncate(self, input, decimals=2):
        multiplier = 10**decimals
        return int(input * multiplier) / multiplier

    def shorten_number(self, number):
        if number > 999:
            return f"{number / 1000}K"
        if number > 999999:
            return f"{number / 1000000}M"
        if number > 999999999:
            return f"{number / 1000000000}B"
        else:
            return number

    def buy_item_1_button_pressed(self):
        if self.player_money >= self.ITEM_1_PRICE:
            self.player_money -= self.ITEM_1_PRICE
            self.total_money_per_tick += self.ITEM_1_VALUE
            self.ITEM_1_QUANTITY += 1

    def buy_item_2_button_pressed(self):
        if self.player_money >= self.ITEM_2_PRICE:
            self.player_money -= self.ITEM_2_PRICE
            self.total_money_per_tick += self.ITEM_2_VALUE
            self.ITEM_2_QUANTITY += 1

    def buy_item_3_button_pressed(self):
        if self.player_money >= self.ITEM_3_PRICE:
            self.player_money -= self.ITEM_3_PRICE
            self.total_money_per_tick += self.ITEM_3_VALUE
            self.ITEM_3_QUANTITY += 1

    def buy_item_4_button_pressed(self):
        if self.player_money >= self.ITEM_4_PRICE:
            self.player_money -= self.ITEM_4_PRICE
            self.total_money_per_tick += self.ITEM_4_VALUE
            self.ITEM_4_QUANTITY += 1

    def buy_item_5_button_pressed(self):
        if self.player_money >= self.ITEM_5_PRICE:
            self.player_money -= self.ITEM_5_PRICE
            self.total_money_per_tick += self.ITEM_5_VALUE
            self.ITEM_5_QUANTITY += 1

    def buy_item_6_button_pressed(self):
        if self.player_money >= self.ITEM_6_PRICE:
            self.player_money -= self.ITEM_6_PRICE
            self.total_money_per_tick += self.ITEM_6_VALUE
            self.ITEM_6_QUANTITY += 1

    def buy_item_7_button_pressed(self):
        if self.player_money >= self.ITEM_7_PRICE:
            self.player_money -= self.ITEM_7_PRICE
            self.total_money_per_tick += self.ITEM_7_VALUE
            self.ITEM_7_QUANTITY += 1

    def buy_item_8_button_pressed(self):
        if self.player_money >= self.ITEM_8_PRICE:
            self.player_money -= self.ITEM_8_PRICE
            self.total_money_per_tick += self.ITEM_8_VALUE
            self.ITEM_8_QUANTITY += 1

    def buy_item_9_button_pressed(self):
        if self.player_money >= self.ITEM_9_PRICE:
            self.player_money -= self.ITEM_9_PRICE
            self.total_money_per_tick += self.ITEM_9_VALUE
            self.ITEM_9_QUANTITY += 1

    def buy_item_10_button_pressed(self):
        if self.player_money >= self.ITEM_10_PRICE:
            self.player_money -= self.ITEM_10_PRICE
            self.total_money_per_tick += self.ITEM_10_VALUE
            self.ITEM_10_QUANTITY += 1

    def buy_item_11_button_pressed(self):
        if self.player_money >= self.ITEM_11_PRICE:
            self.player_money -= self.ITEM_11_PRICE
            self.total_money_per_tick += self.ITEM_11_VALUE
            self.ITEM_11_QUANTITY += 1

    def buy_item_12_button_pressed(self):
        if self.player_money >= self.ITEM_12_PRICE:
            self.player_money -= self.ITEM_12_PRICE
            self.total_money_per_tick += self.ITEM_12_VALUE
            self.ITEM_12_QUANTITY += 1

    def player_level_up_button_pressed(self):
        self.player_level += 1
        self.player_money -= (
            self.level_up_cost
        )  # Subtract cost of level up from the player's money
        self.total_money_per_tick *= 1.5  # increase money per tick by 50%
        self.level_up_cost *= 2  # increase level up cost by 200%

        self.player_level_label.set_text(f"Player Level: {self.player_level}")
        self.money_increase_label.set_text(f"+{self.total_money_per_tick} per tick)")
        self.player_level_up_button.set_text(f"Level Up: -${self.level_up_cost}")

        if self.player_level >= 2:
            self.buy_item_7_button.visible = True
            self.buy_item_8_button.visible = True
            self.buy_item_9_button.visible = True

        if self.player_level >= 3:
            self.buy_item_10_button.visible = True
            self.buy_item_11_button.visible = True
            self.buy_item_12_button.visible = True

    def auto_buy_button_pressed(self):
        self.auto_buy = not self.auto_buy

        if self.auto_buy:
            self.auto_buy_button.set_text("Auto Buy: ON")

        if not self.auto_buy:
            self.auto_buy_button.set_text("Auto Buy: OFF")
            self.auto_buy_button.colours = (190, 190, 190)

    def check_affordable_items(self):
        if self.player_money >= self.ITEM_1_PRICE:
            self.buy_item_1_button.enable()
        else:
            self.buy_item_1_button.disable()

        if self.player_money >= self.ITEM_2_PRICE:
            self.buy_item_2_button.enable()
        else:
            self.buy_item_2_button.disable()

        if self.player_money >= self.ITEM_3_PRICE:
            self.buy_item_3_button.enable()
        else:
            self.buy_item_3_button.disable()

        if self.player_money >= self.ITEM_4_PRICE:
            self.buy_item_4_button.enable()
        else:
            self.buy_item_4_button.disable()

        if self.player_money >= self.ITEM_5_PRICE:
            self.buy_item_5_button.enable()
        else:
            self.buy_item_5_button.disable()

        if self.player_money >= self.ITEM_6_PRICE:
            self.buy_item_6_button.enable()
        else:
            self.buy_item_6_button.disable()

        if self.player_money >= self.ITEM_7_PRICE:
            self.buy_item_7_button.enable()
        else:
            self.buy_item_7_button.disable()

        if self.player_money >= self.ITEM_8_PRICE:
            self.buy_item_8_button.enable()
        else:
            self.buy_item_8_button.disable()

        if self.player_money >= self.ITEM_9_PRICE:
            self.buy_item_9_button.enable()
        else:
            self.buy_item_9_button.disable()

        if self.player_money >= self.ITEM_10_PRICE:
            self.buy_item_10_button.enable()
        else:
            self.buy_item_10_button.disable()

        if self.player_money >= self.ITEM_11_PRICE:
            self.buy_item_11_button.enable()
        else:
            self.buy_item_11_button.disable()

        if self.player_money >= self.ITEM_12_PRICE:
            self.buy_item_12_button.enable()
        else:
            self.buy_item_12_button.disable()

    def check_player_level(self):
        if self.player_money >= self.level_up_cost:
            self.player_level_up_button.visible = True
            self.player_level_up_button.enable()
        else:
            # self.player_level_up_button.set_text(f"Level Up: -${self.level_up_cost}")
            self.player_level_up_button.disable()
            self.player_level_up_button.visible = False

    def check_auto_buy_req(self):
        if self.player_level >= 2:
            self.auto_buy_button.visible = True
        if self.player_money >= self.AUTO_BUY_PRICE:
            self.auto_buy_button.enable()

    def add_money(self):  # add money per tick
        self.player_money += self.constant_money_increase
        self.player_money += self.ITEM_1_QUANTITY * self.ITEM_1_VALUE
        self.player_money += self.ITEM_2_QUANTITY * self.ITEM_2_VALUE
        self.player_money += self.ITEM_3_QUANTITY * self.ITEM_3_VALUE
        self.player_money += self.ITEM_4_QUANTITY * self.ITEM_4_VALUE
        self.player_money += self.ITEM_5_QUANTITY * self.ITEM_5_VALUE
        self.player_money += self.ITEM_6_QUANTITY * self.ITEM_6_VALUE
        self.player_money += self.ITEM_7_QUANTITY * self.ITEM_7_VALUE
        self.player_money += self.ITEM_8_QUANTITY * self.ITEM_8_VALUE
        self.player_money += self.ITEM_9_QUANTITY * self.ITEM_9_VALUE
        self.player_money += self.ITEM_10_QUANTITY * self.ITEM_10_VALUE
        self.player_money += self.ITEM_11_QUANTITY * self.ITEM_11_VALUE
        self.player_money += self.ITEM_12_QUANTITY * self.ITEM_12_VALUE

        self.player_money = self.truncate(self.player_money)

        self.player_money_label.set_text(
            f"Player Money: {self.shorten_number(self.player_money)}"
        )
        self.money_increase_label.set_text(
            f"(+{self.truncate(self.total_money_per_tick)} per tick)"
        )

    def check_button_events(self, event):
        if event.ui_element == self.buy_item_1_button:
            self.buy_item_1_button_pressed()
        if event.ui_element == self.buy_item_2_button:
            self.buy_item_2_button_pressed()
        if event.ui_element == self.buy_item_3_button:
            self.buy_item_3_button_pressed()
        if event.ui_element == self.buy_item_4_button:
            self.buy_item_4_button_pressed()
        if event.ui_element == self.buy_item_5_button:
            self.buy_item_5_button_pressed()
        if event.ui_element == self.buy_item_6_button:
            self.buy_item_6_button_pressed()
        if event.ui_element == self.buy_item_7_button:
            self.buy_item_7_button_pressed()
        if event.ui_element == self.buy_item_8_button:
            self.buy_item_8_button_pressed()
        if event.ui_element == self.buy_item_9_button:
            self.buy_item_9_button_pressed()
        if event.ui_element == self.buy_item_10_button:
            self.buy_item_10_button_pressed()
        if event.ui_element == self.buy_item_11_button:
            self.buy_item_11_button_pressed()
        if event.ui_element == self.buy_item_12_button:
            self.buy_item_12_button_pressed()
        if event.ui_element == self.player_level_up_button:
            self.player_level_up_button_pressed()
        if event.ui_element == self.auto_buy_button:
            self.auto_buy_button_pressed()

    def main(self):

        self.fps = 10

        clock = pygame.time.Clock()

        is_running = True

        while is_running:

            time_delta = clock.tick(self.fps) / 1000.0

            if self.auto_buy:
                for func, item in self.AUTO_BUY_FUNCS:
                    if self.player_money >= item:
                        func()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    is_running = False

                if event.type == pygame_gui.UI_BUTTON_PRESSED:

                    self.check_button_events(event)

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_m:
                        self.Menu()

                    if event.key == pygame.K_q:
                        is_running = False

                    if event.key == pygame.K_p:
                        self.pause_game()

                self.manager.process_events(event)

            self.check_affordable_items()
            self.check_player_level()
            self.check_auto_buy_req()
            self.add_money()

            self.manager.update(time_delta)

            self.window_surface.blit(self.background, (0, 0))
            self.manager.draw_ui(self.window_surface)

            pygame.display.update()


if __name__ == "__main__":
    IdleGame()
