import random

# Обозначаются наборы всех символов, которые могут быть зашифрованы в данной программе
russian_alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
numbers = '1234567890'
special_symbols = " ,."
chars = list(russian_alphabet + numbers + special_symbols)
# Размер исходного алфавита
# (вычитание единицы связано с началом индексации массива с нуля)
N = len(chars) - 1


# Функция генерации гаммы для заданного текста
def generate_gamma(text):
    g = ''.join(random.choice(chars) for i in range(len(text)))
    return g


# Функция шифрования
def encode(text, gamma):
    encoded_text = ""
    for i in range(len(text)):
        # Если пользователь ввел символ, не обозначенные ранее - возвращается ошибка
        if text[i] not in chars:
            message = f"Вы ввели символ '{text[i]}', который невозможно закодировать данной программой!"
            raise Exception(message)
        # Считается порядковый номер в алфавите для каждого символа из текста и гаммы
        index_text = chars.index(text[i])
        index_gamma = chars.index(gamma[i])
        # Номера суммируются
        sum_index = index_text + index_gamma
        # Берется остаток от деления суммы номеров на размер алфавита
        left = sum_index % N
        # Если остаток равняется нулю - его следует заменить на размер алфавита
        if left == 0:
            left = N
        # Выбирается зашифрованный символ и добавляется к зашифрованному тексту
        encoded_char = chars[left]
        encoded_text += encoded_char
    return encoded_text


def decode(encoded_text, gamma):
    text = ""
    for i in range(len(encoded_text)):
        # Если данную фенкцию применить для текста, который был зашифрован с пмощью другой гаммы, то она будет
        # некорректно работать. Поэтому необходимо вернуть ошибку, информирующую пользователя об этом
        if encoded_text[i] not in chars:
            raise Exception("Шифрование производилось с использованием другого ключа (гаммы)")
        # Считается порядковый номер в алфавите для каждого символа из зашифрованного текста и гаммы
        index_text = chars.index(encoded_text[i])
        index_gamma = chars.index(gamma[i])
        # Номера суммируются вместе с размеров алфавита
        sum_index = index_text - index_gamma + N
        # Берется остаток от деления суммы номеров и размера алфавита на размер алфавита
        left = sum_index % N
        # Если остаток равер размеру алфавита - его следует заменить на ноль
        if left == N:
            left = 0
        # Выбирается расшифрованный символ и добавляется к расшифрованному тексту
        decoded_char = chars[left]
        text += decoded_char
    return text


# Главная функция
def main():
    # Пользовательский ввод
    raw_text = input("Введите исходный текст (только русский алфавит, цифры, пробелы и символы '.' и ','): ")
    # Текст приводится к нижнему регистру для упрощения работы
    raw_text = raw_text.lower()
    # Генерация гаммы
    gamma = generate_gamma(raw_text)
    print(f"Введенный текст:\n{raw_text}")
    print(f"Гамма:\n{gamma}")
    # Шифрование текста
    encoded_text = encode(raw_text, gamma)
    print(f"Зашифрованный текст:\n{encoded_text}")
    # Расшифровывание текста
    decoded_text = decode(encoded_text, gamma)
    print(f"Расшифрованный текст:\n{decoded_text}")


if __name__ == '__main__':
    main()
