# Simple Movie Recommendation System

# Sample movie dataset (you can add more)

movies = {
    "Inception": ["sci-fi", "thriller", "action"],
    "Interstellar": ["sci-fi", "drama"],
    "The Dark Knight": ["action", "crime"],
    "Tenet": ["sci-fi", "action"],
    "Avengers": ["action", "superhero"],
    "Titanic": ["romance", "drama"],
    "Notebook": ["romance", "drama"]
}


def recommend(movie_name):
    if movie_name not in movies:
        print("Movie not found in database.")
        return

    print(f"\nMovies similar to '{movie_name}':")
    
    target_genres = movies[movie_name]
    scores = {}

    # Compare with every other movie
    for title, genres in movies.items():
        if title == movie_name:
            continue

        # Score = number of matching genres
        common = len(set(target_genres) & set(genres))
        if common > 0:
            scores[title] = common

    # Sort by score
    sorted_scores = sorted(scores.items(), key=lambda x: x[1], reverse=True)

    # Show recommendations
    if not sorted_scores:
        print("No similar movies found.")
    else:
        for movie, score in sorted_scores:
            print(f"- {movie} (Match Score: {score})")


# -------- Main -------- #
print("Available movies:")
for m in movies:
    print(" -", m)

chosen = input("\nEnter a movie name to get recommendations: ")
recommend(chosen)