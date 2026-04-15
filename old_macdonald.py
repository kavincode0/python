#OLD MACDONALD: Write a function that capitalizes the first and fourth letters of a name

def old_macdonald(name):
    Name = ""
    for i in range(len(name)):
        if i == 0 or i == 3:
            Name += name[i].upper()
        else:
            Name += name[i]

        # return name[0].upper() + name[1:3] + name[3].upper + name[4:]

    return Name


print(old_macdonald('macdonald'))