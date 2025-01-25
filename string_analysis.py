def analyze_string(input_string):
    vowels = "aeiouAEIOU"
    digits = "0123456789"
    
    vowel_count = 0
    consonant_count = 0
    digit_count = 0
    special_char_count = 0

    for char in string:
        if char.isdigit():
            digit_count += 1
        elif char.isalpha():  
            if char in vowels:
                vowel_count += 1
            else:
                consonant_count += 1
        elif char in digits:
            special_char_count += 1
        else:
            special_char_count += 1  

    reversed_string = string[::-1]
    
    print(f"Vowels: {vowel_count}")
    print(f"Consonants: {consonant_count}")
    print(f"Digits: {digit_count}")
    print(f"Special characters: {special_char_count}")
    print(f"Reversed string: {reversed_string}")

def main():
    analyze_string(string)

string = input("Enter a string: ")
main()
