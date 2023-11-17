#Ask first friend the movies they like. Save it in a list
#Ask another friend the same question. If the movie is in the first friend's list, 
#Print "You both like "name of the movie"
#Continue until they is atleast 3 movies they both likes

movies=input("What movies you like(movies separated by commas): ")
movieList=movies.split(",")

commonMovieCount=0
commonMovie=[]
while True:
    movie=input("What movie do you like: ")
    if  movie in movieList:
        commonMovieCount+=1
        commonMovie.append(movie)

    if(commonMovieCount>=3):
        break

    else:
        print("Try again")
print("You both like:" ,commonMovie)