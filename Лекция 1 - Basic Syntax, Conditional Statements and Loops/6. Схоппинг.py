budget = int(input())
command = input()

while command != "End":
    product_price = int(command)
    budget -= product_price
    if budget < 0:
        print("You went in overdraft!")
        break
    command = input()    #  ТУК ПРОЧИТА КОМАНДАТА END, АКО Е ЗАДАДЕНА ТАКАВА. в ПРОТИВЕН СЛУЧАЙ ЩЕ ВЪРТИ СТОЙНОСТТА
                          # ,КОЯТО Е ЗАДАДЕНА ДОКАТО НЕ ДОКАРА БЮДЖЕТА ДО ОТРИЦАТЕЛНО ЧИСЛО И ДАДЕ, ЧЕ СМЕ В ОУВЪРДРАФТ,
                           # ЗАЩОТО НИЕ ИМАМЕ САМО ЕДНА ПОКУПКА И КОМАНДА END.
else:
    print("You bought everything needed.")
