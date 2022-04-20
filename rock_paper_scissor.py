import random
ls=["rock","paper","scissor"]
ele={1:"rock",2:"paper",3:"scissor"}

record=0
com=0
draw=0
steps=0
user=input("Enter your name: ")

try:
	while True:
		if steps<10:
			ui=int(input('\nEnter your input as 1, 2, 3 for rock, paper, scissor respectively:\n'))
			rs=random.choice(ls)
			if rs == ele[ui]:
				print(f"Computer and {user} both chose {ele[ui]} resulting in [DRAW!]\n")
				draw+=1
			elif rs=="rock" and ui==2:
				print(f"Computer chose {rs} and {user} chose {ele[ui]} resulting in [VICTORY!]\n")
				record+=1
			elif rs=="paper" and ui==3:
				print(f"Computer chose {rs} and {user} chose {ele[ui]} resulting in [VICTORY!]\n")
				record+=1
			elif rs=="scissor" and ui==1:
				print(f"Computer chose {rs} and {user} chose {ele[ui]} resulting in [VICTORY!]\n")
				record+=1
			else:
				print(f"Computer chose {rs} and {user} chose {ele[ui]} resulting in [FAILURE!]\n")
				com+=1

		if steps==9:
			steps=0	
			print(f"{user} WON {record} times.\nComputer WON {com} times.\nNo. of DRAWS are {draw}")
			if record>com:
				print(f"We Declare {user} as the WINNER!")
			elif record==com:
				print(f"This Game resulted in [DRAW] So neither {user} nor Computer would be considered as the WINNER")
			else:
				print("We Declare Computer as the WINNER!")
			record,com,draw=0,0,0
				
			co=input('Enter y to Continue OR q to Quit:\n')
			if co in "yY":
				continue
			else:
				break
				
				
		steps+=1
		
except:
	print("\nINVALID INPUT\nARE YOU TRYING TO BREAK MY PROGRAM -_-")
	input("Run the program again press enter to quit out of this one")
