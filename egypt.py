import random
import sys

class Egypt():
	# Lists of possible events to be used in corresponding functions (camel case function with r in front)
	rProtest = ["You are murdered by the police. May your sacrifice help free Egypt!\n",
				"You are arrested and thrown in jail.\n",
				"You make it through a day of protests! Thank you for your support!\n"]
	rSpread = ["Sisi is watching everything. You are arrested and thrown in jail.\n",
			   "Your Facebook friend reports you to the police. You are arrested and thrown in\n"
			   "jail. You can't always trust your Facebook friends.\n",
			   "Your voice is helping bring change! Thank you for your support!\n"]
	rNothing = ["Your neighbour does not like you and so reports you to the police as being a\n"
				"member of the Muslim Brotherhood. You are arrested and thrown in jail.\n",
				"You have done nothing. Your day goes by like normal.\n"]
	rJail = ["You are convicted of terrorism and sentenced to death.\n",
			 "You are convicted of protesting illegally and sentenced to many years in prison.\n",
			 "You are left in jail without a trial.\n"]
	rJailed = ["SISI IS TOPPLED AND THE NEW LEADER FREES YOU AND ALL POLITICAL PRISONERS FROM\n"
			   "PRISON! EGYPT BECOMES A GREAT DEMOCRATIC NATION!\n",
			   "Due to your horrible living conditions and treatment in jail, you die.\n",
			   "You remain in jail for a decade before being released.\n"]
	day = 1

	def __init__(self):
		# Gives context
		print("\n\n"+"="*80)
		print("Welcome to Egypt. Egypt is currently under the oppressive dictatorship of Abdel\n"
			  "Fattah el-Sisi. You must choose your actions carefully. Will you try to survive\n"
			  "as long as possible, or make a difference to this great nation?\n"+"="*80+"\n")
		self.firstChoice()

	def firstChoice(self):
		print("\n"+"_"*80)
		print("You have begun day {} in Egypt.".format(self.day))
		choice = input("Will you [P]rotest, [S]pread the truth, do [N]othing, or [Q]uit? ").lower()
		if choice == "p":
			self.protest()
		elif choice == "s":
			self.spread()
		elif choice == "n":
			self.nothing()
		elif choice == "q":
			print("\nDon't leave! Egypt needs you!\n")
			self.message()
			sys.exit()
		else:
			self.firstChoice()

	def protest(self):
		print(" ")
		num = random.randint(0,9)
		if num == 0 or num == 1:
			print(self.rProtest[0])
			self.message()
			sys.exit()
		elif num == 2 or num == 3 or num == 4:
			print(self.rProtest[1])
			self.jail()
		elif num > 4:
			print(self.rProtest[2])
			self.day+=1
			self.firstChoice()

	def spread(self):
		print(" ")
		num = random.randint(0,9)
		if num == 0 or num == 1:
			print(self.rSpread[0])
			self.jail()
		elif num == 2 or num == 3:
			print(self.rSpread[1])
			self.jail()
		elif num > 3:
			print(self.rSpread[2])
			self.day+=1
			self.firstChoice()

	def nothing(self):
		print(" ")
		num = random.randint(0,9)
		if num == 0:
			print(self.rNothing[0])
			self.jail()
		elif num > 0:
			print(self.rNothing[1])
			self.day+=1
			self.firstChoice()

	def jail(self):
		num = random.randint(0,4)
		if num == 0:
			print(self.rJail[0])
			self.message()
			sys.exit()
		elif num == 1 or num == 2:
			print(self.rJail[1])
			self.jailed()
		elif num == 3 or num == 4:
			print(self.rJail[2])
			self.jailed()

	def jailed(self):
		num = random.randint(0,7)
		if num == 0:
			print(self.rJailed[0])
		elif num == 1 or num == 2:
			print(self.rJailed[1])
		elif num > 2:
			print(self.rJailed[2])
		self.message()
		sys.exit()

	def message(self):
		# Message from the creator
		print("\nMay Egypt one day truly be free from oppression and dictatorship!\n")

Egypt()
