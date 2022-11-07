# pattern = "1111100000011011111001000100101011101100110010";

# listnew = []
# for i in pattern:
#     if len(pattern) < 8:
#         no_zeros = 8 - len(pattern)
#         print(no_zeros)
#         pattern.join(['0']*no_zeros)
#         listnew.append(pattern)
#         break
#     else:
#         listnew.append(pattern[:8])
#         pattern = pattern[8:]

# print("\n-----after adding zeroes------")
# print(listnew)

binary_string = "1010"

decimal_representation = int(binary_string, 2)
hexadecimal_string = hex(decimal_representation)

print(hexadecimal_string)