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
                
    # path_out = 'C:/GB/Python_GB/PythonSeminars/HW/HW_Seminar_5/rle_encoding_out.txt'
    with open ('rle_encoding_out.txtpath_out', 'w') as file:
        file.write(encoding)
            
    return encoding

# path = 'C:/GB/Python_GB/PythonSeminars/HW/HW_Seminar_5/rle_encoding_in.txt'
with open('rle_encoding_in.txt', 'r') as file:
    rle_in = file.read()
    print(f'Исходный текст: {rle_in}')
       
print(f'Текст сжатый RLE: {rle_encode(rle_in)}')

# def rle_decode(data): 
#     decode = '' 
#     count = '' 
#     for char in data:
#         if char.isdigit():
#             count += char
#         else: 
#             decode += char * int(count)
#             count = ''
            
#             # path = 'C:/GB/Python_GB/PythonSeminars/HW/HW_Seminar_5/rle_decoding_out.txt'
#             with open('rle_decoding_out.txt', 'w') as file:
#                 file.write(decode)
#     return decode

# # path = 'C:/GB/Python_GB/PythonSeminars/HW/HW_Seminar_5/rle_encoding_out.txt'
# with open('rle_encoding_out.txt', 'r') as file:
#     rle_decoding_in = file.read()
#     print(f'\nИсходный текст сжатый RLE: {rle_decoding_in}')
  
# print(f'Текст RLE восстановленный: {rle_decode(rle_decoding_in)}')
