class CaesarsCipher:

    def __init__(self) -> None:
        """Инициализация работы со своим алфавитом."""
        self.__alphabet: str = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcde" \
                          "fghijklmnopqrstuvwxyz1234567890 !?."

    def decrypt(self, target: str) -> dict[int:str]:
        """Расшифровка строки брутфорсом.

        Args:
            target: расшифровываемая строка.

        Returns:
            Словарь вариантов расшифровки с соотв ключём.
        """
        out: dict[int:str] = {}
        check_len: int = len(self.__alphabet)
        for key in range(0, check_len):
            result: str = ""
            for i in range(0, len(target)):
                index = self.__alphabet.find(target[i])
                result += self.__alphabet[index - key]
            out[key] = result
        return out

    def encrypt(self, target: str) -> dict[int:str]:
        """Все варианты шифра в данном алфавите.

        Args:
            target: шифруемая строка.

        Returns:
            Словарь всех вариантов и использованных ключей
        """
        out: dict[int:str] = {}
        check_len: int = len(self.__alphabet)
        for key in range(0, check_len):
            result = ""
            for i in range(0, len(target)):
                index = self.__alphabet.find(target[i])
                if (index + key) < check_len:
                    result += self.__alphabet[index + key]
                else:
                    result += self.__alphabet[index + key - check_len]
            out[key] = result
        return out


# Пример работы класса
if __name__ == "__main__":

    caesar = CaesarsCipher()

    tries = caesar.decrypt("o3zR v..D0?yRA0R8FR8v47w0ER4.R1WdC!sLF5D")
    for k, v in tries.items():
        print(f'{k}: {v}')

    codes = caesar.encrypt("o3zR v..D0?yRA0R8FR8v47w0ER4.R1WdC!sLF5D")
    for k, v in codes.items():
        print(f'{k}: {v}')
