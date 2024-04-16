def genres(movies):
    return {genre 
            for movie in movies
            for genre in movie.genres}

def actors(movies):
    return {actors
            for movie in movies
            for actors in movie.actors}

def repeat_consecutive(xs, n):
    return [x for x in xs for _ in range(n)]

def repeat_alternating(xs, n):
    return 