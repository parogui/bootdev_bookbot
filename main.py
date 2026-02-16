def get_book_text(book):
    with open(book) as f:
        book_content = f.read()
        return(book_content)
    

def main():
    print(get_book_text("books/frankenstein.txt"))

main()