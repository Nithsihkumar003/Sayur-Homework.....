first_friend_movies = []
matching_movie_count = 0

while matching_movie_count < 3:
    movie_1 = input("First friend, please enter a movie you like: ")
    first_friend_movies.append(movie_1)
    movie_2 = input("Second friend, please enter a movie you like: ")
    if movie_2 in first_friend_movies:
        print(f"You both like '{movie_2}'")
        matching_movie_count += 1