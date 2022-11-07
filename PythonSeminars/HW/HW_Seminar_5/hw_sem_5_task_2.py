# Задача 2. Реализуйте RLE алгоритм: 
# реализуйте модуль сжатия и восстановления данных 
# (здесь только буквы).

def rle_encode(data):
    encoding = ''
    prev_char = '' 
    count = ''
   
    if not data: return 'Нет исходных данных.'
    
    for char in data:
        if char != prev_char: 
            encoding += str(count) + prev_char
            count = 1 
            prev_char = char
        else: 
            count += 1 
    else:
        encoding += str(count) + prev_char
                
    with open ('rle_encoding_out.txt', 'w') as file:
        file.write(encoding)
            
    return encoding

with open('rle_encoding_in.txt', 'r') as file:
    rle_in = file.read()
    print(f'\nИсходный текст: {rle_in}')
       
print(f'Сжатый RLE текст: {rle_encode(rle_in)}')

def rle_decode(data): 
    decode = '' 
    count = '' 
    for char in data:
        if char.isdigit():
            count += char
        else: 
            decode += char * int(count)
            count = ''
            
            with open('rle_decoding_out.txt', 'w') as file:
                file.write(decode)
    return decode

with open('rle_encoding_out.txt', 'r') as file:
    rle_decoding_in = file.read()
    print(f'\nИсходный сжатый RLE текст: {rle_decoding_in}')
  
print(f'Восстановленный RLE текст: {rle_decode(rle_decoding_in)}\n')


