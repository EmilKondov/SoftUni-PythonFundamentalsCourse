from project.beverage.hot_beverage import HotBeverage


class Coffee(HotBeverage):
    MILLILITERS = 50
    PRICE = 3.50

    """
     Понеже в Coffee имаме допълнителен атрибут, то ние трябва да предефинираме __init__ - а,
    както следва в долните редове код

    Важно е да се отбележи, че милилитрите и цената винаги трябва да са от константата на
    класа Coffee докато името може да е различно

    Това означава, че когато някой  ни прави кафе ние няма да му позволим да ни подаде нито цена, нито милилитри,
    които са атрибути на наследения клас beverage, но за класа coffee ние винаги ще имаме константа цена
    и количество за всяко кафе от този клас.

    Тоест името и кофейна ще бъдат подавани отвън за всяко кафе, но цената и количеството ние вътрешно
    ще взимаме винаги от константата.
    """
    def __init__(self, name: str, caffeine:float) -> None:
        super().__init__(name, Coffee.PRICE, Coffee.MILLILITERS)
        self.__caffeine = caffeine

    @property
    def caffeine(self):
        return self.__caffeine