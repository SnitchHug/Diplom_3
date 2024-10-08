from selenium.webdriver.common.by import By


# локаторы для страницы Лента заказов
class FeedLocators:
    # Локатор для кнопки "Конструктор" в хеддере
    CONSTRUCTOR_BUTTON = (By.XPATH, "//p[text()='Конструктор']")

    PERSONAL_ACCOUNT = (By.XPATH, "//p[text()='Личный Кабинет']")

    # Локатор для поиска элемента заказа в ленте заказов по ID
    ORDER_FEED_ITEM_BY_ID = (By.XPATH,
                             "//p[contains(@class, 'text_type_digits-default') and contains(text(), '{order_id}')]")

    # Локатор для всплывающего окна с деталями заказа
    POPUP_ORDER_DETAILS_WINDOW = (By.XPATH, "//div[contains(@class, 'Modal_modal__container')]")

    # Локатор для списка заказов "В работе"
    ORDER_READY_LIST = (By.XPATH, "//ul[contains(@class, 'OrderFeed_orderListReady')]")

    # Локатор для ID заказа, содержащегося в списке заказов "В работе"
    ORDER_READY_ID = (By.XPATH, "//ul[contains(@class, 'OrderFeed_orderListReady')]"
                                "//li[contains(@class,'text_type_digits-default')]")

    # Локатор для счётчика "Выполнено за все время"
    ORDER_COUNTER_ALL_TIME = (By.XPATH, "//p[text()='Выполнено за все время:']"
                                        "/following-sibling::p[contains(@class, 'OrderFeed_number')]")

    # Локатор для счётчика "Выполнено за сегодня"
    ORDER_COUNTER_TODAY = (By.XPATH, "//p[text()='Выполнено за сегодня:']"
                                     "/following-sibling::p[contains(@class, 'OrderFeed_number')]")

    # Локатор последнего выполненного заказа в истории заказов
    LAST_ORDER_IN_HISTORY = (By.XPATH, f"(//p[contains(@class, 'text_type_digits-default')])[last()]")
