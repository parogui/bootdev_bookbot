FRANKENSTEIN_BOOK="books/frankenstein.txt"

def get_book_text(book):
    with open(book) as f:
        book_content = f.read()
        return(book_content)

def counting_words():
    text=get_book_text(FRANKENSTEIN_BOOK).split(None,-1)
    words_count=len(text)
    print(f'Found {words_count} total words')

def main():
    counting_words()

main()