# Принцип единой ответственности
class Journal:
    def __init__(self) -> None:
        self.entries = []
        self.count = 0

    def add_entry(self, text: str) -> None:
        self.count += 1
        self.entries.append(f'{self.count}: {text}')

    def remove_entry(self, pos: int) -> None:
        del self.entries[pos]

    def __str__(self) -> str:
        return '\n'.join(self.entries)

    # Нарушение принципа единой ответственности, вводим еще и сохранение
    # def save(self, filename):
    #     file = open(filename, 'w')
    #     file.write(str(self))
    #     file.close()
    
    # def load(self, filename):
    #     pass

    # def low_from_web(self, url):
    #     pass

class PersistanceManager:
    @staticmethod
    def save_to_file(journal, filename):
        file = open(filename, 'w')
        file.write(str(journal))
        file.close()


j = Journal()
j.add_entry('Сходить в магазин')
j.add_entry('Выгулить собаку')
print(j)