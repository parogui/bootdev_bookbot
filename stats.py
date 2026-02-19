def get_book_text(book):
    # Open the book and return it as a string if it does not exist, print the path
    try:
        with open(book) as f:
            book_content = f.read()
            return(book_content)
    except FileNotFoundError:
        print("--ERROR--")
        print(f"The file on the {book} path does not exist, exiting the program...")
        exit(1)


def counting_words(book):
    text=get_book_text(book).split(None,-1)
    words_count=len(text)
    print("----------- Word Count ----------")
    print(f'Found {words_count} total words')

def counting_characters(book):
    text=get_book_text(book)
    characters_dictionary = {}
    for character in text.lower():
        if character not in characters_dictionary:
            characters_dictionary[character] = 1
        else:
            characters_dictionary[character] += 1
    #print(characters_dictionary)
    return(characters_dictionary)
    
def sorting_characters(book):
    print("--------- Character Count -------")
    characters_dictionary = counting_characters(book)
    characters_dictionaries_list = []
    for character in characters_dictionary:
        #print(f'Character:{character} Occurrences: {characters_dictionary[character]}')
        current_character_dict = {
            "char": character,
            "num": characters_dictionary[character]
        }
        characters_dictionaries_list.append(current_character_dict)
    # After all characters were appended, sort them in reverse by the num count:
    sorted_list= sorted(characters_dictionaries_list, key=lambda x: x["num"],reverse=True)
    for character in sorted_list:
        print(f"{character["char"]}: {character["num"]}")

def check_arguments(arguments):
    if len(arguments) != 2:
        print(f"""The arguments used are {arguments}.
              Usage: python3 main.py <path_to_book>""")
        exit(1)