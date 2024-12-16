import doctest

class Book:
    def __init__(self, title: str, author: str) -> None:
        """
        Инициализация книги с названием и автором.

        :param title: Название книги 
        :param author: Автор книги 
        :raises ValueError: Если название или автор не строки.
        """
        if not isinstance(title, str) or not isinstance(author, str):
            raise ValueError("Название и автор книги должны быть строками.")
        
        self.title = title
        self.author = author

    def read(self) -> str:
        """
        Прочитать книгу.

        :return: Строка, описывающая процесс чтения книги.
        :rtype: str
        :raises NotImplementedError: Этот метод должен быть реализован в подклассе.

        >>> book = Book('1984', 'Джордж Оруэлл')
        >>> book.read()
        'Чтение книги "1984" Джорджа Оруэлла'
        """
        pass

    def bookmark_page(self, page_number: int) -> str:
        """
        Отметить страницу книги для продолжения чтения.

        :param page_number: Номер страницы для закладки.
        :return: Строка с описанием действия.
        :rtype: str
        :raises ValueError: Если номер страницы меньше 1.

        >>> book = Book('1984', 'Джордж Оруэлл')
        >>> book.bookmark_page(150)
        'Страница 150 закладка книги "1984" Джорджа Оруэлла'
        """
        if page_number < 1:
            raise ValueError("Номер страницы должен быть больше 0.")
        pass

if __name__ == "__main__":
    doctest.testmod()  # тестирование примеров, которые находятся в документации