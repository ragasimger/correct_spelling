def correct_spelling(input_text, local_words):
    """
    Corrects the spelling of words in input_text using a list of local words.

    Arguments:
        input_text (str): The input text to correct.
        local_words (list): A list of local words.

    Returns:
        corrected_text (str): The corrected text with spelling mistakes fixed.
    """
    words = input_text.split()  # Split input_text into words
    corrected_words = []

    for word in words:
        # Check if the word is a misspelled word, if yes, replace it with the correct word from local_words
        if word.lower() in local_words:
            corrected_word = local_words[local_words.index(word.lower())]
        else:
            # If the word is not in local_words, find the closest match using Levenshtein distance
            corrected_word = get_closest_match(word.lower(), local_words)

        corrected_words.append(corrected_word)

    # Join the corrected_words list back into a string with spaces between words
    corrected_text = " ".join(corrected_words)
    return corrected_text


def get_closest_match(word, word_list):
    """
    Finds the closest matching word in word_list based on Levenshtein distance.

    Args:
        word (str): The word to find closest match for.
        word_list (list): A list of words to search for a match.

    Returns:
        closest_match (str): The closest matching word in local_word_list.
    """
    import Levenshtein

    closest_match = min(word_list, key=lambda x: Levenshtein.distance(word, x))
    return closest_match


input_text = "Kathmandu plece"
local_words = ["beautiful", "place", "palace", "kathmandu", "welcome"]
corrected_text = correct_spelling(input_text, local_words)
print(corrected_text)