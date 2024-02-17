class AnimalRegistry:
    def __init__(self):
        self.animals = []
        self.counter = Counter()

    def add_animal(self, animal):
        self.animals.append(animal)
        self.counter.add()

    def classify_animal(self, animal):
        # Ваш код для определения класса животного
        pass

    def list_commands(self, animal):
        # Ваш код для вывода списка команд животного
        pass

    def train_animal(self, animal, new_commands):
        # Ваш код для обучения животного новым командам
        pass


class Counter:
    def __init__(self):
        self.value = 0

    def add(self):
        self.value += 1

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type is None and self.value > 0:
            print("Resource closed properly")
        elif exc_type is not None:
            print("Exception occurred")
        else:
            print("Resource not closed properly")


# Пример использования
def main():
    registry = AnimalRegistry()

    with Counter() as counter:
        try:
            # Предполагается, что пользователь вводит данные для создания животного
            animal = input("Enter animal details: ")
            registry.add_animal(animal)
        except Exception as e:
            print("Error:", e)


if __name__ == "__main__":
    main()
