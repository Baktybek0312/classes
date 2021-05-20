 4)ContactList
#
#
# Создайте класс ContactList, который должен наследоваться от
#
# встроенного класса list. В нем должен быть реализован метод
#
# search_by_name, который должен принимать имя, и возвращать список
#
# всех совпадений. Замените all_contacts = [ ] на all_contacts =
#
# ContactList(). Создайте несколько контактов, используйте метод
#
# search_by_name.

class ContactList(list):
    def search_by_name(self, name):
       all_contacts = []
       for i in self:
            if name in i:
                all_contacts.append(i)
            return all_contacts


cont = ContactList()
cont.append("A")
cont.append("B")
cont.append("C")
print(cont)
print(cont.search_by_name("E"))
