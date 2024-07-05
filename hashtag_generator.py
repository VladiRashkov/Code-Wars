def generate_hashtag(s):
    if len(s) == 0:
        return False

    cap = s.title()
    no_spaces = cap.replace(' ', '')
    hashed = '#'+no_spaces

    return hashed if len(no_spaces) < 140 else False


print(generate_hashtag(' Hello there thanks for trying my Kata'))
