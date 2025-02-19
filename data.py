best_selling_albums = [
    {
        "artist": "Michael Jackson",
        "title": "Thriller",
        "year": 1982,
        "genres": ["pop", "post-disco", "funk", "rock"],
        "sale": 70000000,
    },
    {
        "artist": "AC/DC",
        "title": "Back in Black",
        "year": 1980,
        "genres": ["hard rock"],
        "sale": 50000000,
    },
    {
        "artist": "Whitney Houston",
        "title": "The Bodyguard",
        "year": 1992,
        "genres": ["r&b", "soul", "pop", "soundtrack"],
        "sale": 45000000,
    },
    {
        "artist": "Pink Floyd",
        "title": "The Dark Side of the Moon",
        "year": 1973,
        "genres": ["progressive rock"],
        "sale": 45000000,
    },
    {
        "artist": "Eagles",
        "title": "Their Greatest Hits (1971 - 1975)",
        "year": 1976,
        "genres": ["country rock", "soft rock", "folk rock"],
        "sale": 44000000,
    },
    {
        "artist": "Eagles",
        "title": "Hotel California",
        "year": 1976,
        "genres": ["soft rock"],
        "sale": 42000000,
    },
    {
        "artist": "Shania Twain",
        "title": "Come On Over",
        "year": 1997,
        "genres": ["country", "pop"],
        "sale": 40000000,
    },
    {
        "artist": "Fleetwood Mac",
        "title": "Rumours",
        "year": 1977,
        "genres": ["soft rock"],
        "sale": 40000000,
    },
]

# WRITE YOUR CODE AFTER THIS LINE
# Initialize total sales
total_sales = 0

# Iterate through each album and add the sales to total_sales
for album in best_selling_albums:
    total_sales += album["sale"]

# Calculate the average sales
average_sale = total_sales / len(best_selling_albums)

print("Average sales income of the albums:", average_sale)

# Initialize total age
total_age = 0
current_year = datetime.now().year

# Iterate through each album and add the age to total_age
for album in best_selling_albums:
    album_age = current_year - album["year"]
    total_age += album_age

# Calculate the average age
average_age = total_age / len(best_selling_albums)

print("Average age of the albums:", average_age)

# Initialize variables to keep track of the newest and oldest albums
newest_album = best_selling_albums[0]
oldest_album = best_selling_albums[0]

# Iterate through each album and update the newest and oldest albums
for album in best_selling_albums:
    if album["year"] > newest_album["year"]:
        newest_album = album
    if album["year"] < oldest_album["year"]:
        oldest_album = album

print("Newest album:", newest_album)
print("Oldest album:", oldest_album)

# Initialize the albums_of_eagles dictionary
albums_of_eagles = {
    "sales": 0,
    "is_both_soft_rock": True
}

# Calculate the total sales of Eagles albums
for album in best_selling_albums:
    if album["artist"] == "Eagles":
        albums_of_eagles["sales"] += album["sale"]

# Check if both Eagles albums are categorized by genre as "soft rock"
for album in best_selling_albums:
    if album["artist"] == "Eagles":
        if "soft rock" not in album["genres"]:
            albums_of_eagles["is_both_soft_rock"] = False
            break

print(albums_of_eagles)

# Add the i_like_it key to each album
for album in best_selling_albums:
    if album["artist"] == "Eagles" and album["title"] == "Hotel California":
        album["i_like_it"] = True
    elif album["artist"] == "Michael Jackson" and album["title"] == "Thriller":
        album["i_like_it"] = True
    else:
        album["i_like_it"] = False

# Ensure at least one album has i_like_it set to True
if not any(album["i_like_it"] for album in best_selling_albums):
    best_selling_albums[0]["i_like_it"] = True

print(best_selling_albums)
