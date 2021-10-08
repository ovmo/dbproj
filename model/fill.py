
#from mysql_model import *
#import app

#add toppings
from app import db
from controller.ControllerMenu import save_new_toppings, save_new_pizza, save_new_drinks, save_new_desserts
from controller.DriverController import save_new_delivery_driver

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

db.session.add(sauce)
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

#if the Pizzas should take in the topping instance created by the DB
pizza_buratina1 = save_new_pizza("Buratina", [sauce, buratta, tomatoes, basil])
pizza_magarita1 = save_new_pizza("Margherita", [sauce, cheese])
pizza_caprese1 = save_new_pizza("Caprese", [sauce, tomatoes, mozzarella])
pizza_fungi1 = save_new_pizza("Fungi", [sauce, cheese, mushrooms, olives])
pizza_parma1 = save_new_pizza("Parma", [sauce, cheese, parma, arugula])
pizza_prosciutto1 = save_new_pizza("Prosciutto", [sauce, cheese, prosciutto])
pizza_pepperoni1 = save_new_pizza("Pepperoni Picante", [sauce, cheese, pepperoni])
pizza_diavola1 = save_new_pizza("Diavola", [sauce, cheese, chicken, tomatoes, basil])
pizza_salami1 = save_new_pizza("Salami", [sauce, cheese, salami])
pizza_romana1 = save_new_pizza("Romana", [sauce, cheese, olives, anchovy, capers])
pizza_napoli1 = save_new_pizza("Napoli", [sauce, cheese, anchovy, oregano])
pizza_marinara1 = save_new_pizza("Marinara", [sauce, garlic, basil])
pizza_crudo1 = save_new_pizza("Crudo", [sauce, cheese, parma])
pizza_tricolore1 = save_new_pizza("Tricolore", [sauce, bresaola, parmesan])

db.session.add(pizza_caprese)
db.session.add(pizza_magarita)
db.session.add(pizza_buratina)
db.session.add(pizza_fungi)
db.session.add(pizza_parma)
db.session.add(pizza_prosciutto)
db.session.add(pizza_pepperoni)
db.session.add(pizza_diavola)
db.session.add(pizza_salami)
db.session.add(pizza_romana)
db.session.add(pizza_napoli)
db.session.add(pizza_marinara)
db.session.add(pizza_crudo)
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

db.session.add(water)
db.session.add(coke)
db.session.add(apple)
db.session.add(orange)
db.session.add(white_wine)
db.session.add(red_wine)
db.session.add(limoncello)
db.session.add(espresso)
db.session.add(cappuccino)
db.session.commit()

#create the Desserts
tiramisu = save_new_desserts(name="Tiramisu", price=4.00)
pana_cotta = save_new_desserts(name="Pana Cotta", price=5.00)
tartufo = save_new_desserts(name="Tartufo", price=5.00)

db.session.add(tiramisu)
db.session.add(pana_cotta)
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
db.session.add(travis)
db.session.add(julia)
db.session.add(hanna)
db.session.add(mona)
db.session.add(rene)
db.session.add(mane)
db.session.add(frunz)
db.session.add(rosa)
db.session.add(sophie)
db.session.add(husam)
db.session.add(adrien)
db.session.add(lena)
db.session.add(meli)
db.session.add(mischa)
db.session.add(ella)
db.session.add(chiara)
db.session.add(lou)
db.session.add(marie)
db.session.add(sam)
db.session.add(jolijn)
db.session.add(aditi)
db.session.add(leon)
db.session.add(parand)
db.session.add(alex)
db.session.add(michelle)
db.session.add(tom)
db.session.add(joaquin)
db.session.add(kai)
db.session.add(claudia)
db.session.add(alisa)
db.session.add(chandu)
db.session.add(yarik)
db.session.add(dino)
db.session.add(constantin)
db.session.add(simon)
db.session.add(sahil)
db.session.add(carlo)
db.session.add(noah)
db.session.commit()


