def count_occurrence(search_word, words):
    count = 0

    for word in words:
        if word == search_word:
            count += 1

    return count

def count_words(words):

    result = {}

    for word in words:

        result[word] = count_occurrence(word, words)

    return result


words = ["words", "are", "meaningful", "words", "words", "are"]

print(count_words(words))
