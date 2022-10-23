//lib.cpp

#include "pch.h"
#include <iostream>
using namespace std;

#include "BookList.h"

int main(int argc, char* argv[]) {
    //--------------------------------------------------------------
    //  Creates a BookList object, adds several books to the list,
    //  then prints them.
    //--------------------------------------------------------------
    char list[LIST_LEN];
    BookList* books = new BookList();

    books->insert(new Book("F Title"));
    books->insert(new Book("D Title"));
    books->insert(new Book("G Title"));
    books->insert(new Book("A Title"));
    books->insert(new Book("E Title"));
    books->insert(new Book("H Title"));

    cout << "After inserts:\n";
    cout << books->getBookList(list, LIST_LEN) << endl;

    books->delet(new Book("A Title"));
    books->delet(new Book("H Title"));
    books->delet(new Book("G Title"));
    books->delet(new Book("E Title"));

    cout << "After deletes:\n";
    cout << books->getBookList(list, LIST_LEN) << endl;

    books->insert(new Book("A Title"));
    books->insert(new Book("E Title"));
    books->insert(new Book("H Title"));
    books->insert(new Book("G Title"));

    cout << "After 2nd inserts:\n";
    cout << books->getBookList(list, LIST_LEN) << endl;

    return 0;
}

