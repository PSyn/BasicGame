#PK - nested
#imports random so random values can be calculated
import random

#prints initial introduction to game
def print_intro():

    print ("""
Congrats, you are the newest ruler of ancient Samaria, elected for a ten year term
of office. Your duties are to distribute food, direct farming, and buy and sell land
as needed to support your people. Watch out for rat infestations and the resultant
plague! Grain is the general currency, measured in bushels. The following will help
you in your decisions:

(a) Each person needs at least 20 bushels of grain per year to survive.
(b) Each person can farm at most 10 acres of land.
(c) It takes 2 bushels of grain to farm an acre of land.
(d) The market price for land fluctuates yearly.

Rule wisely and you will be showered with appreciation at the end of your term. Rule
poorly and you will be kicked out of office!
    """)


#defines overall BasicGame function and parameters for output
def BasicGame():
    starved = 0
    immigrants = 5
    population = 100
    harvest = 3000 # total bushels harvested
    bushels_per_acre = 3 # amount harvested for each acre planted
    rats_ate = 200 # bushels destroyed by rats
    bushels_in_storage = 2800
    acres_owned = 1000
    cost_per_acre = 19 # each acre costs this many bushels
    plague_deaths = 0
    total_starved = 0 #records total number of people starved during the game
    total_population = 0 #records the total population during the game
    
    print_intro()

    #defines range of game in years  
    for year in range(1,11):
        print("O great Lord!\n")
        print("You are in year", year, "of your ten year rule.")
        print("In the previous year,", starved, "people starved to death.")
        print("In the previous year", immigrants, "people entered the kingdom.")
        print("The population is now", population,".")
        print("We harvested", harvest," bushels at", bushels_per_acre," bushels per acre.")
        print("Rats destroyed", rats_ate, " bushels, leaving", bushels_in_storage, " bushels in storage.")
        print("The city owns", acres_owned," acres of land.")
        print("Land is currently worth", cost_per_acre," bushels per acre.")
        print("There were", plague_deaths,"deaths from the plague")

        #this records the total number of people starved throughout the game
        total_starved = total_starved + starved
        #this records the total population over the whole game
        total_population = total_population + population

        def ask_to_buy_land(bushels, cost):
            '''Ask user how many bushels to spend buying land.'''
            acres = input("How many acres will you buy? ")
            while acres * cost > bushels:
                print "O great Lord, we have but", bushels, "bushels of grain!"
                acres = input("How many acres will you buy? ")
            return acres

        def ask_to_sell_land(acres):
            '''Ask user how much land they want to sell. '''
            land = input ("How many acres will you sell? ")
            while land > acres: #defines rejection if attempting to sell more land than is owned
                print "O great Lord, we have but", acres, "acres to sell!"
                land = input ("How many acres will you sell? ")
            return land

        def ask_to_feed(bushels):
            '''Ask user how many bushels they want to use for feeding. '''
            feed = input ("How many bushels will you feed your people? ")
            while feed  > bushels: #defines rejection if attempting to use more bushels than are owned
                print "O great Lord, we have but", bushels, "bushels of grain!"
                feed = input ("How many bushels will you feed your people? ")
            return feed

        def ask_to_cultivate(acres, population, bushels):
            '''Ask user how much land they want to plant seed in '''
            cultivate = input ("How many acres will you cultivate? ")
            while cultivate > acres: #defines rejection if attempting to cultivate more acres than are owned
                print "O great Lord, we have but", acres, "acres of land!"
                cultivate = input ("How many acres will you cultivate? ")
            while cultivate > population*10: #defines rejection if attempting to cultivate more acres than have enough people for
                print "O great Lord, we have but", population, "people to cultivate the land!"
                cultivate = input ("How many acres will you cultivate? ")
            while cultivate > bushels*2: #defines rejection if attempting to cultivate more acres than have enough bushels for
                print "O great Lord, we have but", bushels, "bushels of grain!"
                cultivate = input ("How many acres will you cultivate? ")
            return cultivate

        #the following code changes the overall parameters of how many acres have been bought and adjusts the bushel count
        acres_bought = ask_to_buy_land(bushels_in_storage, cost_per_acre)
        acres_owned = acres_owned + acres_bought
        bushels_in_storage = bushels_in_storage - acres_bought*cost_per_acre

        #if no acres are bough the following code records how many acres are sold and the impact on total acres and bushels
        if acres_bought == 0:
            acres_sold = ask_to_sell_land(acres_owned)
            acres_owned = acres_owned - acres_sold
            bushels_in_storage = bushels_in_storage + (acres_sold*cost_per_acre)

        #records the effect on total bushels of feeding people
        bushels_fed = ask_to_feed(bushels_in_storage)
        bushels_in_storage = bushels_in_storage - bushels_fed

        #records the effect on bushels of cultivating land and records how much land is cultivated
        land_cultivated = ask_to_cultivate(acres_owned, population, bushels_in_storage)
        bushes_in_storage = bushels_in_storage - land_cultivated*2 

        def is_plague():
            """Determines if there is a plague"""
            plague_chance = random.randint(1,100)
            if plague_chance <=15: #defines the plague chance of 15%
                return True
            else:
                return False

        plague = is_plague()
        if plague == True: #if there was a chance of a plague the deaths from plague are have the population, also records overall reduction in population
            plague_deaths = population/2
            population = population - int(plague_deaths)
        else:
            plague_deaths = 0

        def num_starving(population, bushels):
            """determines how many people starved"""
            if bushels < (population*20): #defines how many people starve if not enough bushels are fed
                people_starved = int(population - bushels/20)
                return people_starved
            else:
                return 0

        #records the amount of starved people
        starved = num_starving(population, bushels_fed)

        #if the total amount of starved peole is equal or greater than 45% the game ends
        if  float(starved)/float(population) >= (45.0/100.0) and starved > 0:
            print "You have starved too many people and have been thrown out of office"
            return
        #records the population change from having people starve
        population = population - starved

        def num_immigrants(land, grain_in_storage, population, num_starving):
            """determines the amount of people that came to the city"""
            if starved == 0: #sets that people may enter if no one has starved
                new_people = ((20*land) + grain_in_storage)/((100*population)+1) #calculates how many new immigrants there are
                return new_people
            else:
                return 0

        #records the total number of immigrants and adjusts the population accordingly
        immigrants = num_immigrants(acres_owned, bushels_in_storage, population, starved)
        population = population + immigrants
      
        
        def get_harvest():
            """defines how good the harvest was"""
            harvest_chance = random.randint(1,8)
            return harvest_chance

        #records how many bushels per acre were harvested, the total harvest and the impact on bushels in storage
        bushels_per_acre = get_harvest()
        harvest = bushels_per_acre * land_cultivated
        bushels_in_storage = bushels_in_storage + harvest

        def do_rats_infest():
            """determines if rats do anything"""
            rat_chance = random.randint(1,100)
            if rat_chance <= 40: #defines that there is a 40% chance that rats do damage
                return True
            else:
                return False

        def percent_destroyed():
            """determines if rats do anything, how much damage they do"""
            rat_percent_chance = random.randint(10,30) #gives an integer for how much damage rats do
            rat_float_chance = float(rat_percent_chance)/100 #converts above integer to decimal value
            return rat_float_chance

        #first defines if rats due anything and if this is true adjusts how much rats ate, finally it records the impact on bushels in storage
        rats_ate = do_rats_infest()
        if rats_ate == True:
            rats_ate = percent_destroyed()
            rats_ate = int(rats_ate * bushels_in_storage)
            bushels_in_storage = bushels_in_storage - rats_ate
        else:
            rats_ate = 0
        
        def price_of_land():
            """determines how much the price of land is next year"""
            price_chance = random.randint(16,22) #generates random price per acre
            return price_chance

        #records the cost per acre based on random chance
        cost_per_acre = price_of_land()

    def totals(starved_over_game, population, total_population, acres_owned):
        """This functon calculates the ratio of total people starved during the game versus the total population,
        if the result is less than 20% this is acceptable, otherwise the person could have done something better.
        Likewise, the ratio of acres to population is calculated, as long as the ratio is not worse than when the game
        began the person has done a good job.  Various combinations of these output different values."""
        ratio_starved = float(starved_over_game / total_population) #ratio of total of starved people to the total population in years 1 through 10
        ratio_acres = float(acres_owned/population) #ratio of acres owned after year ten to the number of people
        if ratio_starved <= float(20/100) and ratio_acres > 10: #defines parameter for what a great job is, in this case as long as acres/population wasnt less than in year one and no more than 20% of people starved 
            return "You did a great job!. The total number of people that starved was", total_starved, "and your ratio of acres to population was", float(acres_owned/population),"."
        #defines an okay job as one where either of the above two parameters were not met
        elif ratio_starved >= float (20/100) and ratio_acres > 10:
            return "You could have done better. The total number of people that starved was", total_starved, "and your ratio of acres to population was", float(acres_owned/population),"."
        elif ratio_starved >= float (20/100) and ratio_acres < 10:
            return "You could have done better. The total number of people that starved was", total_starved, "and your ratio of acres to population was", float(acres_owned/population),"."
        #defines as a terrible job where acres/population were lost and over 20% of the population starved
        else:
            return "You are a terrible leader. The total number of people that starved was", total_starved, "and your ratio of acres to population was", float(acres_owned/population),"."
    print "" #prints empty space
    print totals(total_starved, population, total_population, acres_owned) #prints what kind of job the player did as well as their final scores
        
        
BasicGame()

        

     

