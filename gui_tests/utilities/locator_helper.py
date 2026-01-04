from selenium.webdriver.common.by import By


class LocatorHelper:
    """Helper for building robust locators."""

    @staticmethod
    def by_data_test(value) -> tuple[str, str]:
        """
        Create locator using data-test attribute.

        Example:
            ADD_BUTTON = LocatorHelper.by_data_test("add-to-cart-sauce-labs-bolt-t-shirt")
        """
        return By.CSS_SELECTOR, f'[data-test="{value}"]'

    @staticmethod
    def by_partial_data_test(partial_value) -> tuple[str, str]:
        """
        Find element by partial data-test match.

        Example:
            ALL_ADD_BUTTONS = LocatorHelper.by_partial_data_test("add-to-cart")
        """
        return By.CSS_SELECTOR, f'[data-test*="{partial_value}"]'

    @staticmethod
    def by_id(element_id: str) -> tuple[str, str]:
        """
        Create locator by ID.

        Args:
            element_id: Element ID

        """
        return By.ID, element_id

    @staticmethod
    def by_class(class_name: str) -> tuple[str, str]:
        """
        Create locator by class name.

        Args:
            class_name: CSS class name
        """
        return By.CLASS_NAME, class_name

