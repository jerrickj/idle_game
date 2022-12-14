# Define button size and position variables
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 60
OUTER_BORDER_WIDTH = 10
BUTTON_PADDING = 1
ITEM_BUTTON_WIDTH = WINDOW_WIDTH // 7
ITEM_BUTTON_HEIGHT = WINDOW_HEIGHT // 1
BUTTON_ROW_1_Y_POS = WINDOW_HEIGHT - ITEM_BUTTON_HEIGHT - OUTER_BORDER_WIDTH
BUTTON_ROW_2_Y_POS = BUTTON_ROW_1_Y_POS - ITEM_BUTTON_HEIGHT - BUTTON_PADDING
PLAYER_MONEY_LABEL_WIDTH = 200
PLAYER_MONEY_LABEL_HEIGHT = 7
PLAYER_MONEY_LABEL_X_POS = (
    (WINDOW_WIDTH // 2) - (PLAYER_MONEY_LABEL_WIDTH // 2) - (OUTER_BORDER_WIDTH // 2)
)
PLAYER_MONEY_LABEL_Y_POS = OUTER_BORDER_WIDTH
FUNCTION_BUTTON_WIDTH = 200
FUNCTION_BUTTON_HEIGHT = 75
