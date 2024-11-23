import enchant
from enchant.tokenize import get_tokenizer


class CaesarsCipher:

    def __init__(self) -> None:
        """Инициализация работы со своим алфавитом."""
        self.__alphabet: str = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcde" \
                               "fghijklmnopqrstuvwxyz1234567890 !?."
        self.__key: int = 0

    def decrypt(self, target: str) -> dict[int:str]:
        """Расшифровка строки брутфорсом.

        Args:
            target: расшифровываемая строка.

        Returns:
            Словарь вариантов расшифровки с соотв ключём.
        """
        check_len: int = len(self.__alphabet)
        d = enchant.Dict("en_US")
        tokenizer = get_tokenizer("en_US")
        for key in range(0, check_len):
            result: str = ""
            for i in range(0, len(target)):
                index = self.__alphabet.find(target[i])
                result += self.__alphabet[index - key]
            tokenized_result = [w for w in tokenizer(result)]
            if d.check(tokenized_result[0][0]) and \
                    d.check(tokenized_result[1][0]):
                self.__key = key
                return {key: result}

    def encrypt(self, target: str) -> dict[int:str]:
        """Все варианты шифра в данном алфавите.

        Args:
            target: шифруемая строка.

        Returns:
            Словарь всех вариантов и использованных ключей
        """
        result: str = ''
        check_len: int = len(self.__alphabet)
        for i in range(0, len(target)):
            index = self.__alphabet.find(target[i])
            if (index + self.__key) < check_len:
                result += self.__alphabet[index + self.__key]
            else:
                result += self.__alphabet[index + self.__key - check_len]
        return {self.__key: result}


# Пример работы класса
if __name__ == "__main__":

    caesar = CaesarsCipher()

    tries = caesar.decrypt("o3zR v..D0?yRA0R8FR8v47w0ER4.R1WdC!sLF5D")
    for k, v in tries.items():
        print(f'{k}: {v}')

    codes = caesar.encrypt("The password to my mailbox is fBIvqX5yjw")
    for k, v in codes.items():
        print(f'{k}: {v}')

    # вывод в файл
