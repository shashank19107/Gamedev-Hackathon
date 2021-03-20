import random


def user_bats_first(lives,overs):
	num_overs=0
	target=0
	while(num_overs<overs):
		balls=1
		while(balls<=6):
			print("{:.1f}".format(num_overs+balls/10))

			print("Wickets: "+str(lives))
			print("Current Runs: "+str(target))
			user_num=int(input("Enter num bw 1 to 6: "))
			computer_num=random.choice([1,2,3,4,5,6])
			print("Computer num: "+str(computer_num))

			if(user_num==computer_num):
					lives=lives-1
					print("Out!Wicket lost")
					if(lives<=0):
						print("Innings Complete!")
						return target
			else:
				target+=user_num

			balls=balls+1
		num_overs+=1
	return target


def user_bowls_first(lives,overs):
	num_overs=0
	target=0
	while(num_overs<overs):
		balls=1
		while(balls<=6):
			print("{:.1f}".format(num_overs+balls/10))
			print("Wickets: "+str(lives))
			print("Current Runs: "+str(target))
			user_num=int(input("Enter num bw 1 to 6: "))
			computer_num=random.choice([1,2,3,4,5,6])
			print("Computer num: "+str(computer_num))

			if(user_num==computer_num):
				lives=lives-1
				print("Out!Wicket lost")
				if(lives<=0):
					print("Innings Complete!")
					return target
			else:
				target+=computer_num

			balls+=1
		num_overs+=1
	return target

def user_bats_second(lives,overs,limit):
	num_overs=0
	target=0
	while(num_overs<overs):
		balls=1
		while(balls<=6):
			print("{:.1f}".format(num_overs+balls/10))
			print("Wickets: "+str(lives))
			print("Current Runs: "+str(target))
			user_num=int(input("Enter num bw 1 to 6: "))
			computer_num=random.choice([1,2,3,4,5,6])
			print("Computer num: "+str(computer_num))

			if(user_num==computer_num):
					lives=lives-1
					print("Out!Wicket lost")
					if(lives<=0):
						print("You lost the match!")
						print("You lost by "+str(limit-target)+" runs!")
						return 0

			else:
				target+=user_num
			if(target>limit):
				print("You won!")
				print("You won by "+str(lives)+" wickets!")
				return 1

			balls=balls+1
		num_overs+=1
	print("You lost by "+str(limit-target)+" runs!")
	return 0

def user_balls_second(lives,overs,limit):
	num_overs=0
	target=0
	while(num_overs<overs):
		balls=1
		while(balls<=6):
			print("{:.1f}".format(num_overs+balls/10))
			print("Wickets: "+str(lives))
			print("Current Runs: "+str(target))
			user_num=int(input("Enter num bw 1 to 6: "))
			computer_num=random.choice([1,2,3,4,5,6])
			print("Computer num: "+str(computer_num))

			if(user_num==computer_num):
					lives=lives-1
					print("Out!Wicket lost")
					if(lives<=0):
						print("You won the match!")
						print("You won by "+str(limit-target)+" runs!")
						return 1 
			else:
				target+=computer_num
			if(target>limit):
				print("You lost!")
				print("You lost by "+str(lives)+" wickets!")
				return 0

			balls=balls+1
		num_overs+=1
	print("You won the match!")
	print("You won by "+str(limit-target)+" runs!")
	return 1



if __name__ == "__main__":


	lives=3
	overs=2 #int(input(('Enter overs: ')))
	#print("Hello")

	#toss
	print("Toss")
	toss_choice=int(input("Enter 0 or 1: "))
	result=random.choice([0,1])
	choice=0
	if(toss_choice!=result):
		print("You lost the toss!")
		choice=random.choice([0,1]) #0-bat first,1-ball first
		if(choice==0):
			print("Computer chose to bat first")
		else:
			print("Computer chose to ball first")

	else:
		print("You won the toss!")
		print("Choices : 0)Ball first 1)Bat first")
		choice=int(input("Enter 0 or 1: ")) #0-ball first,1-bat first
	#declaration
	if(choice==0):
		print("You are balling first!")
	else:
		print("You are batting first!")

	#simulation
	result=0

	if(choice==0):
		print("First Innings start!")
		target=user_bowls_first(lives,overs)
		print(str(target)+" runs scored by computer!")
		print(str(target+1)+" runs to win!")
		print("Second Innings start!")
		result=user_bats_second(lives,overs,target)
	else:
		print("First Innings start!")
		target=user_bats_first(lives,overs)
		print(str(target)+" runs scored by you!")
		print(str(target+1)+" runs to protect!")
		print("Second Innings start!")
		result=user_balls_second(lives,overs,target)
	if(result==1):
			print("Congratulations!")
	else:
			print("Better luck next time!")



























