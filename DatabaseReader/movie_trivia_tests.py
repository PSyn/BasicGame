
              
import unittest
#imports all from movie_trivia file
from movie_trivia import*

class TestLibrary(unittest.TestCase):
    #sets up test databases
    movieDb={}
    ratingDB={}
    #assigns values to test databases and iterates with each test
    def setUp(self):
        self.movieDb={'Brad':['Sleepers','Assassins'],'Meg':['philadelphia','Cobra','Assassins']}
        self.ratingDb={'original sin':[12,62],'Assassins':[16,45],'Cobra':[35,50]}
        self.ratingsisDb={'original sin':[92,82],'Assassins':[82,95],'Cobra':[85,85]}
        self.ratingsisDa={'Sleepers':[85,85],'Assassins':[82,95],'Cobra':[85,85]}
    def test_insert_actor_info(self):
        """tests insert_actor_info"""
        #inserts actor and movies
        insert_actor_info('Tom',['wonder','Jetlag'],self.movieDb)
        #tests new length of database    
        self.assertEqual(len(self.movieDb),3)
        #tests all entries of database
        self.assertEqual(self.movieDb,{'Brad':['Sleepers','Assassins'],'Meg':['philadelphia','Cobra','Assassins'],'Tom':['wonder','Jetlag']})
    def test_insert_rating(self):
        """tests insert_rating function"""
        #inserts new movie and ratings
        insert_rating('Wonder',[67,88],self.ratingDb)
        #tests new length of database
        self.assertEqual(len(self.ratingDb),4)
        #tests database against actual database
        self.assertEqual(self.ratingDb,{'original sin':[12,62],'Assassins':[16,45],'Cobra':[35,50],'Wonder':[67,88]})
 
    def test_delete_movie(self):
        """tests delete movie function"""
        #deletes a movie
        delete_movie('Assassins', self.movieDb, self.ratingDb)
        #checks to see if the movie was deleted from the movies database
        self.assertEqual(self.movieDb,{'Brad':['Sleepers'],'Meg':['philadelphia','Cobra']})
        #checks to see if the movie was deleted from the ratings database
        self.assertEqual(self.ratingDb,{'original sin':[12,62],'Cobra':[35,50]})
    def test_select_where_movie_is(self):
        """tests the select where movie is function"""
        #tests spelling 1 and correct output
        self.assertEqual(select_where_movie_is('Assassins', self.movieDb),['Meg','Brad'])
        #tests spelling 2 and correct output
        self.assertEqual(select_where_movie_is('assassins', self.movieDb),['Meg','Brad'])
        
    def test_select_where_actor_is(self):
        """tests select where actor is"""
        #tests for difference in cases
        self.assertEqual(select_where_actor_is('Brad', self.movieDb),['Sleepers','Assassins'])
        self.assertEqual(select_where_actor_is('brad', self.movieDb),['Sleepers','Assassins'])
        self.assertEqual(select_where_actor_is('Meg', self.movieDb),['philadelphia','Cobra','Assassins'])
    def test_is_movie_in_database(self):
        """tests is movie in database"""
        #tests to make sure sleepers is in the database
        self.assertTrue(is_movie_in_database('Sleepers',self.movieDb))
        #tests a false movie
        self.assertFalse(is_movie_in_database('nmujjjs',self.movieDb))
    def test_select_where_rating_is(self):
        """tests select where reating is"""
        #tests different parameters
        self.assertEqual(select_where_rating_is('=', 35, True, self.ratingDb),['Cobra'])
        self.assertEqual(select_where_rating_is('<', 51, False, self.ratingDb),['Cobra','Assassins'])
        self.assertEqual(select_where_rating_is('>', 65, False, self.ratingDb),[])
    def test_get_co_actors(self):
        """tests get co actors function"""
        #confirms different spellings and responses
        self.assertEqual(get_co_actors('Brad',self.movieDb),['Meg'])
        self.assertEqual(get_co_actors('brad',self.movieDb),['Meg'])
    def test_get_common_movie(self):
        """tests get common function"""
        #tests different itterations and spellings and checks for correct response
        self.assertEqual(get_common_movie('Meg','Brad',self.movieDb),['Assassins'])
        self.assertEqual(get_common_movie('Brad','Meg',self.movieDb),['Assassins'])
        self.assertEqual(get_common_movie('brad','meg',self.movieDb),['Assassins'])
    def test_critics_darling(self):
        """tests critics darling function"""
        #checks to see if the correct response is returned for critics_darling
        self.assertEqual(critics_darling(self.movieDb,self.ratingDb),['Meg'])
        #Tests if there is a tie
        self.assertEqual(critics_darling(self.movieDb,self.ratingsisDa),['Meg','Brad'])
    def test_audience_darling(self):
        """tests audience darling function"""
        #checks to see if the correct response is returned for audience_darling
        self.assertEqual(audience_darling(self.movieDb,self.ratingDb),['Meg'])
        #Tests if there is a tie
        self.assertEqual(audience_darling(self.movieDb,self.ratingsisDa),['Meg','Brad'])
    def test_good_movies(self):
        """tests for good_movies function"""
        self.assertEqual(good_movies(self.ratingsisDb),set(['Cobra']))
        self.assertEqual(good_movies(self.ratingDb),set([]))
    def test_get_common_actors(self):
        """tests for test_get_common_actors function"""
        self.assertEqual(get_common_actors("Assassins","Cobra",self.movieDb),['Meg'])
        self.assertEqual(get_common_actors("assassins","cobra",self.movieDb),['Meg'])
unittest.main()
