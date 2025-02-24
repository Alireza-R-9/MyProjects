#include <iostream>
#include <fstream>
using namespace std;

struct Book {
    string title;
    string author;
    int publicationYear{};
    string isbn;
};


void addBook(const Book& book) {
    ofstream file("library.txt", ios::app);
    file << book.title << ',' << book.author << ',' << book.publicationYear << ',' << book.isbn << endl;
    file.close();
}


void displayAllBooks() {
    ifstream file("library.txt");
    string line;

    cout << "All Books:\n";
    while (getline(file, line)) {
        cout << line << endl;
    }

    file.close();
}


void searchBook(const string& searchKey) {
    ifstream file("library.txt");
    string line;
    bool found = false;

    cout << "Search Results:\n";
    while (getline(file, line)) {
        size_t pos = line.find(searchKey);
        if (pos != string::npos) {
            cout << line << endl;
            found = true;
        }
    }

    if (!found) {
        cout << "No matching books found.\n";
    }

    file.close();
}


void deleteBook(const string& isbn) {
    ifstream inFile("library.txt");
    ofstream outFile("temp.txt");
    string line;

    bool found = false;

    while (getline(inFile, line)) {
        size_t pos = line.find(isbn);
        if (pos == string::npos) {
            outFile << line << endl;
        } else {
            found = true;
        }
    }

    inFile.close();
    outFile.close();

    remove("library.txt");
    rename("temp.txt", "library.txt");

    if (found) {
        cout << "Book with ISBN " << isbn << " deleted successfully.\n";
    } else {
        cout << "Book with ISBN " << isbn << " not found.\n";
    }
}

int main() {
    int choice;

    do {
        cout << "\nLibrary Management System\n";
        cout << "1. Add a new book\n";
        cout << "2. Display all books\n";
        cout << "3. Search for a book\n";
        cout << "4. Delete a book\n";
        cout << "5. Quit\n";
        cout << "Enter your choice: ";
        cin >> choice;

        switch (choice) {
            case 1: {
                Book newBook;
                cout << "Enter book title: ";
                cin.ignore();
                getline(cin, newBook.title);
                cout << "Enter author name: ";
                getline(cin, newBook.author);
                cout << "Enter publication year: ";
                cin >> newBook.publicationYear;
                cout << "Enter ISBN: ";
                cin >> newBook.isbn;

                addBook(newBook);
                break;
            }
            case 2:
                displayAllBooks();
                break;
            case 3: {
                string searchKey;
                cout << "Enter ISBN or title to search: ";
                cin.ignore();
                getline(cin, searchKey);
                searchBook(searchKey);
                break;
            }
            case 4: {
                string isbn;
                cout << "Enter ISBN to delete: ";
                cin >> isbn;
                deleteBook(isbn);
                break;
            }
            case 5:
                cout << "Goodbye!\n";
                break;
            default:
                cout << "Invalid choice. Please try again.\n";
        }
    } while (choice != 5);

    return 0;
}