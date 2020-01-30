#Cinema application

#Creating movie dictionary
films = {
	"Roots":[18,5],
	"Shaft":[15,5],
	"The Dictator":[5,5],
	"Polar":[15,5],
	"Green Lantern":[12,5],
	"Mind The Baby":[3,5]
	}
print(films)

while True:

#choose a movie to see

        choice = input("What movie will you like to see?: ").strip().title()

        if choice in films:
                #check user's age
                age = int(input("How old are you?: ").strip())
                if age >= films[choice][0]:

                        #check enough seats
                        num_seats = films[choice][1]

                        if num_seats >0:
                                print("Enjoy your movie!")
                                films[choice][1] = films[choice][1] -1
                        else:
                                print("Sorry, we are sold out!")
                        
                else:
                        print("You are too young to see this movie!")
                
        else:
                print("We don't have that movie now, check back next week!")
