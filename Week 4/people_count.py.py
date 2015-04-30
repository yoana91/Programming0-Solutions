def get_people_count(activity):
    counted_people = []
    
    for person in activity:
        if person not in counted_people:
            counted_people += [person]

    return len(counted_people)