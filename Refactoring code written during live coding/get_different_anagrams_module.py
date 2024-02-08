def get_group_anagrams(words_list: list) -> dict:
    '''
    Groups words in a list based on their anagrams.

    Parameters:
    - words_list (list): A list of words to be grouped.

    Returns:
    dict: A dictionary where keys are sorted anagrams and values are lists of words with the same sorted anagram.
    '''
    anagram_group = {}

    for word in words_list:
        sorted_word = ''.join(sorted(word))
        anagram_group.setdefault(sorted_word, []).append(word)

    return anagram_group

words_list = ['aba', 'bac', 'abb', 'bab', 'bba', 'aab', 'abca']
print(get_group_anagrams(words_list))
