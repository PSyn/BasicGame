#Kevin Muriuki and Philip Kyd
#imports csv reader
import csv

def create_actors_DB(actor_file):
    '''Create a dictionary keyed on actors from a text file'''
    #opens whichever file is passed as actor_file
    f = open(actor_file)
    #creates a dictionary called movieInfo
    movieInfo = {}
    #loops for each line in the file f
    for line in f:
        #defines line and strips white space from both ends
        line = line.rstrip().lstrip()
        #defines actorAndMovies and splits line by a comma
        actorAndMovies = line.split(',')
        #defines the actor as the first split
        actor = actorAndMovies[0]
        #strips white space for x # of movies 
        movies = [x.lstrip().rstrip() for x in actorAndMovies[1:]]
        #turns the movieInfo dictionary with actor as the key and
        #the movies as a set of movies as the values for said actor
        movieInfo[actor] = set(movies)
    f.close() #closes the file
    return movieInfo #returns a dictionary called movieInfo

def create_ratings_DB(ratings_file):
    '''make a dictionary from the rotten tomatoes csv file'''
    scores_dict = {}
    #opens ratings_file as a "read" file, works for csv file
    with open(ratings_file, 'r') as csvfile:
        #uses the csv.reader function on the csv file, reader function iterates over lines
        reader = csv.reader(csvfile)
        #returns a string when next() is called
        reader.next()
        #as long as a row exists in the file
        for row in reader:
            #creates a dictionary in which they second and third rows are keyed on the first row
            scores_dict[row[0]] = [row[1], row[2]]
    return scores_dict

def insert_actor_info(actor, movies, movie_Db):
    """ appends new movies to a current actor or a
        new actor with movies, modifies the movie_db
    """
    #checks to see if an actor is in the database
    if actor in movie_Db:
        #adds the list of movies as individual values to the current list
        movie_Db[actor].extend(movies)
    else:
        #creates a new key and value pair
        movie_Db[actor] = (movies)
        
def insert_rating(movie, ratings, ratings_Db):
    """updates the critics and audiance rating for a given movie"""
    #checks if a movie is in ratings_Db
    if movie in ratings_Db:
        #Changes new ratings to the associated movie
        ratings_Db[movie]=ratings
    else:
        #creates a movie and associated ratings
        ratings_Db[movie] =ratings
                        
def delete_movie(movie, movie_Db, ratings_Db):
    """ deletes all information from the database
        that corresponds to a specific movie
    """
    #loops for actor in the movie database
    moviie=movie.title() 
    for actor in movie_Db:
        #checks to make sure that the movie exists and then removes it
        for moviee in movie_Db[actor]:           
            if moviee==moviie:
                movie_Db[actor].remove(moviee)
                break
    #removes the movie from the ratings database
    if movie in ratings_Db:
        del ratings_Db[moviie] 
                        
def select_where_actor_is(actor_name, movie_Db):
    """ if an actor is input into the function,
        returns a list of all associated movies
    """
    #capitalizes the actor name
    actor=actor_name.title()
    #returns the value for the actor key
    return movie_Db[actor]

def is_movie_in_database(movie_name, movie_Db):
    """searches for a movie to check if it exists in the database"""
    #initially sets in_database variable as false, will only change if movie is in database
    in_database=False
    #loops through database, points actor towards keys and movies towards values
    for actor, movies in movie_Db.items(): 
         #sets variable k to loop through the movies      
         for k in movies:
              #sets movi equal to the given movie name
              movi=movie_name
              #checks if there is a value k, that is equal to the movie name, if so returns True
              if k.lower()== movi.lower():
                   in_database=True
    
    return in_database
    
def select_where_movie_is(movie_name, movie_Db):
    """returns a list of actors for a given movie"""
    #creates empty list for actors
    actors=[]
    #loops through the items in the movie database assigning actor to the keys and movies to the values
    for actor, movies in movie_Db.items():       
         #same as above
         for k in movies:
              movi=movie_name
              if k.lower()== movi.lower():
                   actors.append(actor)
    return (actors)   

    
def select_where_rating_is(comparison, targeted_rating, is_critic, ratings_Db):
    """ returns a list of movies based on an associated rating,
        can be lesser, equal to or greater than
    """
    #creates empty movie list
    movies=[]
    #loops through ratings_Db 
    for movie in ratings_Db:
        #determines if the critic rating will be used and then compares the input rating and appends accordingly
        if is_critic==True:
            if comparison=='=':               
                if int(ratings_Db[movie][0])== targeted_rating:
                    movies.append(movie)
            if comparison=='>':               
                if int(ratings_Db[movie][0])> targeted_rating:
                    movies.append(movie)
            if comparison=='<':               
                if int(ratings_Db[movie][0])< targeted_rating:
                    movies.append(movie)
        #if the critic rating is not used will use the audiance rating and complete the same as above
        elif is_critic==False:
            if comparison=='=':               
                if int(ratings_Db[movie][1])== targeted_rating:
                    movies.append(movie)
            if comparison=='>':               
                if int(ratings_Db[movie][1])> targeted_rating:
                    movies.append(movie)
            if comparison=='<':               
                if int(ratings_Db[movie][1])< targeted_rating:
                    movies.append(movie) 
    return movies  
    
def get_co_actors(actor_name, movie_Db):
    #creates empty co_actors list
    co_actors=[]
    #uses movies variable to stores the movies associated with an actor
    movies=select_where_actor_is(actor_name,movie_Db)
    #loops through the above stored list
    for movie in movies:
        #uses the movies from above and populates actors who were in those movies
        co_actors1=select_where_movie_is(movie,movie_Db)
        #adds the list of co_actors to the co_actors list
        co_actors.extend(co_actors1)
        #correctly capitalizes
        actor=actor_name.title()
        #removes the original actor from the list
        co_actors.remove(actor)
    #returns a list as a set (removes multiple instances of actors)
    return list(set(co_actors))
    
def get_common_movie(actor1, actor2, movie_Db):
    """finds out which movies two actors are together in and returns this"""
    #sets variable movie1 as a list of movies the first actor has acted in
    movie1=select_where_actor_is(actor1, movie_Db)
    #sets variable movie2 as a list of movies the second actor has acted in
    movie2=select_where_actor_is(actor2, movie_Db)
    #sets the variable common_movies as a list, with repeats removed (set) 
    #that used the intersection command to find common movies amoung the set
    common_movies=list(set(movie1).intersection(set(movie2)))
    return common_movies

def critics_darling(movie_Db, ratings_Db):
    """ returns a list of actor(s) that have the movies
        with the highest critics ratings
    """
    #sets the initial highest average as 0
    highest_average=0
    #creates an empty list called darling (list will account for ties)
    darling=[]  
    #loops through key values in movie_Db 
    for actor in movie_Db:
        #initializes variable at 0
        total_ratings=0
        #initializes count at 0
        count=0
        #sets variable movies as a list that each actor has acted in
        movies=movie_Db[actor]
        #loops through the list of movies for each actor
        for movie in movies:
            #checks if a movie from the movies list has a rating
            if movie in ratings_Db:
                #extracts the critic rating from the ratings database and stores it in rating
                rating=ratings_Db[movie][0]
                #itirates the count as +1
                count+=1
            else:
                #if no rating is found stores the rating as 0
                rating=0
            #adds the rating to toal_Ratngs             
            total_ratings+=int(rating)
        #sets a base that if the count is 0 the average will be zero
        if count==0:
            average=0
        else:
            #sets the average rating as the total rating divided by the number ov counts
            average=total_ratings/count
        if average>highest_average:
            highest_average=average
            
            #creates an empty list called darling
            darling=[]
            #adds the actor to the darling list
            darling.append(actor)
            
        #only changes the highest average if the average is equal to the highest average
        if average==highest_average:
    
            highest_average=average
            darling.append(actor)
    
    return list(set(darling))
    
def audience_darling(movie_Db, ratings_Db):
    """ returns a list of actor(s) that have the movies
        with the highest audiance ratings
    """
    #repeats above but for the audiance rating
    highest_average=0
    darling=[]   
    for actor in movie_Db:
        total_ratings=0
        count=0
        movies=movie_Db[actor]
        for movie in movies:
            if movie in ratings_Db:
                rating=ratings_Db[movie][1]
                count+=1
            else:
                rating=0               
            total_ratings+=int(rating)
        if count==0:
            average=0
        else:
            average=total_ratings/count
        if average>highest_average:
            highest_average=average
            darling=[]
            darling.append(actor)
        if average==highest_average:
            highest_average=average
            darling.append(actor)
    return list(set(darling))
       
def good_movies(ratings_Db):
    """ gives a set of movies that both critics and
        audiances scored over an 85
    """
    #sets critica as case a, where the rating is equal to 85
    critica=select_where_rating_is('=', 85, True, ratings_Db)
    #sets criticb as case b, where teh erating is greater than 85
    criticb=select_where_rating_is('>', 85, True, ratings_Db)
    #sets critic as the union of a and b, making it greater or equal to
    critics=set(critica).union(set(criticb))
    #defines the same as the above but for the audiance
    audiencea=select_where_rating_is('>', 85, False, ratings_Db)
    audienceb=select_where_rating_is('=', 85, False, ratings_Db)
    audience=set(audiencea).union(set(audienceb))
    #finds the intersection of movies that have both an audiance and critic rating above 85
    good_movies=set(critics).intersection(set(audience))
    return good_movies
        
def get_common_actors(movie1, movie2, movies_Db):
    """returns which actors are in both given movies"""
    #sets actors1 as a list of actors in the first movie 
    actors1=select_where_movie_is(movie1,movies_Db)
    #sets actirs2 as a list of actors in the second movie
    actors2=select_where_movie_is(movie2,movies_Db)
    #finds the intersection for the above two and removes any duplicates
    common_actors=list(set(actors1).intersection(set(actors2)))
    return common_actors


def main():
    #calls create_actors_DB on the movies.txt file and stores it as actor_DB
    actor_DB = create_actors_DB('movies.txt')
    ratings_DB = create_ratings_DB('moviescores.csv')
    print" "
    #sends initial welcome message
    print " Welcome to the Movie Database (it contains actors and associated movies and ratings)! You have the following options:"  
    #prints a list of options
    print """
                 Enter 1 to select an actor and get his/her co-actors.
                 Enter 2 to get common movies acted by any given two actors.
                 Enter 3 to get the highest rated actor by the critics.
                 Enter 4 to get highest rated actor by the audience.
                 Enter 5 to get highly rated(=>85) movies.
                 Enter 6 to get common actors in any pair of movies.
                 Enter 7 to Add an actor and associated movies to the database.
                 Enter 8 to Add ratings for a movie to the database.
                 Enter 9 to Remove movies from the database.
                 Enter 10 Exit."""
    print ""
    #asks the user to select a choice from the above list
    user_choice = input("What would you like to do? Enter your choice as mentioned above")      
    
    if user_choice == 1:
        #asks the user which actor they would like to look up
        actor = raw_input("Which actor would you like to look up?")
        #lowers the actor name
        actor = actor.lower()
        #appropriately capitalizes the actor name
        actor = actor.title()
        #checks if the actor is in the database
        if actor in actor_DB:
            #calls the get_co_actors function and prints the list of co-actors
            actors = get_co_actors(actor, actor_DB)
            print "The co-actors are", actors
            main()
            
        else:
            #prints an error message
            print" "
            print "The selected actor is not in our database."
            main()
    if user_choice == 2:
        #complete same as above but ask for two actor inputs
        actor1 = raw_input("Which is the first actor?")
        actor2 = raw_input("Which is the second actor?")
        actor1 = actor1.lower()
        actor1 = actor1.title()
        actor2 = actor2.lower()
        actor2 = actor2.title()
        #determines if the actors are in the database
        if actor1 not in actor_DB:
            print actor1, "is not in our database"
            
        if actor2 not in actor_DB:
            print actor2, "is not in our database"
           
        elif actor1 in actor_DB and actor2 in actor_DB:
            #calls the get_common_movies function and as long as there are common movies prints the movies
            common_movies = get_common_movie(actor1, actor2, actor_DB)
            if common_movies != []:
                print "The common movies are", common_movies
                main()
            else:
                print "These actors have no movies in common."
                main()
        main()
    if user_choice == 3:
        #calls critics_darling and prints the result
        actor = critics_darling(actor_DB, ratings_DB)
        print "The highest rated actor by the critics is",(actor)
        main()
    if user_choice == 4:
        #calls audience_darling and prints the result
        actor = audience_darling(actor_DB, ratings_DB)
        print " The highest rated by the audience is",(actor)
        main()
    if user_choice == 5:
        #calls the good_movies function and prints the list of good movies
        movie = good_movies(ratings_DB)
        print "The top movies are:", movie
        main()
        
    if user_choice == 6:
        #asks for the first movie
        movie1 = raw_input("Which is the first movie?")
        #determines if the movie is in the database
        in1=is_movie_in_database(movie1,actor_DB)
        #asks for the second movie name
        movie2 = raw_input("Which is the second movie?")
        #repeats
        in2=is_movie_in_database(movie2,actor_DB)
        #determines if the movies exists
        if in1==True and in2==True:
            common_actors = get_common_actors(movie1, movie2, actor_DB)
            if common_actors != []:
                print "The common actors are", common_actors
                main()
            else:
                print "There are no common actors in these movies"
                main()
        if in1==False:
            print movie1,'is not in our database'
        if in2==False:
            print movie2,' is not in our database'
        main()
    if user_choice == 7:
        #prompts for an actor to add
        actor = raw_input("Which actor would you like to add to the database?")
        #prompts for movies to add
        movies = raw_input("Please provide a list of movies to add to the database.")
        #calls the insert actor_info function to add the actor and movies
        insert_actor_info(actor, movies, actor_DB)
        main()
    if user_choice == 8:
        #prompts to select which movie to add ratings to
        movie = raw_input("Which movie would you like to add ratings to?")
        #prompts to select what ratings to add
        ratings = raw_input("What are the ratings that you would like to add?Enclose in square brackets")
        #calls the insert_rating function to add the ratings
        insert_rating(movie, ratings, ratings_DB)
        
        main()
    if user_choice == 9:
        #prompts which movie to delete
        movie_del = raw_input("Which movie would you like to delete from the database?")
        #calls the delete movie function to delete the selected movie
        delete_movie(movie_del, actor_DB, ratings_DB)
        main()
        
    #exits if the user types 10
    if user_choice == 10:
        return
   
if __name__ == '__main__':
    main()
    


   

  
