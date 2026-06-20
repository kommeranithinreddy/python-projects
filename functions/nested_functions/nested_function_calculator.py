def outer_calculator(inp1, inp2, operation):
    def add(num1, num2):
        return num1 + num2
    def sub(num1, num2):
        return num1 - num2
    def mul(num1, num2):
        return num1 * num2
    def div(num1, num2):
        return num1 / num2
    match operation:
        case 'add':
            result = add(inp1, inp2)
        case 'sub':
            result = sub(inp1, inp2)
        case 'mul':
            result = mul(inp1, inp2)
        case 'div':
            result = div(inp1, inp2)
        case _ :
            result = f'{operation} input is invalid'
    return result

print(outer_calculator(1,2, 'div'))