from stats import counting_words,counting_characters,sorting_characters,check_arguments
import sys

def main():
    check_arguments(sys.argv)
    print("============ BOOKBOT ============")
    print(f"Analyzing book at {sys.argv[1]}...")
    counting_words(sys.argv[1])
    #counting_characters(FRANKENSTEIN_BOOK)
    sorting_characters(sys.argv[1])
    print("============= END ===============")
main()