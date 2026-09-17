def calculate_shipping(jeans: int, shoes: int, sunglasses: int, warehouse_ready: bool = True):
    """
    Calculates shipping quantities if the warehouse is ready.
    """
    if not warehouse_ready:
        return "Warehouse is not ready. Try a different warehouse."

    # Directly return the quantities if the warehouse is available
    return jeans, shoes, sunglasses
