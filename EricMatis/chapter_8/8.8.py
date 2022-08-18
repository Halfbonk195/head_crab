def make_album(artist, album, numb_tracks=None):
    """Возвращает словарь по ключам artist, album, number_tracks"""
    if numb_tracks:
        album_dict = {'artist': artist.title(), 'album': album.title(), 'number_tracks': numb_tracks}
    else:
        album_dict = {'artist': artist.title(), 'album': album.title()}
    return album_dict


while True:
    print('Enter the name of the artist or the name of the group and their album, as well as the number of tracks in '
          'the album')
    print('Press "q" to end')

    artist = input('Enter the name: ')
    if artist == 'q':
        break

    album = input('Enter the album: ')
    if artist == 'q':
        break

    numb_tracks = input('Enter number of tracks in album: ')
    if artist == 'q':
        break

    text = make_album(artist, album, numb_tracks)
    print(text, '\n')
