import doctest

class SocialNetwork:
    def __init__(self, name: str, user_count: int) -> None:
        """
        Инициализация социальной сети с названием и количеством пользователей.

        :param name: Название социальной сети
        :param user_count: Количество пользователей.
        :raises ValueError: Если имя не строка или количество пользователей не целое число больше 0.
        """
        if not isinstance(name, str):
            raise ValueError("Название социальной сети должно быть строкой.")
        
        if not isinstance(user_count, int) or user_count <= 0:
            raise ValueError("Количество пользователей должно быть целым числом больше 0.")
        
        self.name = name
        self.user_count = user_count

    def post_message(self, message: str) -> str:
        """
        Опубликовать сообщение в социальной сети.

        :param message: Текст сообщения для публикации.
        :return: Строка, описывающая процесс публикации.
        :rtype: str
        :raises NotImplementedError: Этот метод должен быть реализован в подклассе.

        >>> social_network = SocialNetwork('VK', 1000000)
        >>> social_network.post_message('Привет, мир!')
        'Сообщение "Привет, мир!" опубликовано на VK'
        """
        pass

    def get_statistics(self) -> str:
        """
        Получить статистику о социальной сети.

        :return: Строка с описанием статистики.
        :rtype: str
        :raises NotImplementedError: Этот метод должен быть реализован в подклассе.

        >>> social_network = SocialNetwork('VK', 1000000)
        >>> social_network.get_statistics()
        'Facebook имеет 1000000 пользователей'
        """
        pass

if __name__ == "__main__":
    doctest.testmod()  # тестирование примеров, которые находятся в документации