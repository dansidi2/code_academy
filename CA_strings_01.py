def username_generator(first_name, last_name):
    if len(first_name) <= 3:
        first_slice = first_name
    else:
        first_slice = first_name[:3]

    if len(last_name) <= 4:
        last_slice = last_name
    else:
        last_slice = last_name[:4]
    username = first_slice + last_slice
    return username


def password_generator(first_name, last_name):
    pass


print(username_generator('Abe', 'Simpson'))
