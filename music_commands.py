import music_request

def getArtist(artist):
    token = music_request.get_token()
    result = music_request.search_for_artist(token, artist)
    artist_name = result["name"]
    return artist_name

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