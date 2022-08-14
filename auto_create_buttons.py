        for index, item in enumerate(self.items):
            name, price, value, quantity = item[0], item[1], item[2], item[3]
            print(name, price, value, quantity)
            if index <= 6:
                x_pos = OUTER_BORDER_WIDTH + (ITEM_BUTTON_WIDTH * index + 1)
                y_pos = OUTER_BORDER_WIDTH + (ITEM_BUTTON_HEIGHT)

            if index > 6:
                x_pos = OUTER_BORDER_WIDTH + (ITEM_BUTTON_WIDTH * index + 1)
                y_pos = WINDOW_HEIGHT - (
                    ((ITEM_BUTTON_HEIGHT * 2) + BUTTON_PADDING) * (index + 1)
                )

            self.CreateItemButton(
                self.manager,
                name,
                price,
                value,
                x_pos,
                y_pos,
                ITEM_BUTTON_WIDTH,
                ITEM_BUTTON_HEIGHT,
            )

        # self.CreateItemButton(
        #    self.manager,
        #    "Item 1",
        #    self.ITEM_1_PRICE,
        #    self.ITEM_1_VALUE,
        #    500,
        #    500,
        #    ITEM_BUTTON_WIDTH,
        #    ITEM_BUTTON_HEIGHT,
        # )

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