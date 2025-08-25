a = float(50000)
b = float(25)
def calculate_discount(price, discount_percent):
    return price * discount_percent / 100
if b >= 20:
    result = calculate_discount(a, b)    
    originalp = a - result
    print('Dicounted Price: ', originalp)
else :
    print('Original Price', a)
