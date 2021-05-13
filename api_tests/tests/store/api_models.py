from api_tests.core.set_client import ClientSession


class StoreInventory(ClientSession):
    """
    Path:   /v2/store/inventory
    """


class StoreOrder(ClientSession):
    """
    Path: /v2/store/<ORDER_ID>
    """
