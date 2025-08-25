a = float(input('Enter price: '))
b = float(input('Enter discount percentage: '))
def calculate_discount(price, discount_percent):
    return price * discount_percent / 100
if b >= 20:
    result = calculate_discount(a, b)    
    originalp = a - result
    print('Original Price: ', originalp)
else :
    print(a)
