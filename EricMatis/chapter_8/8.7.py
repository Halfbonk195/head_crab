def make_album(artist, album, numb_tracks=None):
    if numb_tracks:
        album_dict = {'artist': artist.title(), 'album': album.title(), 'number tracks': numb_tracks}
    else:
        album_dict = {'artist': artist.title(), 'album': album.title()}
    return album_dict


text = make_album('Einmusik', 'bella mar 09', 5)
print(text)

text = make_album('artbat', 'our space')
print(text)

text = make_album('artbat', 'horizon', 10)
print(text)
