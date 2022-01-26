def to_nato(words):
    converted_string = ""
    for character in words:
        if character.upper() in NATO:
            converted_string += NATO(character.upper())
    else:
        converted_string += character
    
    return converted_string