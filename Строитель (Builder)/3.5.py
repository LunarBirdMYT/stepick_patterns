# Строители через наследование
class Person:
    def __init__(self) -> None:
        self.name = None
        self.position = None
        self.date_of_birth = None
    
    def __str__(self) -> str:
        return (f'{self.name} born on {self.date_of_birth} '
                f'works as {self.position}')
    
    @staticmethod
    def new():
        return PersonBuilder()
    
class PersonBuilder:
    def __init__(self) -> None:
        self.person = Person()
    
    def build(self):
        return self.person

class PersonInfoBuilder(PersonBuilder):
    def called(self, name):
        self.person.name = name
        return self

class PersonJobBuilder(PersonInfoBuilder):
    def works_as_a(self, position):
        self.person.position = position
        return self

class PersonBirthDateBuilder(PersonJobBuilder):
    def born(self, date_of_birth):
        self.person.date_of_birth = date_of_birth
        return self


pb = PersonBirthDateBuilder()
me = pb.called('Dmitry').works_as_a('Quant').born('1/1/1980').build()
print(me)


# Практическое задание
class CodeBuilder:
    def __init__(self, root_name):
        self.root_name = root_name
        self.members = {}

    def add_field(self, type, name):
        self.members[type] = name
        return self

    def __str__(self):
        lines = [f'class {self.root_name}:']
        if not self.members:
            lines.append('    pass')
        else:
            lines.append(f'    def __init__(self):')
            for k, v in self.members.items():
                lines.append(f'        self.{k} = {v}')
        return '\n'.join(lines)


cb = CodeBuilder('Foo')
print(cb)
cb = CodeBuilder('Person').add_field('name', '""').add_field('age', '0')
print(cb)