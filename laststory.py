#!/usr/bin/env python
# Last Story
# Just a thing, where I have stolen some things from Final Fantasy
# mostly around battling and the like. If I can be bothered, I might
# make a small RPG-esque pygame for it

import random


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Below is for printing output for debugging. I might need to         #
# legitimately use the 'print' command at some point, so using a      #
# 'debug' function lets me find and comment out very easily.          #
#                                                                     # 
# It looks pretty ugly when it prints out but it's quicker later on.  #
#                                                                     #
# This is a lesson learnt hard from CLIc                              #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

def debug(*args):
	print args

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

accuracy = 25
evasion = 12
strength = 100
defence = 80
statuses = []

class Combat(object):
	""" Combat requires some shit to be calculated. It needs to:
#	1. Check if the attack hits (accuracy stats vs evasion stats)
#	2. Calculate how much damage the attack does (strength vs defence)
#	3. Check if there are any other things going on (e.g. is the attack
#	effective against the opponent, or does it do anything extra)
#	
#	1 is pretty straightforward. It would be boring to go with a 
#	straightforward if accuracy > evasion so it needs a multiplier.
#	Take the accuracy and multiply it by a random number between 0 and 1
#	and then do the same for the evasion. Whichever is higher is winner.
#	
#	2 should be the same as above but it should not return a simple yes
#	or no like 1 does. It needs to run the outcome through 3 before it
#	returns a value.
#	
#	3 is more difficult as there's a lot to take into consideration. 
#	This can be expanded on at a later point however.
#	"""

	# Obtain a whole number between 1 and 10, divide by 10 to get a
	# decimal between 0 and 1 - set data type as float to get the 
	# decimal point for an always reductie division
	accuracyModifier = float(random.randint(1,10)) /10
	evasionModifier = float(random.randint(1,10)) /10
	
	
	damageModifier = random.randint(1,4)
	defenceModifier = random.randint(1,4)
	
	def __init__(self, accuracy, evasion, strength, defence, statuses):
		self.accuracy = accuracy
		self.evasion = evasion
		self.strength = strength
		self.defence = defence
		self.statuses = statuses

	def attackAttempted(self):
		self.attackConnects()
		
	def attackConnects(self):
		# Modify attack and evasion stats as per top comments
		modifiedAcc = accuracy * self.accuracyModifier
		modifiedEva = evasion * self.evasionModifier
		
		# Check to see if attack hits. If evasion is higher than the
		# accuracy of the attack, it misses, otherwise arguments are
		# passed to the next function to determine how much damage is
		# done
		if modifiedAcc > modifiedEva:
			debug("hit")
			self.damageDone()
		else:
			debug("miss")
			return False
	
	def damageDone(self):
		# I don't know why but the line below doesn't work if arguments
		# aren't called as self - seems silly but it stops working if
		# removed. Maybe look to fix at some point.
		
		# TODO: + 25 below to replaced by something more random
		damageToDo = int(((strength * self.damageModifier) % (defence * self.defenceModifier) + 25))
		debug("made it to this bit at least...", damageToDo)
		
		# damageConfirmed needs value of damage to be further modified
		# or negated. Pass damageToDo directly to damageConfirmed rather
		# than calling function again
		self.damageConfirmed(damageToDo)
		
	def damageConfirmed(self, initialDamage):
		self.initialDamage = initialDamage
		""" Check for status modifications to weapons """
		# List of status modifications passed as argument. If length
		# is 0, no status modifiers
		# NB: statuses list may need to be a dictionary
		if len(self.statuses) == 0:
			debug(initialDamage, "and this little piggy")
			#return initialDamage
		#else:
		#	for each in self.statuses:
				


combatTrial = Combat(accuracy, evasion, strength, defence, statuses)
combatTrial.attackAttempted()
