# sourcery skip: merge-nested-ifs
import pygame
import pygame_gui


class IdleGame:
    def __init__(self) -> None:

        WINDOW_WIDTH = 800
        WINDOW_HEIGHT = 600

        pygame.init()

        pygame.display.set_caption("Idle Clicker")

        self.window_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

        self.background = pygame.Surface((WINDOW_WIDTH, WINDOW_HEIGHT))
        self.background.fill(pygame.Color("#111111"))

        self.manager = pygame_gui.UIManager((WINDOW_WIDTH, WINDOW_HEIGHT))

        # Define button size and position variables

        OUTER_BORDER_WIDTH = 10
        BUTTON_PADDING = 20

        BUTTON_WIDTH = WINDOW_WIDTH // 6 - OUTER_BORDER_WIDTH * 2
        BUTTON_HEIGHT = WINDOW_HEIGHT // 12 - OUTER_BORDER_WIDTH * 2

        BUTTON_ROW_1_Y_POS = WINDOW_HEIGHT - BUTTON_HEIGHT - OUTER_BORDER_WIDTH
        BUTTON_ROW_2_Y_POS = BUTTON_ROW_1_Y_POS - BUTTON_HEIGHT - BUTTON_PADDING

        PLAYER_MONEY_LABEL_WIDTH = 200
        PLAYER_MONEY_LABEL_HEIGHT = 75

        # Define Main Stored Game Variables; these are the variables that are saved to the game save file

        self.PLAYER_STARTING_MONEY = 50
        self.player_money = self.PLAYER_STARTING_MONEY
        self.player_level = 1
        self.level_up_cost = 50

        self.constant_money_increase = 0.25  # This is the amount of money that is added to the player's money every tick no matter what

        self.total_money_per_tick = self.constant_money_increase

        self.player_level_label = pygame_gui.elements.UILabel(
            relative_rect=pygame.Rect(
                (
                    OUTER_BORDER_WIDTH,
                    OUTER_BORDER_WIDTH,
                ),
                (PLAYER_MONEY_LABEL_WIDTH, PLAYER_MONEY_LABEL_HEIGHT),
            ),
            text=f"Multiplier: {self.player_level}",
            manager=self.manager,
        )

        self.player_money_label = pygame_gui.elements.UILabel(
            relative_rect=pygame.Rect(
                (
                    WINDOW_WIDTH // 2 - (PLAYER_MONEY_LABEL_WIDTH // 2),
                    OUTER_BORDER_WIDTH,
                ),
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

        self.player_level_up_button = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect(
                (
                    WINDOW_WIDTH // 2 - (PLAYER_MONEY_LABEL_WIDTH // 2),
                    OUTER_BORDER_WIDTH + PLAYER_MONEY_LABEL_HEIGHT + BUTTON_PADDING,
                ),
                (200, 100),
            ),
            text=f"Level Up: -${self.level_up_cost}",
            manager=self.manager,
        )

        # Prices to purchase one of each item
        self.ITEM_1_PRICE = 20
        self.ITEM_2_PRICE = 100
        self.ITEM_3_PRICE = 500
        self.ITEM_4_PRICE = 2000
        self.ITEM_5_PRICE = 5000
        self.ITEM_6_PRICE = 12000
        self.ITEM_7_PRICE = 20000
        self.ITEM_8_PRICE = 50000
        self.ITEM_9_PRICE = 100000
        self.ITEM_10_PRICE = 200000
        self.ITEM_11_PRICE = 500000
        self.ITEM_12_PRICE = 1000000

        # Amount of each item that the player has
        self.ITEM_1_QUANTITY = 0
        self.ITEM_2_QUANTITY = 0
        self.ITEM_3_QUANTITY = 0
        self.ITEM_4_QUANTITY = 0
        self.ITEM_5_QUANTITY = 0
        self.ITEM_6_QUANTITY = 0
        self.ITEM_7_QUANTITY = 0
        self.ITEM_8_QUANTITY = 0
        self.ITEM_9_QUANTITY = 0
        self.ITEM_10_QUANTITY = 0
        self.ITEM_11_QUANTITY = 0
        self.ITEM_12_QUANTITY = 0

        # Item Values Added to Player's Money (Multiplied by Quantity)
        self.ITEM_1_VALUE = 0.25
        self.ITEM_2_VALUE = 1
        self.ITEM_3_VALUE = 2
        self.ITEM_4_VALUE = 4
        self.ITEM_5_VALUE = 6
        self.ITEM_6_VALUE = 12
        self.ITEM_7_VALUE = 25
        self.ITEM_8_VALUE = 100
        self.ITEM_9_VALUE = 250
        self.ITEM_10_VALUE = 500
        self.ITEM_11_VALUE = 750
        self.ITEM_12_VALUE = 1000

        # Create a UI element for each item in the shop
        self.buy_item_1_button = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect(
                (OUTER_BORDER_WIDTH, BUTTON_ROW_1_Y_POS),
                (BUTTON_WIDTH, BUTTON_HEIGHT),
            ),
            text=f"${self.ITEM_1_PRICE}: +{self.ITEM_1_VALUE}",
            manager=self.manager,
        )

        self.buy_item_2_button = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect(
                (
                    OUTER_BORDER_WIDTH + BUTTON_PADDING + BUTTON_WIDTH,
                    BUTTON_ROW_1_Y_POS,
                ),
                (BUTTON_WIDTH, BUTTON_HEIGHT),
            ),
            text=f"${self.ITEM_2_PRICE}: +{self.ITEM_2_VALUE}",
            manager=self.manager,
        )

        self.buy_item_3_button = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect(
                (
                    OUTER_BORDER_WIDTH + (BUTTON_PADDING * 2) + (BUTTON_WIDTH * 2),
                    BUTTON_ROW_1_Y_POS,
                ),
                (BUTTON_WIDTH, BUTTON_HEIGHT),
            ),
            text=f"${self.ITEM_3_PRICE}: +{self.ITEM_3_VALUE}",
            manager=self.manager,
        )

        self.buy_item_4_button = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect(
                (
                    OUTER_BORDER_WIDTH + (BUTTON_PADDING * 3) + (BUTTON_WIDTH * 3),
                    BUTTON_ROW_1_Y_POS,
                ),
                (BUTTON_WIDTH, BUTTON_HEIGHT),
            ),
            text=f"${self.ITEM_4_PRICE}: +{self.ITEM_4_VALUE}",
            manager=self.manager,
        )

        self.buy_item_5_button = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect(
                (
                    OUTER_BORDER_WIDTH + (BUTTON_PADDING * 4) + (BUTTON_WIDTH * 4),
                    BUTTON_ROW_1_Y_POS,
                ),
                (BUTTON_WIDTH, BUTTON_HEIGHT),
            ),
            text=f"${self.ITEM_5_PRICE}: +{self.ITEM_5_VALUE}",
            manager=self.manager,
        )

        self.buy_item_6_button = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect(
                (
                    OUTER_BORDER_WIDTH + (BUTTON_PADDING * 5) + (BUTTON_WIDTH * 5),
                    BUTTON_ROW_1_Y_POS,
                ),
                (BUTTON_WIDTH, BUTTON_HEIGHT),
            ),
            text=f"${self.ITEM_6_PRICE}: +{self.ITEM_6_VALUE}",
            manager=self.manager,
        )

        self.buy_item_7_button = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect(
                (OUTER_BORDER_WIDTH, BUTTON_ROW_2_Y_POS),
                (BUTTON_WIDTH, BUTTON_HEIGHT),
            ),
            text=f"${self.ITEM_7_PRICE}: +{self.ITEM_7_VALUE}",
            manager=self.manager,
            visible=False,
        )

        self.buy_item_8_button = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect(
                (
                    OUTER_BORDER_WIDTH + BUTTON_PADDING + BUTTON_WIDTH,
                    BUTTON_ROW_2_Y_POS,
                ),
                (BUTTON_WIDTH, BUTTON_HEIGHT),
            ),
            text=f"${self.ITEM_8_PRICE}: +{self.ITEM_8_VALUE}",
            manager=self.manager,
            visible=False,
        )

        self.buy_item_9_button = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect(
                (
                    OUTER_BORDER_WIDTH + (BUTTON_PADDING * 2) + (BUTTON_WIDTH * 2),
                    BUTTON_ROW_2_Y_POS,
                ),
                (BUTTON_WIDTH, BUTTON_HEIGHT),
            ),
            text=f"${self.ITEM_9_PRICE}: +{self.ITEM_9_VALUE}",
            manager=self.manager,
            visible=False,
        )

        self.buy_item_10_button = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect(
                (
                    OUTER_BORDER_WIDTH + (BUTTON_PADDING * 3) + (BUTTON_WIDTH * 3),
                    BUTTON_ROW_2_Y_POS,
                ),
                (BUTTON_WIDTH, BUTTON_HEIGHT),
            ),
            text=f"${self.ITEM_10_PRICE}: +{self.ITEM_10_VALUE}",
            manager=self.manager,
            visible=False,
        )

        self.buy_item_11_button = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect(
                (
                    OUTER_BORDER_WIDTH + (BUTTON_PADDING * 4) + (BUTTON_WIDTH * 4),
                    BUTTON_ROW_2_Y_POS,
                ),
                (BUTTON_WIDTH, BUTTON_HEIGHT),
            ),
            text=f"${self.ITEM_11_PRICE}: +{self.ITEM_11_VALUE}",
            manager=self.manager,
            visible=False,
        )

        self.buy_item_12_button = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect(
                (
                    OUTER_BORDER_WIDTH + (BUTTON_PADDING * 5) + (BUTTON_WIDTH * 5),
                    BUTTON_ROW_2_Y_POS,
                ),
                (BUTTON_WIDTH, BUTTON_HEIGHT),
            ),
            text=f"${self.ITEM_12_PRICE}: +{self.ITEM_12_VALUE}",
            manager=self.manager,
            visible=False,
        )

        # Buttons 7 - 12 are only visible if the player has leveled enough to buy them

        self.main()

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
        self.player_money -= self.level_up_cost
        self.total_money_per_tick * 1.5
        self.level_up_cost *= 2.5

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

    def check_affordable(self):
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
            self.player_level_up_button.enable()
        else:
            self.player_level_up_button.disable()

        if self.player_level >= 5:
            self.buy_item_4_button.enable()
            self.buy_item_5_button.enable()
            self.buy_item_6_button.enable()
        if self.player_level >= 10:
            self.buy_item_7_button.enable()
            self.buy_item_8_button.enable()
            self.buy_item_9_button.enable()
        if self.player_level >= 15:
            self.buy_item_10_button.enable()
            self.buy_item_11_button.enable()
            self.buy_item_12_button.enable()

    def add_money(self):
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

        self.player_money * self.player_level

        self.player_money_label.set_text(f"Player Money: {self.player_money}")
        self.money_increase_label.set_text(f"(+{self.total_money_per_tick} per tick)")

    def check_events(self, event):
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

    def main(self):

        fps = 10

        clock = pygame.time.Clock()

        is_running = True

        while is_running:

            time_delta = clock.tick(fps) / 1000.0

            self.check_affordable()
            self.check_player_level()
            self.add_money()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    is_running = False

                if event.type == pygame_gui.UI_BUTTON_PRESSED:

                    self.check_events(event)

                self.manager.process_events(event)

            self.manager.update(time_delta)

            self.window_surface.blit(self.background, (0, 0))
            self.manager.draw_ui(self.window_surface)

            pygame.display.update()


if __name__ == "__main__":
    IdleGame()
