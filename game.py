#import replit
#Only works on repl.it

from random import randint
from textwrap import fill
from time import sleep

# A foreword - I tried hard to write code that made sense to
# read through (i.e. avoiding hardcore abbreviations and
# such). It may be a bit longer but I feel like it's easier
# on human eyes and brains. Some parts of the game I've added
# comments to (lots of 'em) and others I've left alone.
# If there are any questions or comments, feel free to
# e-mail me at alexandracecille1@gmail.com
#
# The super-long dictionaries I implemented are so I could
# focus on making the code work before I worried about descriptions
# and the actual content. It felt really novel and smart to me at
# the time, but now I kind of feel silly. They seem like
# big blocks of plain unnecessarity. But hey. It is what it is.
#
# Oh, and I feel like this is a great example of spaghetti code.
# See link below. I just don't quite know how to make it cleaner
# and more aesthetically pleasing. I'll work on it.
#
# http://tinyurl.com/gsdvajz



########## CURRENT OBJECTIVES #############
# Add fancy woman quest
# Add chef quest
# Implement talk methods for everyone
# Figure out wtf you're going to do for the sewers
# Finish descriptions
# Add sleeps to guy/girl conversation


######### BEFORE FINALIZATION #############
# Take out """ from sleep in user_input
# (it's just annoying when I'm trying to fly
# through the game to debug)
# Set player money back to 0
# Clear player inventory, set money and class to 0


############# CHANGE LOG ##################
# Added newspaper/suitcase puzzle
# Added lottery ticket and 'scratch'
# Changed up fight scene and some descriptions
# Added 'look' and 'take' functions to each category
# Changed text wraps to fill 100 characters
# Added dumpster functionality
# Changed sunglasses to 'hat' and 'scarf'
# Brought piano back
# Streamlined 'look'
# Added street dude quest
# Turned attendant into an NPC for conversations
# Fixed 'scratch' functionality and exceptions
# Added 'buy' and 'sell' functions
# Added the fighter NPC (how could I forget him?)
# Fixed 'fight' for drunk and boxer
# Added old man quest
# Fixed bug w/ dude if you have 2 tacos
# Added 'play' and 'smoke' functions
# SWEET JESUS FINISHED THE POOL GAME FINALLY PRAISE THE LORD
# Added bar guy/girl quest
# Added fighter quest
# Fixed it so you can die (Muahahaha)
# Fixed buy/sell so it removes item from NPC inventory
# Fixed pool game from playing if you input something stupid





lock = str((randint(0,9), randint(0,9), randint(0,9)))
#For the newspaper/suitcase puzzle
 

#                    -----======(   PREPOSITIONS   )======-----


prepositions = ["from", "with", "inside", "outside", "of", "in", "to", "for", "on", "at", "by",
"about", "as", "into", "like", "through", "after", "over", "between", "out", "against", "during",
"without", "before", "under", "around", "among"]


#                    -----======(   DESCRIPTIONS   )======-----

items = {"hat":"A fancy-looking top hat. Maybe the rabbit costs extra...",
         "scarf":"A basic scarf. It seems thin and designed for fashion, not warmth.",
         "map":"Oh the necessary map. Your pride and joy; finally a way to navigate your world.",
         "hot dog":"A delicious (though rubbery) looking hot dog slathered with the works.",
         "taco":"A crunchy taco filled to the brim. You oughta eat it over a tortilla; everything\
 that falls out = extra taco!!",
         "pretzel":"Mmm...a warm soft pretzel drowning in salt.",
         "pizza":"A slice of New York style pizza. There is nothing better.",
         "fists":"You look down at your fists. They've gotten you through many scraps just fine.\
 You may want to look for a weapon though - just saying.",
         "glass pipe":"A solid water pipe. Good for smoking or beating someone over the head.",
         "pipe":None,
         "utility knife":"A dull knife that probably couldn't even cut through fabric. Hey,\
 better than your fists.",
         "knife":None,
         "broken bottle":"A green bottle broken at the neck. Sharp, jagged edges make it\
 the perfect weapon.",
         "boxing gloves":"Thick gloves that pack a punch (ha). Combined with your super-ninja\
 fighting skills, they make for a formidable weapon that can blast through any face imaginable.",
         "solid tie":"A single-color tie that does not impress. Still, better than nothing.",
         "patterned tie":"A paisley tie that pops.",
         "bracelet":"A sterling silver chain-link bracelet. Beautiful down to the last detail.",
         "shank":"A dirty shank that looks like it was made in prison; the edges are sharpened\
 hastily and the metal is bent. By this point it has dulled and you'll be lucky if it\
 breaks the first layer of skin.",
         "dirty shoes":"Some nasty brown hobo shoes. You get the impression that they used to be white.",
         "piss puddle":"A puddle of piss. Need I say more?",
         "piss":None,
         "puddle":None,
         "blanket":"A tattered old blanket. You can't imagine it providing any level of warmth.",
         "pillow":"A nasty, stained pillow. You don't even want to know where the stains came from.",
         "cardboard box":"Your run of the mill cardboard box. Exciting.",
         "suitcase":"A small suitcase likely holding the hobo's panhandling money.",
         "gum":"Some pink bubble gum littered with bite marks. Disgusting.",
         "newspaper":"It's full of biased stories that make you gag. Scribbled in the margin are\
 the numbers {}. You wonder what they're for.".format(lock),
         "apple":"A half-eaten apple. What's worse than finding a worm in your apple? Finding half a worm.",
         "dumpster":"You hold your nose and hop in the dumpster, which is mostly filled with cardboard\
 boxes and trash bags.",
         "leather wallet":"A fancy-looking leather wallet. Real leather? Who knows. Close enough.",
         "cell phone":"An old dinosaur of a flip phone that likely doesn't even work.",
         "jukebox":"A rockin' jukebox filled with some classics. Maybe you should play one.",
         "long island":"A drink made strong in this joint. Served with a lemon wedge.",
         "limoncello":"Some fancy dessert liquor. Lemon flavored and hangover-enducing.",
         "mint julep":"Rimmed with sugar, most would consider it a girly drink. Packs a\
 punch if you're not expecting it.",
         "cigar":"A legitimate cuban cigar. Where did the old man get this? You have a strong urge\
 to smoke it.",
         "lottery ticket":"Step right up, you're sure to win this cheap-looking lottery ticket!",
         "ticket":None,
         "plain tee":"A plain T-shirt. Nothing to write home about.",
         "graphic tee":"A T-shirt that only men in a mid-life crisis wear.",
         "jeans":"What is Mario's favorite fabric? Denim denim denim.",
         "slacks":"Nice-looking slacks that your mother would be proud of.",
         "fancy shoes":"Some dress shoes that shine in the light. Beautiful.",
         "coffee":"A cup o' joe. Should wake you right up. At least, it would,\
 if tiredness was a thing here.",
         "chairs":"Uncomfortable-looking chairs. You refuse to sit in them.",
         "clock":"Look at that, the clock is set to 12:34. Your favorite time. Too bad it's wrong.",
         "calendar":"Set on August, it appears the staff are several months behind.",
         "purse":"A clear knockoff, but hey, we're not all made of money. Looks like\
 there's some items you can take, if you're so morally inclined.",
         "lipstick":"Some color named 'Kiss me dead.' That's disturbing.",
         "lighter":"A lighter with 'Bob Marley lives' scrawled on it. Pretty sure he doesn't.",
         "used napkin":"A napkin that likely contains a booger or two.",
         "tampon":"Thank god it's not used.",
         "bruschetta":"Grilled bread with garlic, tomatoes, olive oil, and other ingredients.",
         "crostini":"A mini-toast sort of dish.",
         "insalata caprese":"Caprese salad. Sounds fancy.",
         "waterfall":"A gorgeous waterfall aglow in soft white light. The sound is beyond\
 soothing.",
         "pin":"An almost brooch-looking pin with a centrally set diamond. Looks like\
 it costs a pretty penny.",
         "piano":"A grand piano with all the fixins. You should play it, you just might have some\
 mad piano skillz.",
         "steamed lobster":"Just what it sounds like. You can't seem to crack it open.\
 Someone else might want this...",
         "punching bag":"Your basic punching bag. Good for relieving stress and breaking hands.",
         "street vendor":"A street vendor who peddles wares for a living. Seems like someone\
 you could buy from.",
         "vendor":None,
         "hobo":"A smelly man. You feel bad that he's sleeping behind a dumpster, but the\
 shank scares you a little bit.",
         "drunk":"An annoying frat boy that needs just one good punch to the kisser.",
         "dude":"A clear OG. You want to be like him with every fiber of your being.",
         "guy":"A desperate-looking man sitting alone at the bar. He motions for you\
 to talk to him.",
         "girl":"A girl that speaks her mind. Good for her.",
         "old man":"A disabled man in a wheelchair with a plethora of white hair.",
         "man":None,
         "pool shark":"Your average pool shark, ready to challenge whoever comes\
 his way. You can play if you want to, maybe try to make some cash...",
         "pool":None,
         "shark":None,
         "cashier":"A sweet-looking girl manning the cash register.",
         "woman":"A fancy, stuck-up woman with her head in the clouds.",
         "chef":"A pleasant, portly gentleman with a considerable amount of skill.",
         "boxer":"A built athlete covered in a sheen of sweat. Think you can take him?",
         "fighter":"A rumblin'-bumblin' boxer practicing on the punching bag. He stops\
 every few moments and looks your way. Maybe he wants to talk to you?",

         #Items with a 'None' desc. and items below are for 'look' function
         
         "north":"See, this is a good reason to have a map. Go find one.",
         "east":"See, this is a good reason to have a map. Go find one.",
         "west":"See, this is a good reason to have a map. Go find one.",
         "south":"See, this is a good reason to have a map. Go find one.",
         "box office":"Just a fancy box office.",
         "attendant":"A clearly disgruntled employee.",
         "bartender":"A chick with full sleeves on each arm. She doesn't look like\
 a lady to mess with. You consider buying some drinks from her; wonder what the specials are?",
         "clothes":None
         }



#                    -----======(   FOOD   )======-----

class Consumable:
    #Items that can be eaten/drunk(drank?)
    def __init__(self):
    	raise NotImplementedError("This consumable object has no attributess")

    def __str__(self):
    	#What I want the item to return when it shows up in the game
        return "{} (+{} HP)".format(self.name,
                                    self.healing_value)
                                              
    def look(self):
        print(fill(items[self.name], 100))
        
    def take(self, scene):
        print("{} added to inventory.".format(self.name.capitalize()))
        item = real_item[self.name]
        player.inventory.append(item)
        scene.room_items.remove(item.name)
                                              
    def eat(self):
    	print("You eat the {}.".format(self.name))
    	print("+{} HP".format(self.healing_value))
    	if player.hp < 100:
    		player.hp += self.healing_value
    		player.hp = min(100, player.hp)

class CashConsumable:
    #Items like the above that can be purchased/sold
    def __init__(self):
    	raise NotImplementedError("This consumable object has no attributes")

    def __str__(self):
        return "{} (+{} HP) - ${:.2f} ".format(self.name,
                                              self.healing_value,
                                              self.value)
                                                         
    def look(self):
        print(fill(items[self.name], 100))
        
    def take(self, scene):
        print("Sorry klepto, you have to buy that first.")

    def eat(self):
    	print("You eat the {}.".format(self.name))
    	print("+{} HP".format(self.healing_value))
    	if player.hp < 100:
    		player.hp += self.healing_value
    		player.hp = min(100, player.hp)

class HotDog(CashConsumable):
    def __init__(self):
        self.name = "hot dog"
        self.healing_value = 4
        self.value = 2
        self.verb = "eat"

class Taco(CashConsumable):
    def __init__(self):
        self.name = "taco"
        self.healing_value = 6
        self.value = 4
        self.verb = "eat"

class Pretzel(CashConsumable):
    def __init__(self):
        self.name = "pretzel"
        self.healing_value = 10
        self.value = 6
        self.verb = "eat"

class Pizza(CashConsumable):
    def __init__(self):
        self.name = "pizza"
        self.healing_value = 15
        self.value = 8
        self.verb = "eat"

class PissPuddle(Consumable):
    def __init__(self):
        self.name = "piss puddle"
        self.healing_value = 1
        self.class_value = 10
        self.verb = "drink"
        
    def drink(self):
    	print("Oh that's disgusting! You take a few slurps from the puddle.")
    	print("+{} HP".format(self.healing_value))
    	player.hp += self.healing_value
    	print("-{} class".format(self.class_value))
    	player.classy -= self.class_value
    	
    def take(self, scene):
        print("You grab handfuls of the urine and try to stuff them in your\
 pockets, but your bottoms get soaked and you give up. Congratulations, now\
 you smell bad.")
        print("-10 class")
        player.classy -= 10

class Apple(Consumable):
    def __init__(self):
        self.name = "apple"
        self.healing_value = 5
        self.verb = "eat"

    def __str__(self):
    	#This one decreases HP so I want a different string output
        return "{} (-{} HP)".format(self.name,
                                    self.healing_value)
                                               
    def eat(self):
    	print("You eat the {}.".format(self.name))
    	print("-{} HP".format(self.healing_value))
    	player.hp -= self.healing_value

class Coffee(Consumable):
    def __init__(self):
        self.name = "coffee"
        self.class_value = 5
        self.verb = "drink"

    def __str__(self):
        return "{} (-{} class)".format(self.name,
                                       self.class_value)
    
    def drink(self):
    	print("You drink the {}.".format(self.name))
    	print("+0 HP")
    	print("-{} class".format(self.class_value))
    	player.classy -= self.class_value
    	
class Bruschetta(CashConsumable):
    def __init__(self):
        self.name = "bruschetta"
        self.healing_value = 10
        self.value = 15
        self.verb = "eat"

class Crostini(CashConsumable):
    def __init__(self):
        self.name = "crostini"
        self.healing_value = 12
        self.value = 20
        self.verb = "eat"

class InsalataCaprese(CashConsumable):
    def __init__(self):
        self.name = "insalata caprese"
        self.healing_value = 15
        self.value = 25
        self.verb = "eat"




#                    -----======(   CLASSY   )======-----

class Classy:
    #Items that raise (or lower) class
    def __init__(self):
        raise NotImplementedError("This classy object has no attributes")

    def __str__(self):
        return "{} (+{} class)".format(self.name,
                                       self.class_value)
                                       
    def look(self):
        print(fill(items[self.name], 100))
        
    def take(self, scene):
        print("{} added to inventory.".format(self.name.capitalize()))
        item = real_item[self.name]
        player.inventory.append(item)
        scene.room_items.remove(item.name)
                                       
    def wear(self):
    	print("You put on the {}.".format(self.name))
    	print("+{} class".format(self.class_value))
    	player.classy += self.class_value
    	
    def drink(self):
    	print("You drink the {}.".format(self.name))
    	print("+{} class".format(self.class_value))
    	player.classy += self.class_value

class CashClassy:
    #Class items that cost money
    def __init__(self):
        self.name = None
        self.description = None
        self.class_value = None
        raise NotImplementedError("This cash classy object has no attributes")

    def __str__(self):
        return "{} (+{} class) - ${:.2f}".format(self.name,
                                                 self.class_value,
                                                 self.value)
                                                 
    def look(self):
        print(fill(items[self.name], 100))
        
    def take(self, scene):
        print("Sorry klepto, you have to pay for that first.")
                                                 
    def wear(self):
    	print("You put on the {}.".format(self.name))
    	print("+{} class".format(self.class_value))
    	player.classy += self.class_value
    	
    def drink(self):
    	print("You drink the {}.".format(self.name))
    	print("+{} class".format(self.class_value))
    	player.classy += self.class_value

class Hat(CashClassy):
    def __init__(self):
        self.name = "hat"
        self.class_value = 3
        self.value = 6
        self.verb = "wear"

class Scarf(CashClassy):
    def __init__(self):
        self.name = "scarf"
        self.class_value = 7
        self.value = 14
        self.verb = "wear"

class SolidTie(CashClassy):
    def __init__(self):
        self.name = "solid tie"
        self.class_value = 5
        self.value = 10
        self.verb = "wear"

class PatternedTie(CashClassy):
    def __init__(self):
        self.name = "patterned tie"
        self.class_value = 7
        self.value = 14
        self.verb = "wear"

class Bracelet(CashClassy):
    def __init__(self):
        self.name = "bracelet"
        self.class_value = 10
        self.value = 20
        self.verb = "wear"

class DirtyShoes(Classy):
    def __init__(self):
        self.name = "dirty shoes"
        self.class_value = 5
        self.verb = "wear"

class LeatherWallet(Classy):
    def __init__(self):
        self.name = "leather wallet"
        self.class_value = 15
        self.value = randint(10,25)
        self.verb = "wear"
        
    def wear(self):
        print("You put on the {}.".format(self.name))
        print("+{} class".format(self.class_value))
        player.classy += self.class_value
        print()
        print("Upon further inspection, you find ${:.2f} in the wallet!".format(self.value))
        player.money += self.value
        
    def take(self, scene):
        print(fill("You try to pickpocket the drunk guy. As inebriated as he\
 is, he can't ignore a hand grabbing his ass. He swats you back, stumbling\
 in the opposite direction. He quickly forgets your indescretion. Lucky you.", 100))

class Cigar(Classy):
    def __init__(self):
        self.name = "cigar"
        self.class_value = 10
        self.verb = "smoke"

    def take(self, scene):
        print(fill("You try to slip a hand in the old man's pocket and nab the cigar.\
 Unfortunately, he's a little sharper than he looks. He glares at you as you\
 slowly move your hand back.", 100))

    def smoke(self):
        print(fill("You take a few puffs like it's the best thing you've ever tasted.\
 Unfortunately, it's disgusting. At least you look cool, isn't that why all the\
 kids smoke nowadays?",100))
        print("+{} class".format(self.class_value))

class MintJulep(CashClassy):
    def __init__(self):
        self.name = "mint julep"
        self.class_value = 3
        self.value = 8
        self.verb = "drink"

    def drink(self):
    	print("You drink the {}.".format(self.name))
    	print("+{} class".format(self.class_value))
    	player.classy += self.class_value
    	player.drank += 1

class Limoncello(CashClassy):
    def __init__(self):
        self.name = "limoncello"
        self.class_value = 3
        self.value = 8
        self.verb = "drink"
        
    def drink(self):
    	print("You drink the {}.".format(self.name))
    	print("+{} class".format(self.class_value))
    	player.classy += self.class_value
    	player.drank += 1

class LongIsland(CashClassy):
    def __init__(self):
        self.name = "long island"
        self.class_value = 3
        self.value= 8
        self.verb = "drink"
        
    def drink(self):
    	print("You drink the {}.".format(self.name))
    	print("+{} class".format(self.class_value))
    	player.classy += self.class_value
    	player.drank += 1

class PlainTee(CashClassy):
    def __init__(self):
        self.name = "plain tee"
        self.class_value = 10
        self.value = 20
        self.verb = "wear"

class GraphicTee(CashClassy):
    def __init__(self):
        self.name = "graphic tee"
        self.class_value = 12
        self.value = 24
        self.verb = "wear"

class Jeans(CashClassy):
    def __init__(self):
        self.name = "jeans"
        self.class_value = 10
        self.value = 20
        self.verb = "wear"

class Slacks(CashClassy):
    def __init__(self):
        self.name = "slacks"
        self.class_value = 12
        self.value = 24
        self.verb = "wear"

class FancyShoes(CashClassy):
    def __init__(self):
        self.name = "fancy shoes"
        self.class_value = 12
        self.value = 24
        self.verb = "wear"

class Lipstick(Classy):
    def __init__(self):
        self.name = "lipstick"
        self.class_value = 10
        self.verb = "wear"

class Pin(Classy):
    def __init__(self):
        self.name = "pin"
        self.class_value = 15
        self.verb = "wear"
        
    def take(self, scene):
        print(fill("You try to rip the pin off the fancy woman's dress. She is\
 appalled, naturally. How rude of you.", 100))

class Piano(Classy):
    def __init__(self):
        self.name = "piano"
        self.class_value = 10
        self.verb = "play"
        
    def take(self, scene):
        print("Really? Really. Go ahead. Try to take it. I dare you.")
        
    def play(self):
        print(fill("You sit down at the piano, ready to knock the socks off of this joint,\
 and immediately begin weaving an intricate melody with hints of Bach and Beethoven.\
 When you're finished the room bursts into applause and some patrons stand on their\
 feet. Well don't you feel classy.",100))
        print()
        print("+{} class".format(self.class_value))




#                    -----======(   WEAPONS   )======-----

class Weapons:
    #Items you can fight with
    def __init__(self):
        return NotImplementedError("The weapons object has no attributes")

    def __str__(self):
        return "{} ({} damage)".format(self.name,
                                       self.damage)

    def look(self):
        print(fill(items[self.name], 100))
        
        
class CashWeapons:
    #Items you can buy and fight with
    def __init__(self):
        return NotImplementedError("The cash weapons object has no attributes")

    def __str__(self):
        return "{} ({} damage) - ${:.2f}".format(self.name,
                                                 self.damage,
                                                 self.value)
                                                 
    def take(self, scene):
        print("Sorry klepto, you have to buy that first.")

    def look(self):
        print(fill(items[self.name], 100))

class Fists(Weapons):
    def __init__(self):
        self.name = "fists"
        self.damage = 1

class GlassPipe(CashWeapons):
    def __init__(self):
        self.name = "glass pipe"
        self.damage = 3
        self.value = 5

class UtilityKnife(CashWeapons):
    def __init__(self):
        self.name = "utility knife"
        self.damage = 5
        self.value = 10

class Shank(Weapons):
    def __init__(self):
        self.name = "shank"
        self.damage = 7
        
    def take(self, scene):
        print("You'll have to get the hobo out of the way first.")
        
class BrokenBottle(Weapons):
    def __init__(self):
        self.name = "broken bottle"
        self.damage = 10
        
    def take(self, scene):
        print(fill("You try nabbing the broken bottle, but the drunk\
 guy is a little too strong for you. He rips it back and starts after you.\
 Then he lets out a large belch and promptly forgets what he was doing.", 100))

class BoxingGloves(Weapons):
    def __init__(self):
        self.name = "boxing gloves"
        self.damage = 15
        
    def take(self, scene):
        print("Really? I definitely wouldn't do that if I were you.")




#                    -----======(   MISC   )======-----

class Misc:
    #Items that don't belong anywhere else
    def __init__(self):
        raise NotImplementedError("The misc object has no attributes")
    
    def __str__(self):
        return self.name
        
    def look(self):
        print(fill(items[self.name], 100))
        
    def take(self, scene):
        print("{} added to inventory.".format(self.name.capitalize()))
        item = real_item[self.name]
        player.inventory.append(item)
        if item.name in scene.room_items:
            scene.room_items.remove(item.name)
        
class Map(Misc):
    def __init__(self):
        self.name = "map"
    
    def look(self):
        print(fill(items[self.name], 100))
        print("""
                                                            ___________________
                                                           |                   |
                                                           |                   |
         N                                                 |    Boxing Arena   |    
         |                                                 |                   |
     W---X---E      ___________________ ___________________|________   ________|___________________
         |         |                   |                   |                   |           |       |
         S         |                   |                   |                   |  Clothes  | Break |
                   |     Alleyway      |     Restaurant           45th St                          |
                   |                   |                   |                   |   Store   | Room  |
 __________________|________   ________|___________________|___             ___|___________|_______|
|                  |                   |                                       |                   |    
|     Street       |                                                           |                   |
|                        W 8th Ave                    E 8th Ave                         Bar        |
|     Vendor       |                                                           |                   |
|__________________|________   ________|____________________________   ________|___________________|
                   |                   |                   |                   |
                   |                   |                   |                   |
                   |     Box Office    |                   |       Sewers      |
                   |                   |                   |                   |
                   |___________________|                   |___________________|
            """)
            
    def take(self):
        print(fill("Come on, as nice as that guy was? You just want to\
 steal the map? Is a taco too much to ask for? Kids these days.", 100))

class LotteryTicket(Misc):
    def __init__(self):
        self.name = "lottery ticket"
        self.value = randint(5,25)
        self.show_scratch = ["""
 _______________________________________________________
|                                                       |
|   _____   ___  ___          _____  ___                |
|  /       /    |   \    /\     |   /    |    |         |
|  \_____ |     |___/   /  \    |  |     |____|   AND   |
|        \|     |  \   /----\   |  |     |    |   WIN!  |
|   _____/ \___ |   \ /      \  |   \___ |    |         |
|                                                       |
|            _______     _______     _______            |
|           |       |   |       |   |       |           |
|           |       |   |       |   |       |           |
|           |       |   |       |   |       |           |
|           |_______|   |_______|   |_______|           |
|_______________________________________________________|
""","""
 _______________________________________________________
|                                                       |
|   _____   ___  ___          _____  ___                |
|  /       /    |   \    /\     |   /    |    |         |
|  \_____ |     |___/   /  \    |  |     |____|   AND   |
|        \|     |  \   /----\   |  |     |    |   WIN!  |
|   _____/ \___ |   \ /      \  |   \___ |    |         |
|                                                       |
|            _______     _______     _______            |
|           |   ,,  |   |       |   |       |           |
|           |  /|   |   |       |   |       |           |
|           | O O   |   |       |   |       |           |
|           |_______|   |_______|   |_______|           |
|_______________________________________________________|
""","""
 _______________________________________________________
|                                                       |
|   _____   ___  ___          _____  ___                |
|  /       /    |   \    /\     |   /    |    |         |
|  \_____ |     |___/   /  \    |  |     |____|   AND   |
|        \|     |  \   /----\   |  |     |    |   WIN!  |
|   _____/ \___ |   \ /      \  |   \___ |    |         |
|                                                       |
|            _______     _______     _______            |
|           |       |   |   ,,  |   |       |           |
|           |       |   |  /|   |   |       |           |
|           |       |   | O O   |   |       |           |
|           |_______|   |_______|   |_______|           |
|_______________________________________________________|
""","""
 _______________________________________________________
|                                                       |
|   _____   ___  ___          _____  ___                |
|  /       /    |   \    /\     |   /    |    |         |
|  \_____ |     |___/   /  \    |  |     |____|   AND   |
|        \|     |  \   /----\   |  |     |    |   WIN!  |
|   _____/ \___ |   \ /      \  |   \___ |    |         |
|                                                       |
|            _______     _______     _______            |
|           |       |   |       |   |   ,,  |           |
|           |       |   |       |   |  /|   |           |
|           |       |   |       |   | O O   |           |
|           |_______|   |_______|   |_______|           |
|_______________________________________________________|
""","""
 _______________________________________________________
|                                                       |
|   _____   ___  ___          _____  ___                |
|  /       /    |   \    /\     |   /    |    |         |
|  \_____ |     |___/   /  \    |  |     |____|   AND   |
|        \|     |  \   /----\   |  |     |    |   WIN!  |
|   _____/ \___ |   \ /      \  |   \___ |    |         |
|                                                       |
|            _______     _______     _______            |
|           |   ,,  |   |   ,,  |   |       |           |
|           |  /|   |   |  /|   |   |       |           |
|           | O O   |   | O O   |   |       |           |
|           |_______|   |_______|   |_______|           |
|_______________________________________________________|
""","""
 _______________________________________________________
|                                                       |
|   _____   ___  ___          _____  ___                |
|  /       /    |   \    /\     |   /    |    |         |
|  \_____ |     |___/   /  \    |  |     |____|   AND   |
|        \|     |  \   /----\   |  |     |    |   WIN!  |
|   _____/ \___ |   \ /      \  |   \___ |    |         |
|                                                       |
|            _______     _______     _______            |
|           |       |   |   ,,  |   |   ,,  |           |
|           |       |   |  /|   |   |  /|   |           |
|           |       |   | O O   |   | O O   |           |
|           |_______|   |_______|   |_______|           |
|_______________________________________________________|
""","""
 _______________________________________________________
|                                                       |
|   _____   ___  ___          _____  ___                |
|  /       /    |   \    /\     |   /    |    |         |
|  \_____ |     |___/   /  \    |  |     |____|   AND   |
|        \|     |  \   /----\   |  |     |    |   WIN!  |
|   _____/ \___ |   \ /      \  |   \___ |    |         |
|                                                       |
|            _______     _______     _______            |
|           |   ,,  |   |       |   |   ,,  |           |
|           |  /|   |   |       |   |  /|   |           |
|           | O O   |   |       |   | O O   |           |
|           |_______|   |_______|   |_______|           |
|_______________________________________________________|
""","""
 _______________________________________________________
|                                                       |
|   _____   ___  ___          _____  ___                |
|  /       /    |   \    /\     |   /    |    |         |
|  \_____ |     |___/   /  \    |  |     |____|   AND   |
|        \|     |  \   /----\   |  |     |    |   WIN!  |
|   _____/ \___ |   \ /      \  |   \___ |    |         |
|                                                       |
|            _______     _______     _______            |
|           |   ,,  |   |   ,,  |   |   ,,  |           |
|           |  /|   |   |  /|   |   |  /|   |           |
|           | O O   |   | O O   |   | O O   |           |
|           |_______|   |_______|   |_______|           |
|_______________________________________________________|
"""]

    def scratch(self, scene):
        #I tried doing this in one big while loop but it just didn't work out.
        #In fact, there /has/ to be a better way of doing it that isn't as
        #inefficient and ugly, but that's not my priority at the moment.
        #Will fix later.
        print(self.show_scratch[0])
        while True:
            try:
                print("Pick a box to scratch.")
                print()
                answer1 = int(input("> "))
                if answer1 in [1, 2, 3]:
                    print(self.show_scratch[answer1])
                    break
                else:
                    print("Please pick box 1, 2, or 3.")
            except:
                print("Please pick box 1, 2, or 3.")
        while True:
            try:
                print("Pick another box to scratch.")
                print()
                answer2 = int(input("> "))
                if answer2 == answer1:
                    print("Please pick a different box.")
                elif answer2 in [1, 2, 3]:
                    if (answer1 == 1 or answer1 == 2) and (answer2 == 1 or answer2 == 2):
                        print(self.show_scratch[4])
                        break
                    elif (answer1 == 2 or answer1 == 3) and (answer2 == 2 or answer2 == 3):
                        print(self.show_scratch[5])
                        break
                    elif (answer1 == 1 or answer1 == 3) and (answer2 == 1 or answer2 == 3):
                        print(self.show_scratch[6])
                        break
                else:
                    print("Please pick box 1, 2, or 3.")
            except:
                print("Please pick box 1, 2, or 3.")
        while True:
            try:
                print("For formality's sake, last box?")
                print()
                answer3 = int(input("> "))
                if answer3 == answer1 or answer3 == answer2:
                    print("Please pick a different box.")
                elif answer3 in [1, 2, 3]:
                    print(self.show_scratch[7])
                    print("Congratulations! You win ${:.2f}!".format(self.value))
                    print()
                    player.money += self.value
                    map_ = Map_(scene)
                    game = Engine(map_)
                    game.play()
                else:
                    print("Please pick box 1, 2, or 3.")
            except:
                print("Please pick box 1, 2, or 3.")

    def take(self, scene):
        print(fill("You attempt to grab the lottery ticket and run away, but you\
 fumble it and escape with nothing. Good job, that was totally worth it.", 100))

class CellPhone(Misc):
    def __init__(self):
        self.name = "cell phone"
        
    def take(self, scene):
        print(fill("You really want to reach in a young lady's pocket and try to\
 steal something from her? Come on, that's just asking for trouble.", 100))

    #Add more functionality??

class Blanket(Misc):
    def __init__(self):
        self.name = "blanket"
        
    def take(self, scene):
        print(fill("As comfy as it looks, do you really want to be this old carrying around a blankie?", 100))

class Pillow(Misc):
    def __init__(self):
        self.name = "pillow"
        
    def take(self, scene):
        print("You can't think of a use for a smelly, stained pillow.")

class Gum(Misc):
    def __init__(self):
        self.name = "gum"
        
    def take(self, scene):
        print("As gross as it seems, you take the ABC gum. It might come in handy.")
        print()
        print("Used gum added to inventory.")
        player.inventory.append(Gum())
        
class Dumpster(Misc):
    def __init__(self):
        self.name = "dumpster"
        
    def look(self):
        money = randint(1,5)
        print(fill(items[self.name], 100))
        print()
        print(fill("After a short inspection you find ${:.2f}, a wad of used chewing gum, and a half-eaten apple.\
 Should you even take it? Who knows, may come in handy.".format(money),100))
        print()
        print("You pocket the money and ponder taking the other items.")
        print("${:.2f} added.".format(money))

    def take(self, scene):
        print(fill("C'mon, really? Go ahead, try to move it, nonetheless carry it with you.",100))

class CardboardBox(Misc):
    def __init__(self):
        self.name = "cardboard box"
    
    def take(self, scene):
        print("You try to take it with you, but it nearly collapses. Whoops.")

class Suitcase(Misc):
    def __init__(self):
        self.name = "suitcase"
        
    def take(self, scene):
        print("Pretty sure you can exhauast its use from right here.")

class Newspaper(Misc):
    def __init__(self):
        self.name = "newspaper"

class Lighter(Misc):
    def __init__(self):
        self.name = "lighter"

class UsedNapkin(Misc):
    def __init__(self):
        self.name = "used napkin"

class Tampon(Misc):
    def __init__(self):
        self.name = "tampon"

class Purse(Misc):
    def __init__(self):
        self.name = "purse"
        self.inventory = ["lipstick",
                          "lighter",
                          "used napkin",
                          "tampon"]

    def look(self):
        print(fill(items[self.name], 100))
        print()
        print("Contains:")
        for item in self.inventory:
            item = real_item[item]
            print("* {}".format(item))

class Clock(Misc):
    def __init__(self):
        self.name = "clock"
        
    def take(self, scene):
        print("You can't imagine a use for it.")

class Calendar(Misc):
    def __init__(self):
        self.name = "calendar"
    
    def take(self, scene):
        print("However else will the staff know they're months behind?!")

class Waterfall(Misc):
    def __init__(self):
        self.name = "waterfall"
        
    def take(self, scene):
        print(fill("You try to move the waterfall but only succeed in getting yourself\
 immensely wet. Smart move, Sherlock.", 100))

class Jukebox(Misc):
    def __init__(self):
        self.name = "jukebox"
        self.songs = ["Toot-scootin' Boogie", "My Achy Breaky Fart",
        "The Devil Passed Gas in Georgia", "Bathroom Blues"]
        self.requirement = "My Achy Breaky Fart"
        self.unlock = False
        self.class_ = False

    def take(self, scene):
        print(fill("You damn near give yourself an aneurysm trying to lift the jukebox.\
 Better stop before you hurt yourself.",100))
 
    def play(self):
        print(fill("You approach the jukebox with some hip songs in mind, but you discover\
 that everything here seems rather country. And the songs have an odd theme, but you can't pull your\
 finger on it...",100))
        print()
        print("Songs available in the jukebox:")
        i = 1
        for song in self.songs:
            print("{}. {}".format(i, song))
            i += 1
        print()
        print("Go ahead, pick a number to listen to.")
        run = True
        while run:
            print()
            ui = input("> ")
            if ui == "1":
                print(""""Out in the country, in this outhouse of mine..." """)
                print(fill("That's odd, even the lyrics are different. Oh well, maybe\
 it's the bar's gimmick. This song makes you want a drink.", 100))
                run = False
            elif ui == "2":
                print(fill(""""You can tell the world you never was my girl,\
 but I'll burn the can up before I'm gone..." """,100))
                print(fill("As you stand there thinking about how weird these songs are,\
 a girl in the bar lets out a whoop, stands on her table, and starts doing the hoe\
down. A guy sitting at the bar watches her with dinner-plate eyes. You can practically\
 see his heart beating out of his chest.",100))
                self.unlock = True
                run = False
            elif ui == "3":
                if not self.class_:
                    print(fill(""""The devil went down to Georgia, he had some gas that\
 was sure to kill..." """,100))
                    print(fill("The lyrics weave together quite a story and you find yourself dancing\
 to the tune of the fiddle. The bar lets out a drunken cheer when you're done.",100))
                    print()
                    print("+5 class")
                    player.classy += 5
                    self.class_ = True
                else:
                    print(fill(""""The devil went down to Georgia, he had some gas that\
 was sure to kill..." """,100))
                    print(fill("The lyrics weave together quite a story and you find yourself dancing\
 to the tune of the fiddle. The bar lets out a drunken cheer when you're done.",100))
                run = False
            elif ui == "4":
                print(fill(""""All the paper in the world couldn't save you, all the crud\
 that you have inside..." """,100))
                print(fill("This one seems more on the rock side than the country side. The\
 bar boos and demands a different song.",100))
                run = False
            else:
                print("Just a number, 1-4.")

class SteamedLobster(Misc):
    def __init__(self):
        self.name = "steamed lobster"
        
    def take(self, scene):
        print(fill("How did you even know the chef had a steamed lobster? Are you some kind\
 of game replayer? Or just a code reader? Weirdo. Nah, I'm joking. You're awesome.",100))

class PunchingBag(Misc):
    def __init__(self):
        self.name = "punching bag"

    def take(self, scene):
        print("You can barely move the bag, nonetheless lift it.")


#                    -----======(   ENEMIES   )======-----

class Enemy:
    def __init__(self):
        raise NotImplementedError("This Enemy object has no attributes")
		
    def look(self):
        print(fill(items[self.name], 100))
	    
    def take(self, scene):
	    print("stuff")
		
class Hobo(Enemy):
	def __init__(self):
		self.name = "hobo"
		self.hp = 10
		self.damage = randint(3,5)
		self.inventory = ["shank"]

class Drunk(Enemy):
	def __init__(self):
		self.name = "drunk"
		self.hp = 20
		self.damage = randint(5,8)
		self.inventory = ["bottle", "leather wallet",
		"cell phone"]

class Boxer(Enemy):
	def __init__(self):
		self.name = "boxer"
		self.hp = randint(40, 60)
		self.damage = randint(8, 10)
		self.money = randint(20,40)



#                    -----======(   NPCs   )======-----

class Npc:
    def __init__(self):
        raise NotImplementedError("This NPC object has no attributes")
        
    def look(self):
        print(fill(items[self.name],100))

class Attendant(Npc):
    def __init__(self):
        self.name = "attendant"
        
    def talk(self):
        random = randint(1, 3)
        if random == 1:
            print("You ask the attendant why he seems to hate you so much.")
            print("""He blushes. "I just have to act like a snob or I lose my job." """)
            print(fill("Well, that's surprising. He rises up a few notches in your eyes. Never\
 judge a book by it's cover, kids.",100))
        if random == 2:
            print(""""Oh, what do you want?" the attendant asks.""")
            print(fill("You balk at him. How can he be so rude? Maybe someone pissed in his\
 wheaties. Maybe his girlfriend just broke up with him. Maybe he has a term paper due\
 tomorrow. You ask him what his deal is.", 100))
            print(fill(""""I really like that guy standing on W 8th, but he acts like\
 I don't exist." """, 100))
            print(fill("Not what you were expecting. You tell him there's a chance\
 and walk away awkwardly.",100))
        if random == 3:
            print("You walk up to the attendant but his glare sends you walking the other way.")
            print(""""Good talk," you mumble to yourself.""")
        
    def buy(self):
        if (player.classy >= 100 and player.money >= 100):
            print(fill(""""My my, you certainly clean up nice. The show started\
 10 minutes ago, but at least now you can get in!" """, 100))
            print()
            print(fill("You finally buy a ticket to the play. You should\
 feel classy and rich; and hopefully accomplished.", 100))
            print()
            print("Congratulations, you won the game!")
            exit()
        else:
            print(fill("The attendant looks at you like you're crazy\
 and promptly shoos you away. Don't want the well-off to see your\
 un-classy self.",100))
            print()
            print("Sorry, you still need a class of 100 and $100.")
    
    def sell(self):
        print("What could you possibly sell to this guy?")

class Vendor(Npc):
    def __init__(self):
        self.name = "street vendor"
        self.inventory = ["hot dog", "hot dog", "hot dog",
                     "taco", "taco", "taco",
                     "pretzel", "pretzel", "pretzel",
                     "pizza", "pizza", "pizza",
                     "glass pipe", "utility knife",
                     "hat",
                     "solid tie", "patterned tie",
                     "bracelet"]
                     
    def buy(self):
        print("This is what the vendor has available:")
        print()
        print("Food:")
        for item in self.inventory:
            item = real_item[item]
            if isinstance(item, CashConsumable):
                print(item)
        print()
        print("Class:")
        for item in self.inventory:
            item = real_item[item]
            if isinstance(item, CashClassy):
                print(item)
        print()
        print("Weapons:")
        for item in self.inventory:
            item = real_item[item]
            if isinstance(item, CashWeapons):
                print(item)
                
    def talk(self):
        print("This is what the vendor has available:")
        print()
        print("Food:")
        for item in self.inventory:
            item = real_item[item]
            if isinstance(item, CashConsumable):
                print(item)
        print()
        print("Class:")
        for item in self.inventory:
            item = real_item[item]
            if isinstance(item, CashClassy):
                print(item)
        print()
        print("Weapons:")
        for item in self.inventory:
            item = real_item[item]
            if isinstance(item, CashWeapons):
                print(item)
                
    def sell(self):
        print("What do you want to sell?")

class StreetDude(Npc):
    def __init__(self):
        self.name = "dude"
        self.description = items["dude"]
        self.inventory = ["map"]
        self.requirement = "taco"
        self.visited = 0

    def talk(self):
        found = False
        if self.visited == 1:
            print(fill("The dude tries to talk to you through a mouthful of beef and cheese,\
 but he's impossible to understand and you walk away in frustration.", 100))
        else:
            found = False
            for item in player.inventory:
                if item.name == self.requirement:
                    found = True
                    print("You get another glimpse of the golden tooth.")
                    print(fill(""""Righteous! I know this taco's legs are tired, 'cause it's\
 been runnin' through my mind ALL day. Here's the map, hope it helps!" """,100))
                    player.inventory.remove(item)
                    for item in self.inventory:
                        self.inventory.remove(item)
                        item = real_item[item]
                        player.inventory.append(item)
                    print()
                    print("Map added to inventory.")
                    self.visited = 1
                    break
            if not found:
                print(fill("You approach homeboy. He grins at you from underneath\
 a pair of shades, one gold incisor glinting in the light.",100))
                print(fill(""""Hey you," he says, "how's about getting me a taco? I'll make it\
 worth your while! I used to get lost on this block all the time, but this kickass\
 map saved my life. I don't need it anymore, but I *really* need a taco." """,100))
                print()
                print("This sounds like a good deal...maybe you should find the guy a taco...")
                
    def buy(self):
        print("There's nothing to buy off this guy.")
        
    def sell(self):
        print("There's nothing he wants to buy off of you.")

class Bartender(Npc):
    def __init__(self):
        self.name = "bartender"
        self.inventory = ["long island", "limoncello", "mint julep"]
        
    def buy(self):
        print("This is what the bartender has available:")
        print()
        for item in self.inventory:
            item = real_item[item]
            print(item)
            
    def talk(self):
        print("This is what the bartender has available:")
        print()
        for item in self.inventory:
            item = real_item[item]
            print(item)
            
    def sell(self):
        print("What do you want to sell?")

class BarGuy(Npc):
    def __init__(self):
        self.name = "guy"
        self.talked = False
        self.given = False

    def talk(self):
        if not self.talked:
            self.talked = True
            print("You approach the anxious-looking guy. He grins at you creepily,\
 realizes it, and tones it down to a smile.")
            sleep(0.8)
            print(fill(""""Hi!" he says, a bit too loudly. "I saw you come in, you\
 look like someone who could help me. There's this girl here, she's an absolute\
 10. I just can't find the courage to talk to her. Maybe you could soften her up\
 a bit, so I can go in for the kill? I promise I'll make it worth your while.\
 He finishes his spiel and you pause, contemplating. You really\
 don't want to help him, but you also want to help yourself. Maybe it'll be worth\
 it...""",100))
            sleep(3)
        else:
            girl = real_item["girl"]
            if not girl.unlock:
                print(fill(""""The guy looks at you, full of apprehension. "Have you done it yet?\
 Does she want to talk to me? Please, I know you can do it!" """,100))
                print("His pleading is pathetic. You almost feel bad for him. Almost.")
            else:
                if not self.given:
                    print(fill(""""What?!" he yells. "You did it? She wants to talk to me?\
 Oh you're amazing! You're fantastic! You're the best! Here, have some cash, it's all\
 I have. And I'll give you a tip - if you want a quick boost to make yourself seem\
 a little fancier, try buying a drink. Always works for me. And I hear there's a song\
 on the jukebox that the bar really likes..." """,100))
                    self.given = True
                    player.money += 20
                else:
                    print(fill("The guy is gone. You search the bar and see him talking to\
 the dancing girl. She looks uninterested. Oh well. You tried.",100))
    
    def buy(self):
        print("There's nothing to buy off of this guy.")
    
    def sell(self):
        print("He doesn't want to buy anything off of you.")

class BarGirl(Npc):
    def __init__(self):
        self.name = "girl"
        self.talked = False
        self.unlock = False

    def talk(self):
        guy = real_item["guy"]
        if not guy.talked:
            print(fill("You confidently walk up to the girl. Sitting at her table are 3 of\
 her friends who don't acknowledge you at all. She eyeballs you up and down as you\
 get closer. Before you can introduce yourself, she goes back to talking with her friends,\
 pretending you don't exist.",100))
        else:
            if not self.talked:
                self.talked = True
                print(fill("The girl is sitting with her friends. They ignore you as\
 you walk up. ",100))
                sleep(1)
                print(fill(""""Hi there," you say, "can I ask you a question?" """,100))
                print(fill("""She reluctantly peels herself away from her companions and turns\
 toward you. "Yes?" she says. "Can I help you with something?" """,100))
                sleep(2)
                print()
                if player.classy >= 20:
                    print("You channel your inner class and put on the charm.")
                    sleep(0.7)
                    print(fill("""You begin your lie smoothly. "So, I have a bet with a friend.\
 I said that you probably have a hillbilly name. He bet me 10 dollars that you don't; he said\
 angels don't have names." Her offended look changes to one of flattery.""",100))
                    print(fill("She takes in your clothes and appearance, trying to figure out\
 how much you're worth.",100))
                    sleep(4)
                    print()
                    if player.money >= 50:
                        print("It looks like you're up to par.")
                        sleep(0.7)
                        print(fill(""""That's really sweet," she says. "Who's your friend?" You\
 point to the guy at the bar. He quickly looks away, as if he wasn't watching. She smiles. "I\
 tell you what, I'm not having a good enough time yet. If you can get this place to be a little\
 more lively, I'll talk to your friend." Lively huh? There's gotta be a way to get this place\
 riled up...""",100))
                        sleep(6)
                    else:
                        print(fill("Apparently, you aren't worth talking to. Some girls can smell\
 money from a mile away, and you don't have enough of it.",100))
                else:
                    print(fill("You aren't classy enough to hold her interest, but you try\
 anyway. You promised you would. You can't even ask her name before her friends rope her\
 back in. Ah well.",100))
            else:
                jb = real_item["jukebox"]
                if jb.unlock == True:
                    print(fill("""The girl grins at you from atop the table. "That was great!"\
 she says. "I haven't danced like that since college! Tell your friend to come over here,\
 I'm ready to meet him." Success! You need to go tell that guy the good news.""",100))
                    self.unlock = True
                else:
                    print(fill("The girl is done talking to you for now, she made her goal\
 very clear. Liven this place up and get the party started.",100))
        
    
    def buy(self):
        print("She has nothing to sell you.")
        
    def sell(self):
        print(fill("You try to sell her your body, but she doesn't exactly appreciate it.",100))

class OldMan(Npc):
    def __init__(self):
        self.name = "old man"
        self.requirement = "mint julep"
        
    def talk(self):
        found = False
        for item in player.inventory:
            if item.name == self.requirement:
                found = True
        if found == True:
            print(""""AYYYYYY!" he yells. "Yuuu got it!" """)
            print()
            print(fill("""The old man is happy as a clam. He eyes you up and down and apparently deems you\
 worthy, as he starts digging into his pockets. "Here," he says, "sssumthin' for yer trubles." """,100))
            print()
            player.inventory.append(LotteryTicket())
            player.inventory.append(Cigar())
            print("Lottery ticket added to inventory.")
            print("Cigar added to inventory.")
            
        else:
            print(fill("You warily approach the old man in the wheelchair. He shows off his yellowed\
 teeth in a buck-tooth grin.",100))
            print(fill(""""Well hy thrr ssssonny," he slurs. "How'sss bouts gettin' me a daa-rink? Sumthin\
 witttthh a good shotskie of bourbon!" """,100))
            print()
            print(fill("It seems this man's been cut off. Oh well, what could one more drink hurt? Now you\
 just need to get him something with bourbon in it...",100))
 
    def buy(self):
        print("There's nothing to buy off of this guy.")
        
    def sell(self):
        print("He doesn't want to buy anything.")
    

class PoolShark(Npc):
    def __init__(self):
        self.name = "pool shark"
        self.money = 300

    def talk(self):
        print("I'm lazy. He wants to play pool.")
    
    def play(self):
        
        #Need to add sleeps
        #This method is long as a mf and when the player gets in it,
        #THERE'S NO WAY OUT
        #Don't even care about fixing it right now tbh.
        
        print(fill("You try to look intimidating and swagger your way across\
 the room to the pool shark. Too bad you trip on your own feet and knock somebody's\
 beer over. Impressive, you are.",100))
        print("Have you played this guy before?")
        print()
        run = True
        while run:
            play = input("> ").lower()
            if play == "yes" or play == "y":
                run = False
            elif play == "no" or play == "n":
                print(fill("The shark lays out the name of the game. You each\
 have three balls to hit. If you can sink more of 'em in the pockets than him, you win\
 all the money. If there is a tie, you get your money back. If he\
 gets more in than you, he wins your money. You better not scratch that\
 8-ball at the end...",100))
                print()
                run = False
            else:
                print("Sorry, you wanted to play him. He's not letting you go now. Yes or no?")
                print()
        print("How much do you want to bet?")
        print()
        run = True
        while run:
            try:
                bet = float(input("> "))
                if bet > player.money:
                    print("You can't afford to make that bet.")
                    print()
                elif bet > self.money:
                    print("The pool shark can't afford a bet that high.")
                    print()
                else:
                    print("You make a bet of ${:.2f}.".format(bet))
                    sleep(1)
                    print()
                    run = False
            except:
                print("Type a number in there, dunderhead.")
                print()
        player_score = 0
        shark_score = 0
        eight_ball = randint(1,6)
        peight_ball = randint(1,6)
        scratch = randint(6,20)
        break_ = randint(1,2)
        ball = randint(1, 2)
        if break_ == 1:
            print("You grab a cue and break.")
            sleep(0.6)
        elif break_ == 2:
            print("The shark grabs a cue and breaks.")
            sleep(0.6)
        if ball == 1:
            print("Looks like you're solids!")
            type = "solids"
            sleep(1)
            print()
        elif ball == 2:
            print("Looks like you're stripes!")
            type = "stripes"
            sleep(1)
            print()
        if type == "solids":
            ball_one = randint(1,2)
            ball_two = randint(5,6)
            ball_three = randint(3,4)
            ball_four = 7
        elif type == "stripes":
            ball_one = randint(9,10)
            ball_two = randint(13,14)
            ball_three = randint(11,12)
            ball_four = 15
        
        #Overkill, but takes care of the problem with
        #balls repeating themselves (even if you've already
        #hit them in). Whoopsie!
        
        turn = 0
        run = True
        while run:
            if turn == 0:
                print("You have two good shots. Do you hit ball {} or\
 {}?".format(ball_one, ball_two))
            if turn == 1:
                print("You see two more good shots. Should you hit the {} ball\
 or the {} ball?".format(ball_three, ball_four))
            if turn == 2:
                print("Moment of truth! Pick a pocket for the 8-ball, a number\
 between 1 and 6.")
            print()
            if turn < 2:
                try:
                    shot = int(input("> "))
                    if shot == ball_one:
                        ball = ball_one
                    elif shot == ball_two:
                        ball = ball_two
                    elif shot == ball_three:
                        ball = ball_three
                    elif shot == ball_four:
                        ball = ball_four
                        
                    #It's midnight and I can't remember why this is here.
                    #But it works.
                    
                    else:
                        print("Please choose {} or {}.".format(ball_one, ball_two))
                        continue
                except:
                    print("Please choose a number.")
                    continue
                print("You aim your sights at the {} ball,\
 line up your shot, hit the cue ball, and...".format(ball))
                sleep(1)
                miss = randint(1,4)
                if miss == 1:
                    print("Damn it, you missed!")
                    sleep(0.5)
                    print()
                    turn += 1
                else:
                    print("You got it!")
                    sleep(0.5)
                    print()
                    player_score += 1
                    turn += 1
                print("Now it's the pool shark's turn.")
                if type == "solids":
                    ball_one = randint(9,12)
                    ball_two = randint(13,15)
                elif type == "stripes":
                    ball_one = randint(1,4)
                    ball_two = randint(5,7)
                if turn == 1:
                    print("He attempts to hit the {} ball in...".format(ball_one))
                if turn == 2:
                    print("He attempts to hit the {} ball in...".format(ball_two))
                sleep(1)
                
                #This REALLY pisses me off, because even though I set the odds of
                #him hitting the same ball as high as I could, it STILL
                #happens. Whatever. Maybe no one will notice it. >_>
                #This method is complicated enough without me fixing that crap.
                
                pmiss = randint(1,4)
                if pmiss == 1:
                    print("Oh, he missed it!")
                    sleep(0.6)
                    print()
                else:
                    print("He sunk it!")
                    sleep(0.6)
                    print()
                    shark_score += 1
            elif turn == 2:
                try:
                    eight_shot = int(input("> "))
                    if eight_shot == eight_ball:
                        print("You got the 8-ball in! Your mom would be so proud!")
                        sleep(0.6)
                        print()
                        player_score += 1
                    else:
                        if scratch == 6:
                            print("Oh lordy, it looks like you scratched. That's\
 some unlucky business right there. Sorry bud, you automatically lose!")
                            print("-${:.2f}".format(bet))
                            player.money -= bet
                            self.money += bet
                            break
                        else:
                            print("You missed! Ah well. Happens to the best of us.")
                            sleep(0.6)
                            print()
                except:
                    print("Please choose a number.")
                    continue
                print("The shark attempts to hit his 8-ball shot...")
                sleep(1)
                if peight_ball == 1:
                    print("He got it! What a lucky shot!")
                    sleep(0.6)
                    print()
                    shark_score += 1
                elif peight_ball == 2:
                    print("He scratched! Would you look at that, you won!")
                    print("+${:.2f}".format(bet))
                    player.money += bet
                    self.money -= bet
                    break
                else:
                    print("Whoopsie, he huffed it.")
                    sleep(0.6)
                    print()
                if player_score == 1:
                    print("The game is over! You had {} successful shot.".format(player_score))
                else:
                    print("The game is over! You had {} successful shots.".format(player_score))
                if shark_score == 1:
                    print("The pool shark had {} successful shot.".format(shark_score))
                else:
                    print("The pool shark had {} successful shots.".format(shark_score))
                sleep(1)
                if player_score > shark_score:
                    print("Congratulations, you won!")
                    sleep(0.8)
                    print("+${:.2f}".format(bet))
                    player.money += bet
                    self.money -= bet
                    run = False
                elif player_score == shark_score:
                    print("It was a tie!")
                    sleep(0.8)
                    print("The pool shark hands you your money back.")
                    run = False
                else:
                    print("Ouch, sorry, you lost!")
                    sleep(0.8)
                    print("-${:.2f}".format(bet))
                    player.money -= bet
                    self.money += bet
                    run = False
            

        #I. Cannot. Tell you. How many times. I have played this
        #billiards game. I can't. Do it. Anymore.
            
            
            

    def buy(self):
        print("He doesn't have anything to sell you.")
    
    def sell(self):
        print(fill("He would buy your soul if he could...but he doesn't want\
 anything you have right now.",100))

class Cashier(Npc):
    def __init__(self):
        self.name = "cashier"
        self.inventory = ["scarf", "plain tee",
        "graphic tee", "jeans", "slacks", "fancy shoes"]
        
    def buy(self):
        print("This is what the store has available:")
        print()
        for item in self.inventory:
            item = real_item[item]
            print(item)
    
    def sell(self, item):
        print("What do you want to sell?")

class FancyWoman(Npc):
    def __init__(self):
        self.name = "woman"
        self.money = randint(30,50)
    
    #Must implement talk method
    
    def buy(self):
        print("You really think she needs your money?")
        
    def sell(self):
        print("You really think she wants to buy something off of you?")


class Chef(Npc):
    def __init__(self):
        self.name = "chef"
        self.inventory = ["bruschetta", "crostini",
        "insalata caprese"]
      
    #Must implement talk method
    
    def buy(self):
        print("This is what the chef has available:")
        print()
        for item in self.inventory:
            item = real_item[item]
            print(item)
    
    def sell(self):
        print("Sorry, the chef does not buy food back.")
        
        
class Fighter(Npc):
    def __init__(self):
        self.name = "fighter"
        self.inventory = ["boxing gloves"]
        self.requirement = "gum"
        self.unlock = False
        self.talked = False
        self.dead = False
    
    def talk(self):
        found = False
        if self.talked:
            if self.dead:
                print(fill("The fighter is still out cold in the middle of the ring. Is\
 someone going to come pick him up?",100))
            else:    
                print("The fighter looks pathetic. He must really want that gum.")
        if not self.talked:
            print(fill("The heavily-muscled fighter looks distressed. You\
 ask him what's up.",100))
            print(fill(""""Man, I've got a fight tonight," he laments, "and\
 I don't have anything to chew on. I always bring gum with me, I'm\
 so stupid!" Though he looks it, you assure him he's not stupid.\
 Maybe you can help this poor guy out...""",100))
            print()
            self.talked = True
        for item in player.inventory:
            if item.name == self.requirement:
                found = True
                self.unlock = True
                if self.unlock:
                    print(fill("""The fighter beams at you. "Well I'll be a monkey's\
 uncle!" You admit you don't know what that means. "Me neither. But thanks for\
 the gum, now it's time to win!" He pops it in his mouth without a second look. "Here,"\
 he says, handing you his boxing gloves. "I think you need these more than I do. I'm\
 goin' in bareback!" He puts his fists up and punches the air a few times.\
 Climbing in the ring after his opponent, he starts his fight and promptly\
 gets knocked out.""",100))
                    print()
                    player.inventory.append(BoxingGloves())
                    player.inventory.remove(item)
                    print("Boxing gloves added to inventory.")
                    self.dead = True
        if not found:
            pass
    
    def buy(self):
        print("He doesn't have anything to sell.")
        
    def sell(self):
        print("He doesn't want to buy anything off of you.")

#                    -----======(   ITEMS   )======-----

real_item = {"attendant":Attendant(),
             "hat":Hat(),
             "scarf":Scarf(),
             "map":Map(),
             "hot dog":HotDog(),
             "taco":Taco(),
             "pretzel":Pretzel(),
             "pizza":Pizza(),
             "fists":Fists(),
             "glass pipe":GlassPipe(),
             "pipe":GlassPipe(),
             "utility knife":UtilityKnife(),
             "knife":UtilityKnife(),
             "broken bottle":BrokenBottle(),
             "bottle":BrokenBottle(),
             "boxing gloves":BoxingGloves(),
             "solid tie":SolidTie(),
             "patterned tie":PatternedTie(),
             "bracelet":Bracelet(),
             "shank":Shank(),
             "dirty shoes":DirtyShoes(),
             "piss puddle":PissPuddle(),
             "puddle":PissPuddle(),
             "piss":PissPuddle(),
             "blanket":Blanket(),
             "pillow":Pillow(),
             "suitcase":Suitcase(),
             "used gum":Gum(),
             "gum":Gum(),
             "newspaper":Newspaper(),
             "apple":Apple(),
             "dumpster":Dumpster(),
             "cardboard box":CardboardBox(),
             "box":CardboardBox(),
             "leather wallet":LeatherWallet(),
             "wallet":LeatherWallet(),
             "cell phone":CellPhone(),
             "jukebox":Jukebox(),
             "long island":LongIsland(),
             "limoncello":Limoncello(),
             "mint julep":MintJulep(),
             "cigar":Cigar(),
             "lottery ticket":LotteryTicket(),
             "ticket":LotteryTicket(),
             "plain tee":PlainTee(),
             "graphic tee":GraphicTee(),
             "jeans":Jeans(),
             "slacks":Slacks(),
             "fancy shoes":FancyShoes(),
             "coffee":Coffee(),
             "clock":Clock(),
             "calendar":Calendar(),
             "purse":Purse(),
             "lipstick":Lipstick(),
             "lighter":Lighter(),
             "used napkin":UsedNapkin(),
             "tampon":Tampon(),
             "bruschetta":Bruschetta(),
             "crostini":Crostini(),
             "insalata caprese":InsalataCaprese(),
             "waterfall":Waterfall(),
             "pin":Pin(),
             "piano":Piano(),
             "steamed lobster":SteamedLobster(),
             "punching bag":PunchingBag(),
             "street vendor":Vendor(),
             "vendor":Vendor(),
             "hobo":Hobo(),
             "drunk":Drunk(),
             "dude":StreetDude(),
             "street dude":StreetDude(),
             "bartender":Bartender(),
             "guy":BarGuy(),
             "girl":BarGirl(),
             "old man":OldMan(),
             "man":OldMan(),
             "pool shark":PoolShark(),
             "pool":PoolShark(),
             "shark":PoolShark(),
             "cashier":Cashier(),
             "woman":FancyWoman(),
             "chef":Chef(),
             "boxer":Boxer(),
             "fighter":Fighter()
             }




#                    -----======(   PLAYER   )======-----

class Player:
    def __init__(self):
        self.hp = 100
        self.money = 100
        self.classy = 0
        self.inventory = [Fists(), Lipstick(), BoxingGloves(), LotteryTicket()]
        self.drank = 0

    def print_inventory(self):
        print("Weapons:")
        for item in self.inventory:
            if (isinstance(item, Weapons) or
            isinstance(item, CashWeapons)):
                print("* {}".format(item))
        print()
        print("Class Items:")
        for item in self.inventory:
            if isinstance(item, Classy) or isinstance(item, CashClassy):
                print("* {}".format(item))
        print()
        print("Food:")
        for item in self.inventory:
            if isinstance(item, Consumable) or isinstance(item, CashConsumable):
                print("* {}".format(item))
        print()
        print("Miscellaneous:")
        for item in self.inventory:
            if isinstance(item, Misc):
                print("* {}".format(item))
        print()
        print("Money: ${:.2f}".format(self.money))
 




#                    -----======(   SCENES   )======-----

look_text = {"box_office":"You look around the box office. There is an attendant behind a pane of glass. He looks\
 at you like you're scum. There are no items on the ground. There are no people nearby. There are\
 no enemies to fight. To your north is W 8th Avenue, a dirty street with some personality to it.",
 
              "street1":"You look around W 8th Ave. There is a dude leaning against a street lamp with a\
 toothpick in his mouth. He looks interesting. There are no items on the ground. There are no enemies\
 to fight. To your north is an alleyway that looks rather dangerous. To the east is E 8th Ave, just as\
 dirty a street as W 8th Ave. To the south is the box office with the snooty attendant, and to the west is a\
 street vendor peddling his wares.",
 
              "street2":"You look around E 8th Ave. It's mildly less exciting than W 8th Ave. In fact, it's\
 downright ghostly with no one around. A flickering street light is giving you a headache. Without\
 any enemies to fight or things to do, you might as well move on. To your north is 45th St. To your east,\
 a rootin'-tootin' country bar. That might be fun. Nothing but an ominous-looking manhole cover to the south,\
 and to your west is good ol' W 8th Ave.",
 
              "street3":"You look around 45th St. It's even more boring than E 8th, as there is no flickering\
 street light. At least there are multiple surrounding buildings, such as a fancy restaurant (Eau de la Cul) to\
 the west, an intimidating-looking boxing arena to the north, and an upscale clothing store to the east. To your\
 south is E 8th St.",
              
              "street_vendor":"Multiple vendors litter the sidewalk. You see one in particular that's selling a\
 smorgasbord of items. It has everything from dull weapons to cheap food to even cheaper accessories. He grins at\
 you with a mossy smile. You could totally buy something from the vendor. The only way to go is back east toward W\
 8th Ave.",
              
              "alleyway":"A pungent alleyway. There's a dumpster, a cardboard box that may or may not house\
 a hobo, his pillow, his blanket, and a gleaming suitcase. A nearby streetlight flickers and then burns out. Everything\
 goes dark and it reeks of pee. The only way to go is back south the way you came, to W 8th Ave.",
              
              "manhole":"This part of the game is not fully developed yet.",
              
              "bar":"A country bar where everyone is having a darn tootin' good time. There's a jukebox with all the\
 down home hits, a twitching man at the bar, a gorgeous girl at a table with her friends, several drunks, and an old\
 man sitting in a wheelchair. The bartender is swamped with patrons. There's a pool shark standing by the table that\
 looks like he wants to play a game of pool with you. You edge closer to the bar and consider buying a drink. Maybe\
 there's a drunk to fight too...",
              
              "clothes_store":"An upscale clothing store complete with its own teenage cashier, blowing bubbles and popping\
 her gum. Obnoxious, but you could buy something off of her. You see a door labeled 'Break Room' to your east. To your west\
 is the front door, leading to 45th St.",
              
              "break_room":"A dreary breakroom. All that's in here is some chairs, a clock, and a calendar. Actually,\
 upon further examination, you see a purse sitting on the table. Hmm...do you feel lucky? Well, do ya, punk? To your\
 west is the clothing store you came from.",
              
              "restaurant":"Ahh, Eau de la Cul. There's a grand piano, a luxurious waterfall, and a fancy old woman sitting\
 solitary at a table. The chef in the back makes the most delicious cuisines, maybe you could buy something off of him. He\
 looks like he might want to talk to you as well...",
              
              "boxing_arena":"You look around the boxing arena. It seems very legitimate, not one\
 of those new fangled fight-club-like places. You can't talk about those anyway. A fighter stands\
 in the corner, holding his jaw. A boxer is jumping around in the ring, seemingly pointing at you\
 and wanting to fight. Maybe you can make some money off of him. He looks like he'd be up for a\
 couple rounds. The only way to go is back the way you came, south to 45th St."}



class Scene:
    
    def __init__(self):
        raise NotImplementedError("Raw scene object has no attributes.")
    
    def enter(self):
        print("If this\
 shows up, this scene is not yet implemented. I need to implement\
 the function enter().")
 
    def look(self):
        text = fill(look_text[self.name], 100)
        return text

class Engine():
    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene("finished")

        while current_scene != last_scene:
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)

        #current_scene.enter()
        

class BoxOffice(Scene):

    room_objects = ["box office"]
    #Objects that are fixed and can only be looked at
    room_items = ["ticket"]
    #Objects that can be taken or interacted with
    room_characters = ["attendant"]
    #People that can be interacted with but not fought
    room_enemies = []
    #People that can be fought

    def __init__(self):
        self.name = "box_office"
        self.fresh_arrival = True
        self.north = True
        self.east = False
        self.south = False
        self.west = False

    def enter(self):
        if self.fresh_arrival:
            self.fresh_arrival = False
            print(fill("You stand in front of the box office at the Majestic\
 theater. All you want in this world right now is to buy a ticket to The\
 Phantom of the Opera.", 100))
            print("The attendant looks at you with disdain.")
            print(fill(""""I'm sorry, but you're going to have to clean\
 up your act if you want in. I'm  not selling you a ticket looking\
 like *that*. Besides, you don't have enough money. It's $100 for a ticket." """, 100))
            print("Defeated, you turn away.")
            print()
            print(fill("You are facing the box office.\
 The attendant looks at you with contempt in his eyes.\
 He will not let you in unless you have a class of 100 and $100.", 100))
            print()
            print("Type 'help' for a list of commands.")
            value = UserInput(box_office)
            direction = value.user_input()
            if direction == "north":
                return "street1"

        if not self.fresh_arrival:
            print(fill("You are facing the box office. The attendant looks at you with contempt\
 in his eyes. He will not let you in unless you have a class level of 100 and $100.", 100))
            value = UserInput(box_office)
            direction = value.user_input()
            if direction == "north":
                return "street1"
 

class Street1(Scene):

    room_objects = []
    room_items = ["map"]
    room_characters = ["dude"]
    room_enemies = []

    def __init__(self):
        self.name = "street1"
        self.fresh_arrival = True
        self.north = True
        self.east = True
        self.south = True
        self.west = True

    def enter(self):
        if self.fresh_arrival:
            self.fresh_arrival = False
            print(fill("You make your way to W 8th Ave. A shady-looking dude is standing on\
 the sidewalk, staring at the sky. He spies you and grins. It looks like he wants to talk to\
 you.",100))
            print()
            print(fill("You are standing in the middle of W 8th Ave. The smell of the street makes\
 you want to vomit. A cool dude leans against a street light, teeth glinting. His dark\
 sunglasses strike you as odd for 7:30 in the evening.", 100))
            value = UserInput(street1)
            direction = value.user_input()
            if direction == "north":
                return "alleyway"
            if direction == "east":
                return "street2"
            if direction == "south":
                return "box_office"
            if direction == "west":
                return "street_vendor"

        if not self.fresh_arrival:
            print(fill("You are standing in the middle of W 8th Ave. The smell of the street makes\
 you want to vomit. A cool dude leans against a street light, teeth glinting. His dark\
 sunglasses strike you as odd for 7:30 in the evening.", 100))
            value = UserInput(street1)
            direction = value.user_input()
            if direction == "north":
                return "alleyway"
            if direction == "east":
                return "street2"
            if direction == "south":
                return "box_office"
            if direction == "west":
                return "street_vendor"
 

class Street2(Scene):

    room_objects = []
    room_items = []
    room_characters = []
    room_enemies = []

    def __init__(self):
        self.name = "street2"
        self.fresh_arrival = True
        self.north = True
        self.east = True
        self.south = True
        self.west = True

    def enter(self):
        if self.fresh_arrival:
            self.fresh_arrival = False
            print(fill("You arrive at E 8th St. It reminds you of a dream you had\
 as a kid, one where you ran into the street to grab a briefcase and nearly got run over\
 by a car shaped like a dog. You were an odd kid.", 100))
            print()
            print(fill("You are standing at the corner of E 8th St. Nothing here but\
 the sound of water trickling into the sewer grates. To your north is 45th St. In the\
 eastern direction you see a country bar. To the south lies a manhole cover to the sewers.\
 Finally, to the west is W 8th St.", 100))
            value = UserInput(street2)
            direction = value.user_input()
            if direction == "north":
                return "street3"
            if direction == "east":
                return "bar"
            if direction == "south":
                return "manhole"
            if direction == "west":
                return "street1"
            
        if not self.fresh_arrival:
            print(fill("You are standing at the corner of E 8th St. Nothing here but\
 the sound of water trickling into the sewer grates. To your north is 45th St. In the\
 eastern direction you see a country bar. To the south lies a manhole cover to the sewers.\
 Finally, to the west is W 8th St.", 100))
            value = UserInput(street2)
            direction = value.user_input()
            if direction == "north":
                return "street3"
            if direction == "east":
                return "bar"
            if direction == "south":
                return "manhole"
            if direction == "west":
                return "street1"
 

class Street3(Scene):

    room_objects = []
    room_items = []
    room_characters = []
    room_enemies = []

    def __init__(self):
        self.name = "street3"
        self.fresh_arrival = True
        self.north = True
        self.east = True
        self.south = True
        self.west = True

    def enter(self):
        if self.fresh_arrival:
            self.fresh_arrival = False
            print(fill("You arrive at 45th St. A man is standing on the street\
 corner, playing guitar and singing. It looks like he's in his underwear. Doesn't\
 this guy belong in Times Square?", 100))
            print()
            print(fill("You are standing on 45th St. There is nothing much to do here.\
 To your north is a kickass boxing arena. To your east, a snooty-looking clothing store.\
 The west direction holds a fancy restaurant, 'Eau de la Cul.' To the south is E 8th St.",100))
            value = UserInput(street3)
            direction = value.user_input()
            if direction == "north":
                return "boxing_arena"
            if direction == "east":
                return "clothes_store"
            if direction == "south":
                return "street2"
            if direction == "west":
                return "restaurant"
            
        if not self.fresh_arrival:
            print(fill("You are standing on 45th St. There is nothing much to do here.\
 To your north is a kickass boxing arena. To your east, a snooty-looking clothing store.\
 The west direction holds a fancy restaurant, 'Eau de la Cul.' To the south is E 8th St.", 100))
            value = UserInput(street3)
            direction = value.user_input()
            if direction == "north":
                return "boxing_arena"
            if direction == "east":
                return "clothes_store"
            if direction == "south":
                return "street2"
            if direction == "west":
                return "restaurant"
 

class StreetVendor(Scene):

    room_objects = []
    room_items = ["hot dog", "taco", "pretzel", "pizza",
    "glass pipe", "pipe", "utility knife", "knife", "hat",
    "solid tie", "patterned tie", "bracelet"]
    room_characters = ["street vendor", "vendor"]
    room_enemies = []

    def __init__(self):
        self.name = "street_vendor"
        self.fresh_arrival = True
        self.north = False
        self.east = True
        self.south = False
        self.west = False

    def enter(self):
        if self.fresh_arrival:
            self.fresh_arrival = False
            print(fill("You move to the west and arrive at the street vendor\
 area. Immediately you are bombarded by middle-aged men trying to sell you\
 selfie sticks. Brushing them away, you approach one of the tables.", 100))
            print()
            print(fill("You're standing in front of a street vendor. You can\
 buy food, weapons, and accessories from him. To your east is E 8th St.", 100))
            value = UserInput(street_vendor)
            direction = value.user_input()
            if direction == "east":
                return "street1"
            
        if not self.fresh_arrival:
            print(fill("You're standing in front of a street vendor. You can\
 buy food, weapons, and accessories from him. To your east is E 8th St.", 100))
            value = UserInput(street_vendor)
            direction = value.user_input()
            if direction == "east":
                return "street1"
                
                
    def buy(self, item):
        print("{} added to inventory.".format(item.name.capitalize()))
        player.inventory.append(item)
        vendor = real_item["vendor"]
        vendor.inventory.remove(item.name)
        player.money -= item.value
        
    def sell(self, item):
        print("{} sold back at half price.".format(item.name.capitalize()))
        player.money += (item.value / 2)



class Alleyway(Scene):

    room_objects = []
    room_items = ["dumpster", "blanket", "pillow", "cardboard box", "piss puddle",
    "piss", "puddle", "suitcase", "newspaper", "apple", "gum", "shank"]
    room_characters = []
    room_enemies = ["hobo"]

    def __init__(self):
        self.name = "alleyway"
        self.fresh_arrival = True
        self.north = False
        self.east = False
        self.south = True
        self.west = False
        self.enemy = Hobo()

    def enter(self):
        if self.fresh_arrival:
            self.fresh_arrival = False
            print(fill("You move north. It reeks of urine and body odor here.\
 You plug your nose, looking for the source of the stench. You don't have to look far - this\
 alley seems to have a permament occupant.", 100))
            print()
            print(fill("You are in the alleyway. There is a dumpster to your right. Behind it sits a hobo,\
 asleep in his cardboard box with his ratty blanket and stained pillow. He appears to be using a yellow\
 newspaper to cover his face. You can see the tip of a shank poking out from underneath him.", 100))
            print()
            print(fill("In the cardboard box, behind the hobo, you can see a locked suitcase. Looks\
 like you'll have to go through him to get it.", 100))
            value = UserInput(alleyway)
            direction = value.user_input()
            if direction == "east":
                #I need some requirements here
                return "restaurant"
            if direction == "south":
                return "street1"
            
        if not self.fresh_arrival:
            if self.room_enemies:
                print(fill("The alleyway smells as bad as ever. There's a dumpster to your right. Behind it sits\
 a hobo, asleep in his cardboard box with his ratty blanket and stained pillow. He appears to be using a yellow\
 newspaper to cover his face. You can see the tip of a shank poking out from underneath him.", 100))
                print()
                print(fill("In the cardboard box, behind the hobo, you can see a locked suitcase. Looks\
 like you'll have to go through him to get it.", 100))
            else:
                print(fill("The cardboard box behind the dumpster is now vacant. In it lies a pillow,\
 a blanket, and a yellowed newspaper.", 100))
                if "suitcase" in self.room_items:
                    print()
                    print(fill("Great job getting the hobo out of the way. The locked suitcase is lying\
 on its side, ripe for the taking.", 100))
                else:
                    print()
                    print("An opened suitcase is sitting atop the cardboard box.")
            value = UserInput(alleyway)
            direction = value.user_input()
            if direction == "east":
                #I need some requirements here
                return "restaurant"
            if direction == "south":
                return "street1"
 
 
        
    def fight(self, player, weapon):
        print("You decide to instigate the hobo, poking him with your {}.".format(weapon.name))
        print("He rises up, shank in hand, ready to rumble.")
        sleep(0.5)
        print()
        while True:
            if self.enemy.hp > 0:
                print("Do you attack or flee?")
                print()
                words = input("> ").lower()
                if words == "flee":
                    map_ = Map_("alleyway")
                    game = Engine(map_)
                    game.play()
                if words == "attack":
                    phrases = {1:"You wave your {} around, trying to appear frightening. The hobo laughs at you\
 and draws closer. You strike out with minor hesitation.".format(weapon.name),
                    2:"You tentatively reach out with your {}, tapping the hobo's shank. He withdraws and you\
 take advantage of the moment, rushing forward to attack.".format(weapon.name),
                    3:"Instead of fighting, the two of you have a pleasant discussion and agree to meet up for\
 tea tomorrow.\nJust kidding. You ruthlessly attack him with your {}, showing no mercy.".format(weapon.name),
                    4:"A thought runs through the back of your head that fighting may not be the best option here.\
 Too bad it doesn't compare to your bloodlust. You strike out at the hobo with your {}.".format(weapon.name)}
                    phrase = randint(1,4)
                    print(fill(phrases[phrase], 100))
                    sleep(3)
                    print()
                    miss = randint(1,4)
                    if miss == 1:
                        print("Too bad, you miss!")
                    else:
                        print("You got him!")
                        self.enemy.hp -= weapon.damage
                        print("Hobo's HP: {}".format(max(self.enemy.hp, 0)))
                    if self.enemy.hp > 0:
                        sleep(0.5)
                        print()
                        print("The hobo takes a swing at you.")
                        sleep(0.5)
                        print()
                        hobomiss = randint(1,5)
                        if hobomiss == 1:
                            print("He missed!")
                            sleep(0.5)
                            print()
                        else:
                            print("Ouch, he got you!")
                            player.hp -= self.enemy.damage
                            print("Your HP: {}".format(max(player.hp, 0)))
                            sleep(0.5)
                            if player.hp <= 0:
                                print()
                                print("Oh no, that was the last straw! You resign yourself\
 to your fate of a gruesome stabbing at the hands of a hobo. Isn't that how you always wanted\
 to go out? Sorry, game over.")
                                exit()
                            else:
                                print()
                else:
                    print("No idea what you mean. Attack the man or flee.")
            else:
                sleep(1)
                print()
                print(fill("You defeat the hobo! He runs off in the opposite direction, limping and grabbing his side.\
 As he runs, he steps out of his nasty shoes. He also drops his shank, opting to leave it behind. How lucky for you!\
 You pick up the spoils of your victory.", 100))
                sleep(0.5)
                print()
                print("Dirty shoes added to inventory.")
                print("Shank added to inventory.")
                sleep(6)
                print()
                shoes = DirtyShoes()
                shank = Shank()
                player.inventory.append(shoes)
                player.inventory.append(shank)
                self.room_items.remove("shank")
                self.room_enemies.remove("hobo")
                map_ = Map_("alleyway")
                game = Engine(map_)
                game.play()

    def unlock(self):
        if "suitcase" in self.room_items:
            print("Looks like it's a combination lock.")
            print("Take a guess with the format: x, x, x")
            print()
            while True:
                attempt = input("> ")
                if attempt in lock:
                    print("You find: ${:.2f} and piece of paper that says 'Beware\
 the manhole.' Odd.".format(randint(10, 15)))
                    print()
                    self.room_items.remove("suitcase")
                    map_ = Map_("alleyway")
                    game = Engine(map_)
                    game.play()
                else:
                    print("No luck! The combination must be here somewhere...")
                    print()
                    map_ = Map_("alleyway")
                    game = Engine(map_)
                    game.play()
        else:
            print("You already unlocked the suitcase!")
			                

class Manhole(Scene):

    room_objects = []
    room_items = []
    room_characters = []
    room_enemies = []

    def __init__(self):
        self.name = "manhole"
        self.fresh_arrival = True
        self.north = True
        self.east = False
        self.south = False
        self.west = False
        self.requirement = "lighter"

    def enter(self):
        if self.fresh_arrival:
            self.fresh_arrival = False
            print(fill("You arrive at the manhole cover, a gargantuan slab of\
 metal that offers access to the filthy sewers of downtown Manhattan. You\
 really shouldn't be able to lift it, but we're throwing all continuity out of\
 the window.", 100))
            print()
            found = False
            for item in player.inventory:
                if item.name == self.requirement:
                    found = True
                    print("You can see down here!")
            if not found:
                print(fill("You can't see anything down here; it's pitch black. Looks\
 like you'll have to find something to provide a little light. The only way to go is\
 back toward E 8th St.",100))
            value = UserInput(manhole)
            direction = value.user_input()
            if direction == "north":
                return "street2"
            
        if not self.fresh_arrival:
            found = False
            for item in player.inventory:
                if item.name == self.requirement:
                    found = True
                    print("You can see down here!")
            if not found:
                print(fill("You can't see anything down here; it's pitch black. Looks\
 like you'll have to find something to provide a little light. The only way to go is\
 back toward E 8th St.",100))
            value = UserInput(manhole)
            direction = value.user_input()
            if direction == "north":
                return "street2"


class Bar(Scene):

    room_objects = ["jukebox"]
    room_items = ["long island", "limoncello", "mint julep",
    "cigar", "lottery ticket", "cell phone", "leather wallet", "broken bottle"]
    room_characters = ["guy", "girl", "old man", "man", "bartender", "pool shark",
    "pool", "shark"]
    room_enemies = ["drunk"] 

    def __init__(self):
        self.name = "bar"
        self.fresh_arrival = True
        self.north = False
        self.east = False
        self.south = False
        self.west = True
        self.bought = 0
        self.enemy = Drunk()

    def enter(self):
        if self.fresh_arrival:
            self.fresh_arrival = False
            print(fill("You enter the country bar, a place that promises to be a rootin'-tootin'\
 good time. Several drunks are cheering and singing to the jukebox. You are acutely aware of\
 how sober you are.", 100))
            print()
            print(fill("You stand at the door to The Tipsy Cow. The bartender is tending behind the bar\
 (imagine that). A quiet man is sitting at the end of the bar. He's staring at a girl and her friends across\
 the room. Next to him is an old man in a wheelchair, singing army cadences. In the corner, at the pool table,\
 is a pool shark that wants to play. Stumbling around in front of you is a frat boy drunk that needs to get\
 knocked out. To your west is back toward E 8th St.", 100))
            value = UserInput(bar)
            direction = value.user_input()
            if direction == "west":
                return "street2"
            
        if not self.fresh_arrival:
            if self.room_enemies:
                print(fill("You stand at the door to The Tipsy Cow. The bartender is tending behind the bar\
 (imagine that). A quiet man is sitting at the end of the bar. He's staring at a girl and her friends across\
 the room. Next to him is an old man in a wheelchair, singing army cadences. In the corner, at the pool table,\
 is a pool shark that wants to play. Stumbling around in front of you is a frat boy drunk that needs to get\
 knocked out. To your west is back toward E 8th St.", 100))
                value = UserInput(bar)
                direction = value.user_input()
                if direction == "west":
                    return "street2"
            else:
                print(fill("You stand at the door to The Tipsy Cow. The bartender is tending behind the bar\
 (imagine that). A quiet man is sitting at the end of the bar. He's staring at a girl and her friends across\
 the room. Next to him is an old man in a wheelchair, singing army cadences. In the corner, at the pool table,\
 is a pool shark that wants to play. To your west is back toward E 8th St.", 100))
                value = UserInput(bar)
                direction = value.user_input()
                if direction == "west":
                    return "street2"
        
    def fight(self, player, weapon):
        print(fill("You figure it's high time to start an uproar in this joint. You yell at the drunk\
 and brandish your {} so he knows it's time for a fight.".format(weapon.name), 100))
        print(fill("He approaches you, broken bottle in hand, roaring some slurred battle cries."))
        sleep(0.5)
        print()
        while True:
            if self.enemy.hp > 0:
                print("Do you attack or flee?")
                print()
                words = input("> ").lower()
                if words == "flee":
                    map_ = Map_("bar")
                    game = Engine(map_)
                    game.play()
                if words == "attack":
                    phrases = {1:"Phrase 1 w/ {}".format(weapon.name),
                    2:"Phrase 2 w/ {}".format(weapon.name),
                    3:"Phrase 3 w/ {}".format(weapon.name),
                    4:"Phrase 4 w/ {}".format(weapon.name)}
                    phrase = randint(1,4)
                    print(fill(phrases[phrase]))
                    sleep(0.5)
                    print()
                    miss = randint(1,4)
                    if miss == 1:
                        print("Too bad, you miss!")
                    else:
                        print("You got him!")
                        self.enemy.hp -= weapon.damage
                        print("Drunk's's HP: {}".format(max(self.enemy.hp, 0)))
                    if self.enemy.hp > 0:
                        sleep(0.5)
                        print()
                        print("The drunk takes a swing at you.")
                        sleep(0.5)
                        print()
                        drunkmiss = randint(1,5)
                        if drunkmiss == 1:
                            print("He missed!")
                            sleep(0.5)
                            print()
                        else:
                            print("Ouch, he got you!")
                            player.hp -= self.enemy.damage
                            print("Your HP: {}".format(max(player.hp, 0)))
                            sleep(0.5)
                            if player.hp <= 0:
                                print()
                                print("Oh no, that was the last straw! You resign yourself\
 to your fate of an embarrassing death at the hands of a stupid drunk. Isn't that how you always wanted\
 to go out? Sorry, game over.")
                                exit()
                            else:
                                print()
                else:
                    print("No idea what you mean. Attack the man or flee.")
            else:
                sleep(1)
                print()
                print(fill("You emerge victorious! The drunk lies out cold on the floor in a puddle of\
 his own vomit. You're normally not a thief, but this guy really pissed you off. Ransacking his pockets, you\
 find a leather wallet and a cell phone. You take his weapon too, for good measure.", 100))
                sleep(0.5)
                print()
                print("Leather wallet added to inventory.")
                print("Cell phone added to inventory.")
                print("Broken bottle added to inventory.")
                print()
                player.inventory.append(LeatherWallet())
                player.inventory.append(CellPhone())
                player.inventory.append(BrokenBottle())
                self.room_enemies.remove("drunk")
                map_ = Map_("bar")
                game = Engine(map_)
                game.play()

    def buy(self, item):
        if self.bought < 6:
            print("{} added to inventory.".format(item.name.capitalize()))
            player.inventory.append(item)
            vendor = real_item["vendor"]
            player.money -= item.value
            self.bought += 1
        else:
            print(fill("Uh-oh, the bartender cut you off! You're out of luck if\
 you drank all your drinks. Otherwise try to sell some back so she knows\
 you're not a lush.",100))

    def sell(self, item):
        print("{} sold back at half price.".format(item.name.capitalize()))
        player.money += (item.value / 2)
        self.bought -= 1
            

class ClothesStore(Scene):

    room_objects = []
    room_items = ["scarf", "plain tee", "graphic tee",
    "jeans", "slacks", "fancy shoes"]
    room_characters = ["cashier"]
    room_enemies = []

    def __init__(self):
        self.name = "clothes_store"
        self.fresh_arrival = True
        self.north = False
        self.east = True
        self.south = False
        self.west = True

    def enter(self):
        if self.fresh_arrival:
            self.fresh_arrival = False
            print(fill("You're standing in an outlet store. There are racks on\
 racks on racks of clothes. Maybe you could buy some from the cashier.", 100))
            print()
            print(fill("You're standing in an outlet store. It looks like the type\
 of place that requires a dress code, it makes you feel less classy. To your\
 east is the store's break room. To your west is 45th St.", 100))
            value = UserInput(clothes_store)
            direction = value.user_input()
            if direction == "west":
                return "street3"
            if direction == "east":
                return "break_room"
            
        if not self.fresh_arrival:
            print(fill("You're standing in an outlet store. It looks like the type\
 of place that requires a dress code, it makes you feel less classy. To your\
 east is the store's break room. To your west is 45th St.", 100))
            value = UserInput(clothes_store)
            direction = value.user_input()
            if direction == "west":
                return "street3"
            if direction == "east":
                return "break_room"

    def buy(self, item):
        print("{} added to inventory.".format(item.name.capitalize()))
        player.inventory.append(item)
        cashier = real_item["cashier"]
        cashier.inventory.remove(item.name)
        player.money -= item.value
        
    def sell(self, item):
        print("{} sold back at half price.".format(item.name.capitalize()))
        player.money += (item.value / 2)
        cashier = real_item["cashier"]
        cashier.inventory.append(item.name)

class BreakRoom(Scene):

    room_objects = ["chairs", "clock", "calendar"]
    room_items = ["purse", "used napkin", "napkin", "tampon", "lipstick", "lighter"]
    room_characters = []
    room_enemies = []

    def __init__(self):
        self.name = "break_room"
        self.fresh_arrival = True
        self.north = False
        self.east = False
        self.south = False
        self.west = True
        self.have = "purse"

    def enter(self):
        if self.fresh_arrival:
            self.fresh_arrival = False
            print(fill("You enter the break room. It's dreary in here. You wonder\
 how the employees are able to tolerate it.", 100))
            print()
            print(fill("You see some chairs around a table with a purse sitting atop it.\
 There is a clock and a calendar on the wall. Not much else. To your west is back to the\
 clothes store.", 100))
            value = UserInput(break_room)
            direction = value.user_input()
            if direction == "west":
                return "clothes_store"
            
        if not self.fresh_arrival:
            found = False
            for item in player.inventory:
                if item.name == self.have:
                    found = True
                    print(fill("You see some chairs gathered around an empty table. There is a clock\
 and a calendar on the wall. Not much else. To your west is back to the clothes store.",100))
            if not found:
                print(fill("You see some chairs around a table with a purse sitting atop it.\
     There is a clock and a calendar on the wall. Not much else. To your west is back to the\
     clothes store.",100))
            value = UserInput(break_room)
            direction = value.user_input()
            if direction == "west":
                return "clothes_store"
                

class Restaurant(Scene):

    room_objects = ["waterfall"]
    room_items = ["piano", "bruschetta", "crostini", "insalata caprese",
    "pin"]
    room_characters = ["fancy woman", "chef"]
    room_enemies = []

    def __init__(self):
        self.name = "restaurant"
        self.fresh_arrival = True
        self.north = False
        self.east = True
        self.south = False
        self.west = False

    def enter(self):
        if self.fresh_arrival:
            if player.classy >= 20:
                self.fresh_arrival = False
                print(fill("A fancy schmancy restaurant, Eau de la Cul. You're rusty\
 on your French, but the name doesn't sound pleasant.", 100))
                print()
                print(fill("You are standing in a fancy restaurant. On the far side\
 you can see a waterfall and a grand piano. Lovely. There's a fancy woman at the table\
 nearest you who must think you're her server. She's calling you over. If you'd like,\
 you can buy a delicacy from the chef.",100))
            else:
                self.fresh_arrival = False
                print(fill("Uh-oh. It looks like you're not fancy enough to get in here.\
 The maitre d' kicks you out. Try again when you're a little classier.",100))
                print()
                map_ = Map_("street3")
                game = Engine(map_)
                game.play()
            value = UserInput(restaurant)
            direction = value.user_input()
            if direction == "east":
                return "street3"
            
        if not self.fresh_arrival:
            if player.classy >= 20:
                print(fill("You are standing in a fancy restaurant. On the far side\
 you can see a waterfall and a grand piano. Lovely. There's a fancy woman at the table\
 nearest you who must think you're her server. She's calling you over. If you'd like,\
 you can buy a delicacy from the chef.", 100))
            else:
                print(fill("Uh-oh. It looks like you're not fancy enough to get in here.\
 The maitre d' kicks you out. Try again when you're a little classier.",100))
                print()
                map_ = Map_("street3")
                game = Engine(map_)
                game.play()
            value = UserInput(restaurant)
            direction = value.user_input()
            if direction == "east":
                return "street3"

    def buy(self, item):
        print("{} added to inventory.".format(item.name.capitalize()))
        player.inventory.append(item)
        player.money -= item.value
        
    def sell(self, item):
        print("Sorry, this place doesn't buy back food.")

class BoxingArena(Scene):

    room_objects = ["punching bag"]
    room_items = ["boxing gloves"]
    room_characters = ["fighter"]
    room_enemies = ["boxer"]

    def __init__(self):
        self.name = "boxing_arena"
        self.fresh_arrival = True
        self.north = False
        self.east = False
        self.south = True
        self.west = False
        self.enemy = Boxer()

    def enter(self):
        if self.fresh_arrival:
            self.fresh_arrival = False
            print(fill("An intimidating boxing arena. Something nice and\
 descriptive will go here.", 100))
            print()
            print(fill("There's a fighter and a boxer here. You can fight\
 the boxer and win some money. South: 45th St.", 100))
            value = UserInput(boxing_arena)
            direction = value.user_input()
            if direction == "south":
                return "street3"
            
        if not self.fresh_arrival:
            print(fill("There's a fighter and a boxer here. You can fight\
 the boxer and win some money. South: 45th St.", 100))
            value = UserInput(boxing_arena)
            direction = value.user_input()
            if direction == "south":
                return "street3"
        
    def fight(self, player, weapon):
        print("It's time to rumble. You enter the ring and approach the boxer.")
        print("He looks intimidating. Just try picturing him in his underwear.")
        sleep(0.5)
        print()
        while True:
            if self.enemy.hp > 0:
                print("Do you attack or flee?")
                print()
                words = input("> ").lower()
                if words == "flee":
                    map_ = Map_("boxing_arena")
                    game = Engine(map_)
                    game.play()
                if words == "attack":
                    phrases = {1:"Phrase 1 w/ {}.".format(weapon.name),
                    2:"Phrase 2 w/ {}.".format(weapon.name),
                    3:"Phrase 3 w/ {}".format(weapon.name),
                    4:"Phrase 4 w/ {}.".format(weapon.name)}
                    phrase = randint(1,4)
                    print(fill(phrases[phrase]))
                    sleep(0.5)
                    print()
                    miss = randint(1,4)
                    if miss == 1:
                        print("Too bad, you miss!")
                    else:
                        print("You got him!")
                        self.enemy.hp -= weapon.damage
                        print("Boxer's HP: {}".format(max(self.enemy.hp, 0)))
                    if self.enemy.hp > 0:
                        sleep(0.5)
                        print()
                        print("The boxer takes a swing at you.")
                        sleep(0.5)
                        print()
                        boxermiss = randint(1,5)
                        if boxermiss == 1:
                            print("He missed!")
                            sleep(0.5)
                            print()
                        else:
                            print("Ouch, he got you!")
                            player.hp -= self.enemy.damage
                            print("Your HP: {}".format(max(player.hp, 0)))
                            sleep(0.5)
                            if player.hp <= 0:
                                print()
                                print("Oh no, that was the last straw! You resign yourself\
 to your fate of blunt force trauma to the skull. Isn't that how you always wanted\
 to go out? Sorry, game over.")
                                exit()
                            else:
                                print()
                else:
                    print("No idea what you mean. Attack the man or flee.")
            else:
                sleep(1)
                print()
                print(fill("You defeat the boxer! Though he has a black eye, he gives you your\
 money fair and square. A fine day's work.", 100))
                sleep(0.5)
                print()
                print("+${:.2f} added to inventory.".format(self.enemy.money))
                print()
                player.money += self.enemy.money
                self.enemy.hp = randint(30, 40)
                map_ = Map_("boxing_arena")
                game = Engine(map_)
                game.play()

scenes = {"box_office":BoxOffice(),
              "street1":Street1(),
              "street2":Street2(),
              "street3":Street3(),
              "street_vendor":StreetVendor(),
              "alleyway":Alleyway(),
              "manhole":Manhole(),
              "bar":Bar(),
              "clothes_store":ClothesStore(),
              "break_room":BreakRoom(),
              "restaurant":Restaurant(),
              "boxing_arena":BoxingArena()}

class Map_():
    
    scenes = {"box_office":BoxOffice(),
              "street1":Street1(),
              "street2":Street2(),
              "street3":Street3(),
              "street_vendor":StreetVendor(),
              "alleyway":Alleyway(),
              "manhole":Manhole(),
              "bar":Bar(),
              "clothes_store":ClothesStore(),
              "break_room":BreakRoom(),
              "restaurant":Restaurant(),
              "boxing_arena":BoxingArena()}

    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        room = Map_.scenes.get(scene_name)
        return room

    def opening_scene(self):
        return self.next_scene(self.start_scene)




#                    -----======(   GAME   )======-----


box_office = BoxOffice()
street1 = Street1()
street2 = Street2()
street3 = Street3()
street_vendor = StreetVendor()
alleyway = Alleyway()
manhole = Manhole()
bar = Bar()
clothes_store = ClothesStore()
break_room = BreakRoom()
restaurant = Restaurant()
boxing_arena = BoxingArena()
player = Player()

class UserInput():
    def __init__(self, scene):
        self.scene = scene

    def user_input(self):
        while True:
            print()
            user_input = input("> ").lower()
            """
            
            sleep(0.5)
            
            """
            words = user_input.split(" ")
            wordlist = list(words)
            verb = wordlist[0]

			#Handling nouns

            if len(wordlist) == 2:
            	noun = wordlist[1]
            	if noun not in items:
            		print("For some reason '{}' doesn't resonate with me.".format(noun))
            		continue
            if len(wordlist) == 3:
                if wordlist[1] in prepositions:
                    noun = wordlist[2]
                else:
                    noun = wordlist[1] + " " + wordlist[2]
                if noun not in items:
                    print("For some reason '{}' doesn't resonate with me.".format(noun))
                    continue
            if len(wordlist) > 3:
                print("I'm kind of stupid, please keep input to 3 words or less.")
                continue
            
            
            #The basic verbs I don't need real nouns for


            if verb == "quit":
            	print("Thanks for playing!")
            	exit(1)


            elif verb == "help":
                print("inv, status,")
                print("look, take, go,")
                print("eat, drink, wear,")
                print("buy, buy from, sell,")
                print("talk, fight,")
                print("quit")
                print()
                print("'look' will be your best friend in this game")
                print("'look (item)' for info and specialized commands")
                continue


            elif verb == "status":
            	print("HP: {}".format(player.hp))
            	print("Class: {}".format(player.classy))
            	continue


            elif verb == "go":
                if len(wordlist) > 1:
                    if noun == "north":
                        if self.scene.north:
                            return "north"
                        else:
                            print("You head north.")
                            print("*THUNK*")
                            print("Whoops, can't go that way.")
                    elif noun == "south":
                        if self.scene.south:
                            return "south"
                        else:
                            print("You head south.")
                            print("*THUNK*")
                            print("Whoops, can't go that way.")
                    elif noun == "east":
                        if self.scene.east:
                            return "east"
                        else:
                            print("You head east.")
                            print("*THUNK*")
                            print("Whoops, can't go that way.")
                    elif noun == "west":
                        if self.scene.west:
                            return "west"
                        else:
                            print("You head west.")
                            print("*THUNK*")
                            print("Whoops, can't go that way.")
                    else:
                        print("In my humble opinion that makes no sense.")
                else:
                    print("Go where?")


            elif verb == "inv":
            	player.print_inventory()

 
            # More verbs to define           


            elif verb == "look":
                if len(wordlist) > 1:
                    if noun == "clothes":
                        if self.scene.name == "clothes_store":
                            Cashier().buy()
                        else:
                            print("There are no 'clothes' here.")
                            
                            #I'm too lazy to create a separate clothes
                            #class and implement a look method, so this works.
                            
                    found = False
                    for item in player.inventory:
                        if item.name == noun:
                            found = True
                            noun = real_item[noun]
                            noun.look()
                    if noun in self.scene.room_items or noun in self.scene.room_characters\
                    or noun in self.scene.room_enemies:
                        found = True
                        noun = real_item[noun]
                        noun.look()
                    elif noun in self.scene.room_objects:
                        found = True
                        print(items[noun])
                    else:
                        if not found:
                        	print("I don't see '{}' here.".format(noun))
                        else:
                            pass
                else:
                    print(self.scene.look())


            elif verb == "take":
                if len(wordlist) > 1:
                    found = False
                    for item in player.inventory:
                        if item.name == noun:
                            found = True
                            print("You already have '{}'.".format(noun))
                        elif item.name == "purse":
                            purse = real_item["purse"]
                            if noun in purse.inventory:
                                found = True
                                noun = real_item[noun]
                                purse.inventory.remove(noun.name)
                                noun.take(self.scene)
                    if noun in self.scene.room_items:
                        found = True
                        noun = real_item[noun]
                        noun.take(self.scene)
                    elif (noun in self.scene.room_characters or
                    noun in self.scene.room_enemies):
                        found = True
                        print("You can't take '{}'.".format(noun))
                    else:
                        if not found:
                            
                            #Pretty sure I don't need both of those conditions but I'm
                            #scared of what might happen if I remove them.
                            #This take function was carefully crafted.
                            #So, "else: if not found" it is!
                            
                            print("I don't see '{}' here.".format(noun))
                else:
                    print("Take what?")


            elif verb == "drink":
                if len(wordlist) > 1:
                    if "piss puddle" in self.scene.room_items:
                        noun = real_item[noun]
                        noun.drink()
                        
                        #Just waiting for somebody to do this and tell me about it *evil grin*
                        #It's only in its own branch up there because it's the only thing that
                        #can be drunk (drank?) straight from the environment.
                        
                    else:
                        found = False
                        for item in player.inventory:
                            if item.name == noun:
                                found = True
                                if isinstance(item, Consumable) or isinstance(item, CashConsumable):
                                    noun = real_item[noun]
                                    if noun.verb == verb:
                                        noun.drink()
                                        player.inventory.remove(item)
                                    else:
                                        print("You can't drink '{}'.".format(noun))
                                if noun == "limoncello" or noun == "mint julep" or noun == "long island":
                                    noun = real_item[noun]
                                    noun.drink()
                                    player.inventory.remove(item)
                                    if player.drank == 6:
						
                                        #replit.clear()
                                        #A cool little thing on repl.it where it clears the screen
					
					print(fill("You down your sixth drink. Everything you've done\
 up to this point becomes hazy. Maybe you should reconsider some life choices.",100))
                                else:
                                    print("You can't drink '{}'.".format(noun))
                        if not found:
                            print("You don't have '{}'.".format(noun))
                else:
                    print("Drink what?")

	            
            elif verb == "eat":
            	if len(wordlist) > 1:
            		found = False
            		for item in player.inventory:
            			if item.name == noun:
            				found = True
            				if isinstance(item, Consumable) or isinstance(item, CashConsumable):
            					noun = real_item[noun]
            					if noun.verb == verb:
            						noun.eat()
            						player.inventory.remove(item)
            					else:
            						print("You can't eat '{}'.".format(noun))
            				else:
            					print("You can't eat '{}'.".format(noun))
            		if not found:
            			print("You don't have '{}'.".format(noun))
            	else:
	            	print("Eat what?")

	            
            elif verb == "wear":
            	if len(wordlist) > 1:
            		found = False
            		for item in player.inventory:
            			if item.name == noun:
            				found = True
            				if isinstance(item, Classy) or isinstance(item, CashClassy):
            					noun = real_item[noun]
            					if noun.verb == verb:
            						noun.wear()
            						player.inventory.remove(item)
            					else:
            						print("I don't think 'wear' is the right word for that.")
            				else:
            					print("C'mon, you can't wear '{}'.".format(noun))
            		if not found:
            			print("You don't have '{}'.".format(noun))
            	else:
	            	print("Wear what?")

	            
            elif verb == "fight":
                if self.scene.room_enemies:
                    if len(wordlist) > 1:
                        if noun in self.scene.room_enemies:
                            if self.scene.enemy.hp > 0:
                                print("Which weapon do you choose?")
                                print()
                                for item in player.inventory:
                                    if (isinstance(item, Weapons) or
                                    isinstance(item, CashWeapons)):
                                        print("* {}".format(item))
                                while True:
                                    print()
                                    ui = input("> ").lower()
                                    found = False
                                    for item in player.inventory:
                                        if item.name in ui:
                                            found = True
                                            if isinstance(item, Weapons):
                                                weapon = item
                                                if weapon.name == "fists":
                                                    print("This might be easier with a real weapon...")
                                                    sleep(0.5)
                                                    print()
                                                self.scene.fight(player, weapon)
                                        else:
                                            found = False
                                    if not found:
                                        print("C'mon, you can't fight with '{}'.".format(noun))
                            else:
                                print("You already defeated the {}.".format(self.scene.enemy.name))
                        else:
                            print("Why would you fight '{}' when the {} is right there?".format(noun, self.scene.enemy.name))
                    else:
                        print("Fight who?")
                else:
                    print("There isn't anyone to fight here.")


            elif verb == "unlock":
                if len(wordlist) > 1:
                    if "suitcase" in self.scene.room_items:
                        if self.scene.enemy.hp > 0:
                            print(fill("You try reaching over the hobo for the suitcase. He grumbles\
 angrily and you snatch your hand back. Looks like you gotta get him out of the way first.", 100))
                        else:
                            self.scene.unlock()
                    else:
                        print("I don't see anything to unlock.")
                else:
                    print("Unlock what?")


            elif verb == "scratch":
                if len(wordlist) > 1:
                    found = False
                    for item in player.inventory:
                        if item.name == noun:
                            if item.name == "lottery ticket":
                                found = True
                                noun = real_item[noun]
                                player.inventory.remove(item)
                                noun.scratch(self.scene.name)
                            else:
                                found = True
                                print("You can't scratch '{}', as much as you'd like to.".format(noun))
                    if not found:
                        print(fill("You don't have '{}', so you start scratching yourself.\
 Then you remember you're in public.".format(noun), 100))
                else:
                    print("Scratch what?")


            elif verb == "talk":
                if len(wordlist) > 1:
                    if noun in self.scene.room_characters:
                        noun = real_item[noun]
                        if isinstance(noun, Npc):
                            noun.talk()
                    elif (noun in self.scene.room_objects or
                    noun in self.scene.room_items or
                    noun in self.scene.room_enemies):
                        print(fill("'{}' either can't or doesn't want to talk to you.".format(noun.capitalize()),100))
                    else:
                        print(fill("I don't see '{}' here.".format(noun), 100))
                else:
                    print(fill("You start talking to yourself. Some people look\
 at you strangely. Maybe you should find someone to talk to...", 100))
 
 
            elif verb == "buy":
                if len(wordlist) > 1:
                    if noun == "ticket":
                        if self.scene.name == "box_office":
                            Attendant().buy()
                        else:
                            print("Go to the box office to buy a ticket.")
                    if noun == "clothes":
                        if self.scene.name == "clothes_store":
                            Cashier().buy()
                        else:
                            print("There are no 'clothes' here.")
                            
                            #I'm too lazy to make a separate clothes class and
                            #implement a buy method, so this works.
                            
                    elif wordlist[1] == "from":
                        if noun in self.scene.room_characters:
                            noun = real_item[noun]
                            noun.buy()
                        else:
                            print("You can't buy from '{}'.".format(noun))
                    elif noun in self.scene.room_items:
                        noun = real_item[noun]
                        if (isinstance(noun, CashConsumable) or
                        isinstance(noun, CashClassy) or
                        isinstance(noun, CashWeapons)):
                            if noun.value < player.money:
                                self.scene.buy(noun)
                            else:
                                print("Sorry, that's a bit too expensive for your tastes.")
                        else:
                            print("You can't buy '{}'.".format(noun.name))
                    else:
                        print("You can't buy '{}' here.".format(noun))
                else:
                    print("Buy from who? Buy what? Who are you? Where am I?")


            elif verb == "sell":
                if len(wordlist) > 1:
                    if wordlist[1] == "to":
                        if noun in self.scene.room_characters:
                            noun = real_item[noun]
                            noun.sell()
                        else:
                            print("You can't sell to '{}'.".format(noun))
                    elif noun in self.scene.room_items:
                        found = False
                        for item in player.inventory:
                            if item.name == noun:
                                found = True
                                if (isinstance(item, CashConsumable) or
                                isinstance(item, CashClassy) or
                                isinstance(item, CashWeapons)):
                                    self.scene.sell(item)
                                else:
                                    print("You can't sell '{}'.".format(noun))
                        if not found:
                            print("You don't have '{}'.".format(noun))
                    else:
                        print("You can't sell '{}' here.".format(noun))
                else:
                    print("Huh? Eh? Sell what? Or to whom?")


            elif verb == "smoke":
                if len(wordlist) > 1:
                    if (noun == "cigar" or
                    noun == "glass pipe" or
                    noun == "pipe"):
                        found = False
                        for item in player.inventory:
                            if item.name == noun:
                                found = True
                                noun = real_item[noun]
                                noun.smoke()
                        if not found:
                            print("You don't have '{}'.".format(noun))
                    else:
                        print("You can't smoke '{}'.".format(noun))
                else:
                    print(fill("You try smoking the air but, for some reason, it just\
 doesn't pan out.",100))
 
 
            elif verb == "play":
                if len(wordlist) > 1:
                    found = False
                    if noun in self.scene.room_objects:
                        if (noun == "jukebox" or
                        noun == "piano"):
                            found = True
                            noun = real_item[noun]
                            noun.play()
                        else:
                            print("Sorry, you can't play '{}'.".format(noun))
                    elif (noun == "pool shark" or
                    noun == "pool" or noun == "shark" or noun == "game"):
                        if "pool shark" in self.scene.room_characters:
                            found = True
                            noun = real_item[noun]
                            noun.play()
                        else:
                            found = True
                            print("There's no '{}' here.".format(noun))
                    elif (noun in self.scene.room_items or
                    noun in self.scene.room_characters or
                    noun in self.scene.room_enemies):
                        found = True
                        print("C'mon, you can't play '{}'.".format(noun))
                    for item in player.inventory:
                        if item.name == noun:
                            found = True
                            print("You can't play '{}'.".format(noun))
                    if not found:
                        print("I don't see '{}' in this room.".format(noun))
                else:
                    print("Play what? You can't just start playing with yourself.")
                    
                    
            



            else:
                print(fill("I'm not sure what you're trying to do. Type 'help' for a list of commands.", 100))
                






map_ = Map_("box_office")
game = Engine(map_)
game.play()
