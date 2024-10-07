from selenium.webdriver.common.by import By


# локаторы для главной страницы
class MainLocators:
    LOGIN_TO_ACCOUNT_BUTTON = (By.XPATH, "//button[text()='Войти в аккаунт']")
    ORDER_BUTTON = (By.XPATH, "//button[text()='Оформить заказ']")
    PERSONAL_ACCOUNT = (By.XPATH, "//p[text()='Личный Кабинет']")
    CONSTRUCTOR_BUTTON = (By.XPATH, "//p[text()='Конструктор']")
    ASSEMBLE_BURGER_TITLE = (By.XPATH, "//h1[text()='Соберите бургер']")
    ORDER_FEED_BUTTON = (By.XPATH, "//p[text()='Лента Заказов']")
    ORDER_FEED_TITLE = (By.XPATH, "//h1[text()='Лента Заказов']")
    BURGER_INGREDIENT_BUN = (By.XPATH, "//img[@alt='Флюоресцентная булка R2-D3']")
    BURGER_INGREDIENT_SOUSES = (By.XPATH, "//img[@alt='Соус Spicy-X']")
    POPUP_INGREDIENT_DETAILS_WINDOW = (By.XPATH, "//h2[contains(@class, Modal_modal__title_modified)]"
                                                 "[text()='Детали ингредиента']")
    CLOSE_BUTTON = (By.XPATH, "//button[contains(@class, 'Modal_modal__close')]")
    BURGER_CONSTRUCTOR_BASKET = (By.XPATH, "//ul[contains(@class, 'BurgerConstructor_basket__list')]")
    COUNTER_BUN = (By.XPATH, f"(//p[contains(@class, 'counter_counter__num')])[0]")
    POPUP_ORDER_ID_WINDOW = (By.XPATH, "//div[contains(@class, 'Modal_modal__container')]")
    ORDER_ID_TITLE = (By.XPATH, "//h2[contains(@class, 'Modal_modal__title_shadow')]")
