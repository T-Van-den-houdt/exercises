def directors(movies):
    return {movie.director for movie in movies}

def common_elements(xs, ys):
    return {c for c in xs if c in ys}