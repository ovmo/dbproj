
#from mysql_model import *
#import app

from db import db
from controller.ControllerMenu import save_new_toppings, save_new_pizza, save_new_drinks, save_new_desserts, \
    find_single_topping, find_single_pizza, find_single_drinks, find_single_dessert
from controller.DriverController import save_new_delivery_driver, find_single_driver


def fillDB():
    # add toppings
    sauce = save_new_toppings(name="Sauce", price=1.00, vegi=True)
    cheese = save_new_toppings(name="Cheese", price=1.00, vegi=True)
    mozzarella = save_new_toppings(name="Mozzarella", price=1.50, vegi=True)
    buratta = save_new_toppings(name="Buratta", price=1.75, vegi=True)
    tomatoes = save_new_toppings(name="Cherry Tomatoes", price=1.00, vegi=True)
    mushrooms = save_new_toppings(name="Mushroom", price=1.00, vegi=True)
    parma = save_new_toppings(name="Parma", price=2.00, vegi=False)
    prosciutto = save_new_toppings(name="Prosciutto", price=2.00, vegi=False)
    salami = save_new_toppings(name="Salami", price=2.00, vegi=False)
    chicken = save_new_toppings(name="Chicken", price=2.00, vegi=False)
    bresaola = save_new_toppings(name="Bresaola", price=2.00, vegi=False)
    pepperoni = save_new_toppings(name="Pepperoni", price=2.00, vegi=False)
    arugula = save_new_toppings(name="Arugula", price=1.00, vegi=True)
    basil = save_new_toppings(name="Basil", price=0.50, vegi=True)
    anchovy = save_new_toppings(name="Anchovy", price=1.50, vegi=False)
    tuna = save_new_toppings(name="Tuna", price=1.50, vegi=False)
    olives = save_new_toppings(name="Olives", price=0.50, vegi=True)
    capers = save_new_toppings(name="Capers", price=0.50, vegi=True)
    garlic = save_new_toppings(name="Garlic", price=0.50, vegi=True)
    oregano = save_new_toppings(name="Oregano", price=0.50, vegi=True)
    parmesan = save_new_toppings(name="Parmesan", price=0.50, vegi=True)

    if find_single_topping(toppings_name=sauce.toppings_name) is None:
        db.session.add(sauce)
    if find_single_topping(toppings_name=cheese.toppings_name) is None:
        db.session.add(cheese)
    if find_single_topping(toppings_name=mozzarella.toppings_name) is None:
        db.session.add(mozzarella)
    if find_single_topping(toppings_name=buratta.toppings_name) is None:
        db.session.add(buratta)
    if find_single_topping(toppings_name=tomatoes.toppings_name) is None:
        db.session.add(tomatoes)
    if find_single_topping(toppings_name=mushrooms.toppings_name) is None:
        db.session.add(mushrooms)
    if find_single_topping(toppings_name=parma.toppings_name) is None:
        db.session.add(parma)
    if find_single_topping(toppings_name=prosciutto.toppings_name) is None:
        db.session.add(prosciutto)
    if find_single_topping(toppings_name=salami.toppings_name) is None:
        db.session.add(salami)
    if find_single_topping(toppings_name=chicken.toppings_name) is None:
        db.session.add(chicken)
    if find_single_topping(toppings_name=bresaola.toppings_name) is None:
        db.session.add(bresaola)
    if find_single_topping(toppings_name=pepperoni.toppings_name) is None:
        db.session.add(pepperoni)
    if find_single_topping(toppings_name=arugula.toppings_name) is None:
        db.session.add(arugula)
    if find_single_topping(toppings_name=basil.toppings_name) is None:
        db.session.add(basil)
    if find_single_topping(toppings_name=anchovy.toppings_name) is None:
        db.session.add(anchovy)
    if find_single_topping(toppings_name=tuna.toppings_name) is None:
        db.session.add(tuna)
    if find_single_topping(toppings_name=olives.toppings_name) is None:
        db.session.add(olives)
    if find_single_topping(toppings_name=capers.toppings_name) is None:
        db.session.add(capers)
    if find_single_topping(toppings_name=garlic.toppings_name) is None:
        db.session.add(garlic)
    if find_single_topping(toppings_name=oregano.toppings_name) is None:
        db.session.add(oregano)
    if find_single_topping(toppings_name=parmesan.toppings_name) is None:
        db.session.add(parmesan)

    db.session.commit()

    #creating the Pizzas
    pizza_magarita = save_new_pizza("Margherita", ["Sauce", "Cheese"])
    pizza_caprese = save_new_pizza("Caprese", ["Sauce", "Mozzarella", "Cherry Tomatoes"])
    pizza_buratina = save_new_pizza("Buratina", ["Sauce", "Buratta", "Cherry Tomatoes", "Basil"])
    pizza_fungi = save_new_pizza("Fungi", ["Sauce", "Cheese", "Mushroom", "Olives"])
    pizza_parma = save_new_pizza("Parma", ["Sauce", "Cheese", "Parma", "Arugula"])
    pizza_prosciutto = save_new_pizza("Prosciutto", ["Sauce", "Cheese", "Prosciutto"])
    pizza_pepperoni = save_new_pizza("Pepperoni", ["Sauce", "Cheese", "Pepperoni"])
    pizza_diavola = save_new_pizza("Diavola", ["Sauce", "Cheese", "Chicken", "Cherry Tomatoes", "Basil"])
    pizza_salami = save_new_pizza("Salami", ["Sauce", "Cheese", "Salami"])
    pizza_romana = save_new_pizza("Romana", ["Sauce", "Cheese", "Olives", "Anchovy", "Capers"])
    pizza_napoli = save_new_pizza("Napoli", ["Sauce", "Cheese", "Oregano", "Anchovy"])
    pizza_marinara = save_new_pizza("Marinara", ["Sauce", "Garlic", "Basil"])
    pizza_crudo = save_new_pizza("Crudo", ["Sauce", "Cheese", "Parma"])
    pizza_tricolore = save_new_pizza("Tricolore", ["Sauce", "Bresaola", "Parmesan"])

    if find_single_pizza(pizza_name=pizza_caprese.pizza_name) is None:
        db.session.add(pizza_caprese)
    if find_single_pizza(pizza_name=pizza_magarita.pizza_name) is None:
        db.session.add(pizza_magarita)
    if find_single_pizza(pizza_name=pizza_buratina.pizza_name) is None:
        db.session.add(pizza_buratina)
    if find_single_pizza(pizza_name=pizza_fungi.pizza_name) is None:
        db.session.add(pizza_fungi)
    if find_single_pizza(pizza_name=pizza_parma.pizza_name) is None:
        db.session.add(pizza_parma)
    if find_single_pizza(pizza_name=pizza_prosciutto.pizza_name) is None:
        db.session.add(pizza_prosciutto)
    if find_single_pizza(pizza_name=pizza_pepperoni.pizza_name) is None:
        db.session.add(pizza_pepperoni)
    if find_single_pizza(pizza_name=pizza_diavola.pizza_name) is None:
        db.session.add(pizza_diavola)
    if find_single_pizza(pizza_name=pizza_salami.pizza_name) is None:
        db.session.add(pizza_salami)
    if find_single_pizza(pizza_name=pizza_romana.pizza_name) is None:
        db.session.add(pizza_romana)
    if find_single_pizza(pizza_name=pizza_napoli.pizza_name) is None:
        db.session.add(pizza_napoli)
    if find_single_pizza(pizza_name=pizza_marinara.pizza_name) is None:
        db.session.add(pizza_marinara)
    if find_single_pizza(pizza_name=pizza_crudo.pizza_name) is None:
        db.session.add(pizza_crudo)
    if find_single_pizza(pizza_name=pizza_tricolore.pizza_name) is None:
        db.session.add(pizza_tricolore)

    db.session.commit()

    #creating the Drinks
    water = save_new_drinks(name="Water", price=1.00)
    coke = save_new_drinks(name="Coca Cola", price=2.00)
    apple = save_new_drinks(name="Apple Juice", price=2.00)
    orange = save_new_drinks(name="Orange Juice", price=2.00)
    white_wine = save_new_drinks(name="White Wine", price=4.00)
    red_wine = save_new_drinks(name="Red Wine", price=4.00)
    limoncello = save_new_drinks(name="Limoncello", price=4.00)
    espresso = save_new_drinks(name="Espresso", price=1.50)
    cappuccino = save_new_drinks(name="Cappuccino", price=2.50)

    if find_single_drinks(drinks_name=water.drinks_name) is None:
        db.session.add(water)
    if find_single_drinks(drinks_name=coke.drinks_name) is None:
        db.session.add(coke)
    if find_single_drinks(drinks_name=apple.drinks_name) is None:
        db.session.add(apple)
    if find_single_drinks(drinks_name=orange.drinks_name) is None:
        db.session.add(orange)
    if find_single_drinks(drinks_name=white_wine.drinks_name) is None:
        db.session.add(white_wine)
    if find_single_drinks(drinks_name=red_wine.drinks_name) is None:
        db.session.add(red_wine)
    if find_single_drinks(drinks_name=limoncello.drinks_name) is None:
        db.session.add(limoncello)
    if find_single_drinks(drinks_name=espresso.drinks_name) is None:
        db.session.add(espresso)
    if find_single_drinks(drinks_name=cappuccino.drinks_name) is None:
        db.session.add(cappuccino)

    db.session.commit()

    #create the Desserts
    tiramisu = save_new_desserts(name="Tiramisu", price=4.00)
    pana_cotta = save_new_desserts(name="Pana Cotta", price=5.00)
    tartufo = save_new_desserts(name="Tartufo", price=5.00)

    if find_single_dessert(dessert_name=tiramisu.dessert_name) is None:
        db.session.add(tiramisu)
    if find_single_dessert(dessert_name=pana_cotta.dessert_name) is None:
        db.session.add(pana_cotta)
    if find_single_dessert(dessert_name=tartufo.dessert_name) is None:
        db.session.add(tartufo)

    db.session.commit()

    #deliveryDrinvers

    chiara = save_new_delivery_driver(name="Chiara", area=621)
    lou = save_new_delivery_driver(name="Lou", area=621)
    marie = save_new_delivery_driver(name="Marie", area=621)
    sam = save_new_delivery_driver(name="Sam", area=621)
    jolijn = save_new_delivery_driver(name="Jolijn", area=621)
    aditi = save_new_delivery_driver(name="Aditi", area=621)
    leon = save_new_delivery_driver(name="Leon", area=621)
    parand = save_new_delivery_driver(name="Parand", area=621)
    alex = save_new_delivery_driver(name="Alex", area=621)
    michelle = save_new_delivery_driver(name="Michelle", area=621)
    tom = save_new_delivery_driver(name="Tom", area=621)
    joaquin = save_new_delivery_driver(name="Joaquin", area=621)
    kai = save_new_delivery_driver(name="Kai", area=621)
    claudia = save_new_delivery_driver(name="Claudia", area=621)
    alisa = save_new_delivery_driver(name="Alisa", area=621)
    chandu = save_new_delivery_driver(name="Chandu", area=621)
    yarik = save_new_delivery_driver(name="Yarik", area=621)
    dino = save_new_delivery_driver(name="Dino", area=621)
    constantin = save_new_delivery_driver(name="Constantin", area=622)
    simon = save_new_delivery_driver(name="Simon", area=622)
    sahil = save_new_delivery_driver(name="Sahil", area=622)
    carlo = save_new_delivery_driver(name="Carlo", area=622)
    noah = save_new_delivery_driver(name="Noah", area=622)
    julia = save_new_delivery_driver(name="Julia", area=622)
    hanna = save_new_delivery_driver(name="Hanna", area=622)
    mona = save_new_delivery_driver(name="Mona", area=622)
    rene = save_new_delivery_driver(name="Rene", area=622)
    mane = save_new_delivery_driver(name="Mane", area=622)
    frunz = save_new_delivery_driver(name="Frunz", area=622)
    rosa = save_new_delivery_driver(name="Rosa", area=622)
    sophie = save_new_delivery_driver(name="Sophie", area=622)
    husam = save_new_delivery_driver(name="Husam", area=622)
    mischa = save_new_delivery_driver(name="Mischa", area=622)
    ella = save_new_delivery_driver(name="Ella", area=622)
    lena = save_new_delivery_driver(name="Lena", area=622)
    meli = save_new_delivery_driver(name="Meli", area=622)
    travis = save_new_delivery_driver(name="Travis", area=622)
    adrien = save_new_delivery_driver(name="Adrien", area=622)

    # adding the Drivers to the DB
    if find_single_driver(delivery_driver_name=travis.delivery_driver_name) is None:
        db.session.add(travis)
    if find_single_driver(delivery_driver_name=julia.delivery_driver_name) is None:
        db.session.add(julia)
    if find_single_driver(delivery_driver_name=hanna.delivery_driver_name) is None:
        db.session.add(hanna)
    if find_single_driver(delivery_driver_name=mona.delivery_driver_name) is None:
        db.session.add(mona)
    if find_single_driver(delivery_driver_name=rene.delivery_driver_name) is None:
        db.session.add(rene)
    if find_single_driver(delivery_driver_name=mane.delivery_driver_name) is None:
        db.session.add(mane)
    if find_single_driver(delivery_driver_name=frunz.delivery_driver_name) is None:
        db.session.add(frunz)
    if find_single_driver(delivery_driver_name=rosa.delivery_driver_name) is None:
        db.session.add(rosa)
    if find_single_driver(delivery_driver_name=sophie.delivery_driver_name) is None:
        db.session.add(sophie)
    if find_single_driver(delivery_driver_name=husam.delivery_driver_name) is None:
        db.session.add(husam)
    if find_single_driver(delivery_driver_name=adrien.delivery_driver_name) is None:
        db.session.add(adrien)
    if find_single_driver(delivery_driver_name=lena.delivery_driver_name) is None:
        db.session.add(lena)
    if find_single_driver(delivery_driver_name=meli.delivery_driver_name) is None:
        db.session.add(meli)
    if find_single_driver(delivery_driver_name=mischa.delivery_driver_name) is None:
        db.session.add(mischa)
    if find_single_driver(delivery_driver_name=ella.delivery_driver_name) is None:
        db.session.add(ella)
    if find_single_driver(delivery_driver_name=chiara.delivery_driver_name) is None:
        db.session.add(chiara)
    if find_single_driver(delivery_driver_name=lou.delivery_driver_name) is None:
        db.session.add(lou)
    if find_single_driver(delivery_driver_name=marie.delivery_driver_name) is None:
        db.session.add(marie)
    if find_single_driver(delivery_driver_name=sam.delivery_driver_name) is None:
        db.session.add(sam)
    if find_single_driver(delivery_driver_name=jolijn.delivery_driver_name) is None:
        db.session.add(jolijn)
    if find_single_driver(delivery_driver_name=aditi.delivery_driver_name) is None:
        db.session.add(aditi)
    if find_single_driver(delivery_driver_name=leon.delivery_driver_name) is None:
        db.session.add(leon)
    if find_single_driver(delivery_driver_name=parand.delivery_driver_name) is None:
        db.session.add(parand)
    if find_single_driver(delivery_driver_name=alex.delivery_driver_name) is None:
        db.session.add(alex)
    if find_single_driver(delivery_driver_name=michelle.delivery_driver_name) is None:
        db.session.add(michelle)
    if find_single_driver(delivery_driver_name=tom.delivery_driver_name) is None:
        db.session.add(tom)
    if find_single_driver(delivery_driver_name=joaquin.delivery_driver_name) is None:
        db.session.add(joaquin)
    if find_single_driver(delivery_driver_name=kai.delivery_driver_name) is None:
        db.session.add(kai)
    if find_single_driver(delivery_driver_name=claudia.delivery_driver_name) is None:
        db.session.add(claudia)
    if find_single_driver(delivery_driver_name=alisa.delivery_driver_name) is None:
        db.session.add(alisa)
    if find_single_driver(delivery_driver_name=chandu.delivery_driver_name) is None:
        db.session.add(chandu)
    if find_single_driver(delivery_driver_name=yarik.delivery_driver_name) is None:
        db.session.add(yarik)
    if find_single_driver(delivery_driver_name=dino.delivery_driver_name) is None:
        db.session.add(dino)
    if find_single_driver(delivery_driver_name=constantin.delivery_driver_name) is None:
        db.session.add(constantin)
    if find_single_driver(delivery_driver_name=simon.delivery_driver_name) is None:
        db.session.add(simon)
    if find_single_driver(delivery_driver_name=sahil.delivery_driver_name) is None:
        db.session.add(sahil)
    if find_single_driver(delivery_driver_name=carlo.delivery_driver_name) is None:
        db.session.add(carlo)
    if find_single_driver(delivery_driver_name=noah.delivery_driver_name) is None:
        db.session.add(noah)

    db.session.commit()
