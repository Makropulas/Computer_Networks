# Шифрование и дешифрование алгоритмом Цезаря (в двух реализациях)

def encrypt(text, shift=17):
    result = ""
    for char in text:
        if char.isalpha():
            # Определяем базу для сдвига в зависимости от регистра буквы (A для больших, a для маленьких)
            base = ord('A') if char.isupper() else ord('a')
            # Применяем сдвиг и учитываем, что алфавит круглый (после 'Z' идет 'A', после 'z' идет 'a')
            shifted_char = chr(((ord(char) - base + shift) % 26) + base)
            result += shifted_char
        else:
            # Если символ не является буквой, оставляем его неизменным
            result += char
    return result

def decrypt(text, shift=17):
    result = ""
    for char in text:
        if char.isalpha():
            base = ('a', 'A')[char.isupper()]
            shifted_char = chr(ord(base) + (ord(char) - shift - ord(base)) % 26)
            result += shifted_char
        else:
            result += char
    return result