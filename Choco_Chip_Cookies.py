from kitchen import Rosemary
from kitchen.utensils import Plate, Bowl, Oven, BakingTray
from kitchen.ingredients import Butter, Egg, Flour, Milk, ChocolateChips, Sugar, BakingPowder
import time

bowl = Bowl.use(name = 'Bowl')
cookie_oven = Oven.use()

# preheat the oven
cookie_oven.preheat(degrees=175)

# take the butter and suggar and mix
butter = Butter.take('part')
bowl.add(butter)

# add the sugar in increments 
for i in range(5):
    sugar = Sugar.take(grams=50)
    bowl.mix()

# add the eggs
for i in range(2):
    egg = Egg.take()
    egg.crack()
    bowl.add(egg)
    bowl.mix()
# in increments add the Chocolate Chips and the Flour
for i in range(4):
    ChocolateChips=ChocolateChips.take(grams=50)
    bowl.add(ChocolateChips)
    Flour=Flour.take(grams=75)
    bowl.add(Flour)
    bowl.mix()
baking_powder = BakingPowder.take('some')

#use a Cookie Tray and a Plate
plate = Plate.use(name='cookie-plate')
cookie_tray = BakingTray.use(name='cookies')

#form 8 cookies on the baking tray 
for i in range(8):
    cookie_tray.add(bowl.take('1/8'))


# Now add the tray to the oven and take it again
cookie_oven.add(cookie_tray)
cookie_oven.bake(minutes=10)
baked_cookie_tray = cookie_oven.take()

#take them all off the tray and serve them on the plate
plate.add(baked_cookie_tray.take())

#perheaps wait for the cookies to cool down :-)
time
time.sleep(5.5)

#and then serve them
Rosemary.serve(plate)