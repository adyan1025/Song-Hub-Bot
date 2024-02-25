import music_request

def getArtist(artist):
    token = music_request.get_token()
    result = music_request.search_for_artist(token, artist)
    artist_name = result["name"]
    return artist_name

def getRelatedArtists(artist):
    token = music_request.get_token()
    result = music_request.search_for_artist(token, artist)
    artist_id = result["id"]
    related_artists = music_request.get_related_artists(token, artist_id)
    final_message = ""
    i = 0
    for artist in related_artists:
        i+=1
        name = artist['name']
        final_message += f"{i}. {name}\n"
    return final_message

def getTrack(artist):
    tracks = ""
    token = music_request.get_token()
    result = music_request.search_for_artist(token, artist)
    artist_id = result["id"]
    songs = music_request.get_songs_by_artists(token, artist_id)
    for i, song in enumerate(songs):
        tracks += (str(i + 1) + ". " + song['name'] + "\n")
    response = f"\n{tracks}"
    return response