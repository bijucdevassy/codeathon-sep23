

def sort_string_by_frequency(input_string):
    # Create a dictionary to store the frequency of each character in the input string
    char_freq = {}
    for char in input_string:
        if char in char_freq:
            char_freq[char] += 1
        else:
            char_freq[char] = 1
    
    # Sort the characters in the input string by their frequency
    sorted_chars = sorted(char_freq, key=lambda x: char_freq[x], reverse=True)
    
    # Create the final string by concatenating the sorted characters
    final_string = ''
    for char in sorted_chars:
        final_string += char * char_freq[char]
    
    return final_string

print(sort_string_by_frequency("abc adfsdfsd"))

def test_sort_string_by_frequency():
    # Test case 1: Empty string
    assert sort_string_by_frequency("") == ""
    
    # Test case 2: String with one character
    assert sort_string_by_frequency("a") == "a"
    
    # Test case 3: String with repeated characters
    assert sort_string_by_frequency("aaabbbccc") == "aaabbbccc"
    
    # Test case 4: String with mixed characters
    assert sort_string_by_frequency("abcabcabc") == "aaabbbccc"
  

test_sort_string_by_frequency()
