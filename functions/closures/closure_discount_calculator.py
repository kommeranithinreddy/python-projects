def discount(percentage):
    def dis_calculator(total):
        return (total/100)*(100-percentage)
    return dis_calculator

discount_10 = discount(10)
print(discount_10(1000))
print(discount_10(200))
print(discount_10(50))