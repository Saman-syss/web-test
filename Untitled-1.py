# def print_formatted(number):
#     # your code goes here
#     width = len(bin(number)[2:])
#     for i in range(1, number+1):
#         print(str(i).rjust(width), oct(i)[2:].rjust(width), hex(i)[2:].upper().rjust(width), bin(i)[2:].rjust(width))

# def print_formatted(number):
#     width = len(bin(number)[2:])
#     for i in range(1,number+1):
#         decimal = i
#         octal = oct(i)[2:].rjust(width)
#         hexa = hex(i)[2:]
#         hexa_cap = hexa.upper().rjust(width)
#         binary = bin(i)[2:].rjust(width)
#         print(decimal,octal,hexa_cap,binary)


n = 3
for i in range(n+1,1):
    print("A")