def is_long(text:str):
    if (character_count := len(text)) > 100:
        return True
    return False