# Проект по реализации шифра Цезаря. Последняя правка 25.09.2023
# эту штуку мжно сделать как приложуху через tkinter
import string

def text_cipher(language, input_str, rot_n): # ввод на русском
    encrypted_str = '' # зашифрованная строка
    if language == 'ru':
        for i in input_str:
            if i in string.punctuation or i in ' ': # если пробел или знаки пунктуации, просто добавляем
                encrypted_str += i
                continue # если нет продолжаем


            ascii_sym = ord(i) + rot_n # номер по аски + число сдвига

            if i.isupper() and ascii_sym > 1071: # если верхний регистр и больше ord последнего символа
                encrypted_str += chr(ascii_sym - 32) # 32, потому что ё не учитывается
            elif i.islower() and ascii_sym > 1103: # если нижний регистр и больше ord последнего символа
                encrypted_str += chr(ascii_sym - 32)
            else:
                encrypted_str += chr(ascii_sym) # если в пределах круга

        return encrypted_str

    elif language == 'en':
        for i in input_str:
            if i in string.punctuation or i in ' ': # если пробел или знаки пунктуации, просто добавляем
                encrypted_str += i
                continue # если нет продолжаем


            ascii_sym = ord(i) + rot_n # номер по аски + число сдвига

            if i.isupper() and ascii_sym > 90: # если верхний регистр и больше ord последнего символа
                encrypted_str += chr(ascii_sym - 26)
            elif i.islower() and ascii_sym > 122: # если нижний регистр и больше ord последнего символа
                encrypted_str += chr(ascii_sym - 26)
            else:
                encrypted_str += chr(ascii_sym) # если в пределах круга

        return encrypted_str

    else:
        return print('Попробуйте ещё раз')



def text_decoding(language, input_str, rot_n): # функция дешифровки
    decod_str = '' # дешифрованная строка
    if language == 'ru':
        for i in input_str:
            if i in string.punctuation or i in ' ': # если пробел или знаки пунктуации, просто добавляем
                decod_str += i
                continue # если нет продолжаем


            ascii_subtraction = ord(i) - rot_n # номер по аски - число сдвига

            if i.isupper() and ascii_subtraction < 1040: # если верхний регистр и меньше ord последнего символа
                decod_str += chr(ascii_subtraction + 32) # 32, потому что ё не учитывается
            elif i.islower() and ascii_subtraction < 1072: # если нижний регистр и больше ord последнего символа
                decod_str += chr(ascii_subtraction + 32)
            else:
                decod_str += chr(ascii_subtraction) # если в пределах круга

        return decod_str

    elif language == 'en':
        for i in input_str:
            if i in string.punctuation or i in ' ': # если пробел или знаки пунктуации, просто добавляем
                decod_str += i
                continue # если нет продолжаем


            ascii_subtraction = ord(i) - rot_n # номер по аски + число сдвига

            if i.isupper() and ascii_subtraction < 65: # если верхний регистр и больше ord последнего символа
                decod_str += chr(ascii_subtraction + 26)
            elif i.islower() and ascii_subtraction < 97: # если нижний регистр и больше ord последнего символа
                decod_str += chr(ascii_subtraction + 26)
            else:
                decod_str += chr(ascii_subtraction) # если в пределах круга

        return decod_str

    else:
        return print('Попробуйте ещё раз')

# пользовательский ввод
print('Программа Шифр Цезаря'.center(100, '_'))
action = input('Если вы хотите зашифровать текст введите "шифрование" \nЕсли вы хотите расшифровать текст введите "расшифровка"\n')
language = input('Выберите язык шифрования: ru - русский, en - английский ')
input_str = input('Введите текст ')
rot_n = int(input('Ведите число сдвига(целое) '))

# этот кусок вообще не нравится, можно переделать
if action == 'шифрование':
    print(text_cipher(language, input_str, rot_n))
elif action == 'расшифровка':
    print(text_decoding(language, input_str, rot_n))
else:
    print('Недопустимое значение')


# package main # пардон за код на golang

# import "fmt"

# func main() {
# 	var num int
# 	fmt.Scan(&num)
# 	fmt.Println(num % 100)

# }
