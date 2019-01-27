from Chef import Chef
from ChineseChef import ChineseChef

myChef = Chef()
myChef.make_special_dish() #chef version

myChineseChef = ChineseChef()
myChineseChef.make_special_dish() #chinese chef version

myChineseChef.make_chicken() #the chinese chef inherited the behaviour of the chef class
