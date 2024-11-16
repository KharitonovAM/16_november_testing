from src.logic1 import calculate_taxes

def calculate_discont(price:list[float], tax:float, disc:float)->list[float]:
    actual_price = calculate_taxes(price,tax)
    price_after_discont = [x*(1-disc/100) for x in actual_price]
    return price_after_discont