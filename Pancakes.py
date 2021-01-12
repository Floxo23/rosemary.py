from kitchen import Rosemary
from kitchen.utensils import Pan, Plate, Bowl
from kitchen.ingredients import Butter, Egg, Flour, Milk, Salt

#initially, take a bowl
bowl = Bowl.use(name='Bowl')
# then, take two eggs and crack the, in the bowl mixing them when their in
for i in range(2):
    egg = Egg.take()
    egg.crack()
    bowl.add(egg)
bowl.mix()
#add a dash of salt
bowl.add(Salt.take('dash'))
#then add the flour in increments of 50g, stiring in between 
for i in range(5):
    bowl.add(Flour.take(grams = 50))
    bowl.mix()
#add the milk in two increments of 250ml    
for i in range(2):    
    bowl.add(Milk.take(ml = 250))
    bowl.mix()
#use the pan to fry 8 pencakes seperately ...   
plate = Plate.use(name='pen-plate')
for i in range(8):
    pancake_pan = Pan.use(name='pancake')
    pancake_pan.add(Butter.take('slice'))
    pancake_pan.add(bowl.take('1/8'))
    # ...but cook them 60s on each sides then flip
    for i in range(2):
        pancake_pan.cook(minutes=1)
        pancake_pan.flip()   
   #take a plate and serve them  
    pancake = pancake_pan.take()
    plate.add(pancake)
Rosemary.taste(plate)       
Rosemary.serve(plate)