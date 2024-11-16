from src.logic1 import calculate_taxes

def calculate_discont(price:list[float], tax:float, disc:float = 0, long_of_price:int = 2)->list[float]:
    actual_price = calculate_taxes(price,tax)
    price_after_discont = [round(x*(1-disc/100),long_of_price) for x in actual_price]
    return price_after_discont