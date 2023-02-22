def add_songs(*args):
    song_dictionary = {}

    for song_title, lyrics in args:
        if song_title not in song_dictionary:
            song_dictionary[song_title] = []
        song_dictionary[song_title].extend(lyrics)

    result = []

    for song_title, lyrics in song_dictionary.items():
        result.append('- ' + song_title)
        if lyrics:
            result.extend(lyrics)

    return "\n".join(result)


print(add_songs(
    ("Bohemian Rhapsody", []),
    ("Just in Time",
     ["Just in time, I found you just in time",
      "Before you came, my time was running low",
      "I was lost, the losing dice were tossed",
      "My bridges all were crossed, nowhere to go"])
))