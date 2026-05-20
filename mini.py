# Library Management System

library = {}

def add_book():
    book = input("Enter book name: ")
    library[book] = "Available"
    print("Book added successfully")

def display_books():
    if not library:
        print("No books available")
    else:
        print("\nLibrary Books:")
        for book, status in library.items():
            print(book, "-", status)

def issue_book():
    book = input("Enter book to issue: ")
    if book in library and library[book] == "Available":
        library[book] = "Issued"
        print("Book issued successfully")
        
    else:
        print("Book not available")

def return_book():
    book = input("Enter book to return: ")
    if book in library and library[book] == "Issued":
        library[book] = "Available"
        print("Book returned successfully")
    else:
        print("Invalid book name")

while True:
    print("\n1. Add Book")
    print("2. Display Books")
    print("3. Issue Book")
    print("4. Return Book")
    print("5. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        add_book()
    elif choice == 2:
        display_books()
    elif choice == 3:
        issue_book()
    elif choice == 4:
        return_book()
    elif choice == 5:
        print("Thank you")
        break
    else:
        print("Invalid choice")
        