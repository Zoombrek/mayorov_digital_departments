import doctest

class Computer:
    def __init__(self, model: str, operating_system: str) -> None:
        """
        Инициализация компьютера с моделью и операционной системой.

        :param model: Модель компьютера
        :param operating_system: Операционная система
        :raises ValueError: Если модель или операционная система не строка.
        :raises ValueError: Если операционная система не поддерживается.
        """
        if not isinstance(model, str) or not isinstance(operating_system, str):
            raise ValueError("Модель и операционная система должны быть строками.")
        
        self.model = model
        self.operating_system = operating_system
        
        # Проверка поддерживаемых операционных систем
        supported_os = ['Windows', 'macOS', 'Linux']
        if operating_system not in supported_os:
            raise ValueError(f"Операционная система '{operating_system}' не поддерживается.")


    def power_on(self) -> str:
        """
        Включить компьютер.

        :return: Строка, описывающая процесс включения компьютера.
        :rtype: str
        :raises NotImplementedError: Этот метод должен быть реализован в подклассе.

        >>> computer = Computer('MacBook Pro', 'macOS')
        >>> computer.power_on()
        'Включение MacBook Pro с macOS'
        """
        pass


    def shutdown(self) -> str:
        """
        Выключить компьютер.

        :return: Строка, описывающая процесс выключения компьютера.
        :rtype: str
        :raises NotImplementedError: Этот метод должен быть реализован в подклассе.

        >>> computer = Computer('MacBook Pro', 'macOS')
        >>> computer.shutdown()
        'Выключение MacBook Pro с macOS'
        """
        pass

if __name__ == "__main__":
    doctest.testmod()  # тестирование примеров, которые находятся в документации