## Sam's extension file for the Musicians projects, Unit 1, Lesson 3.1.1
## 5.27.17

class Musician(object):
    def __init__(self, sounds):
        self.sounds = sounds

    def solo(self, length):
        for i in range(length):
            print(self.sounds[i % len(self.sounds)], end=" ")
        print()

class Bassist(Musician): 
# The Musician class is the parent of the Bassist class
    def __init__(self):
        # Call the __init__ method of the parent class
        super().__init__(["Twang", "Thrumb", "Bling"])

class Guitarist(Musician):
    def __init__(self):
        # Call the __init__ method of the parent class
        super().__init__(["Boink", "Bow", "Boom"])

    def tune(self):
        print("Be with you in a moment")
        print("Twoning, sproing, splang")

class Drummer(Musician):
	def __init__(self):
		#call the __init__ method of the parent class
		super().__init__(["Thump", "Thump", "Thump", "Thump Thump"])

	def countin(self):
		print("Alright - one, two, three, four!")

	def explode(self):
		print("The Drummer has exploded.")

class Band(object):
	def __init__(self, name):
		self.name = name
		self.members = []

	def hire(self, member):
		# add an item member (who is of class musician) to the band list members
		if member in self.members:
			print("You can't join the band twice!")
		elif type(member) in [Drummer]:
			NoDrummer = True
			for e in self.members:
				if type(e) == Drummer:
					print("Sorry we already have a drummer!")
					NoDrummer = False
				else:
					pass
			if NoDrummer == True:
				self.members.append(member)
				print ("Great, you're in the band!")
			else:
				pass
		else:
			if type(member) in [Drummer, Bassist, Guitarist]:
				self.members.append(member)
				print ("Great, you're in the band!")
			else:
				print ("Sorry, we only hire musicians in this band.")

	def fire(self,member):
		if member in self.members:
			self.members.remove(member)
			print("Hit the road.  You're out!".format(member))
		else:
			print("That Musician is not in the band.")

	def play_hit(self):
		"""First check if drummer to count in, then everyone play a solo"""
		DrummerInBand = False
		print("{} ready to rock!".format(self.name))
		for member in self.members:
			if type(member) == Drummer:
				member.countin()
				DrummerInBand = True
			else:
				pass
		if DrummerInBand == False:
			print("We can't play, we've got no drummer.")
		else:
			for each in self.members:
				each.solo(10)


##here is the test code, apparently it has to go at the end
##Test scenarios as follows:
## DRUMMER: create drummer, count in, play solo (inherit from Musician class), spontaneously combust

## HIRE: hire one of each, hire more than one of each (except Drummer), try to hire the same person again, try to hire someone that doesn't exist
## please note given this is not a user input I didn't create exceptions for a name error here - but how would i do that?
## FIRE: fire every object in the band once, fire them more than once, fire someone not in the band
## PLAY HIT: play with a drummer, play without a drummer

nigel = Guitarist()
steve = Guitarist()
pete = Drummer()
pete.countin()
pete.solo(20)
pete.explode()

rodney = Bassist()

trevor = Drummer()

my_band = Band("Death Furnace")
print(my_band.name)
## How do I create a band with a space in the name?  Like this?
my_band.hire(nigel)
my_band.hire(rodney)
my_band.hire(nigel)
my_band.hire(pete)
my_band.hire(steve)
my_band.hire("trevor")
my_band.hire(trevor)
print(my_band.members)

my_band.play_hit()

my_band.fire(rodney)
my_band.fire("trevor")
my_band.fire(rodney)
my_band.fire(pete)
my_band.fire(nigel)

my_band.play_hit()

my_band.hire(pete)
my_band.fire(trevor)

my_band.play_hit()



