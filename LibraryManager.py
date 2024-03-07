# Initialize empty lists, sets , and dictionary
books_lists = []
authors_set = set()
books_dict = {}

#Add books
books_lists.append("Python Programming")
authors_set.add("Jhon Smith")
books_dict["Python Programming"] = "Jhon Smith"

books_lists.append("Data Structures and Algorithm")
authors_set.add("Jane Doe")
books_dict["Data Structures and Algorithm"] = "Jane Doe"

books_lists.append("Machine Leaarning Basics")
authors_set.add("Alice Jhonson")
books_dict["Machine Leaarning Basics"] = "Alice Jhonson"

#Search for books
search_title = input("Enter the title of the book: ")
if search_title in books_lists: 
    print(f"Book found! Author: {books_dict[search_title]}")
else:
    print("Book not found")

# Display of books
    print("Lists of books availabe: ")
    for book in books_lists:
        print(book)
# Remove a book
remove_title = input("Enter the title of the book to be removed: ")
if remove_title in books_lists: 
    remove_author= books_dict[remove_title]
    books_lists.remove(remove_title)
    authors_set.remove(remove_author)
    del books_dict[remove_title]
    print('Book removed succesfully!')
else:
    print('Book not found!')
