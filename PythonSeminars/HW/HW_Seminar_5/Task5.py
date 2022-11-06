 # import re

# result = re.match(r'AV', 'AV Analytics Vidhya AV')
# print(result.group(0))

# result = re.match(r'AV', 'AV Analytics Vidhya AV')
# print (result.start())
# print (result.end())


# 5 - Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных. 
# Входные и выходные данные хранятся в отдельных текстовых файлах.
# файл первый:
# AAAAAAAAAAAABBBBBBBBBBBCCCCCCCCCCDDDDDDEEEEEFFFFG python is sooooooo coooooool
# файл второй:
# сжатый текст.

def rle_encode(data):
    encoding = '' 
    prev_char = '' 
    count = 1 

    if not data: return ''

    for char in data:
        # If the prev and current characters don't match... 
        if char != prev_char: 
        # ...then add the count and character to our encoding 
            if prev_char: 
                encoding += str(count) + prev_char 
            count = 1 
            prev_char = char 
        else: 
            # Or increment our counter if the characters do match 
            count += 1 
    else: 
        # Finish off the encoding 
        encoding += str(count) + prev_char 
        return encoding
encoded_val = rle_encode('AAAAAAFDDCCCCCCCAEEEEEEEEEEEEEEEEE')
print(encoded_val)


data = 'AAAAAAFDDCCCCCCCAEEEEEEEEEEEEEEEEE'
fir = data[0]
count = 1
for fur in data:
    if fur != fir:
        count = 1
    if fur == fir:
        count +=1
        print(count)
    else:
        fur = data[]
    else:
print(fir + str(count))

print(fir)


def rle_encode(data):
    encoding = '' 
    prev_char = '' 
    count = 1

    if not data: return ''

    for char in data:
        if char != prev_char: 
            if prev_char: 
                encoding += str(count) + prev_char 
            count = 1
            prev_char = char 
        else: 
            count += 1 
    else: 
        encoding += str(count) + prev_char 
        return encoding
    
encoded_val = rle_encode('AAAAAAFDDCCCCCCCAEEEEEEEEEEEEEEEEE')
print(encoded_val)