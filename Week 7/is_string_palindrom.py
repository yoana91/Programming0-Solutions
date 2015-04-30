def is_string_palindrom(string):
    result = ""
    new_string = ""

    removable_marks = [",", ".", "!", "?", " "]

    for ch in string:
        if ch not in removable_marks:
            new_string += ch

    for ch in new_string:
        result = ch + result

    if result == new_string:
        return True

    return False
