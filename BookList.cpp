//********************************************************************
//  BookList.h
//
//  Represents a collection of books.
//*******************************************************************
#include "pch.h"
#include "BookList.h"


void BookList::insert(Book * newBook) {

	BookNode * node = new BookNode(newBook);
	BookNode * current, * previous;

	if (head == NULL) head = node;
	else {
		if (node->book->compareTo(head->book->getBook()) <= 0) { // Sorts book for the first node
			BookNode * temp = head;
			head = node;
			head->next = temp;
			return;
		}

		previous = head;
		current = head->next;
		while (current != NULL) // Goes through the rest of the list and sorts books in alphabetical order
		{
			if (node->book->compareTo(current->book->getBook()) <= 0)
				break;

			previous = current;
			current = current->next;
		}

		previous->next = node;
		node->next = current;
	}
}


void BookList::delet(Book * newBook) 
{
	BookNode * current, * previous;

	if (head->book->compareTo(newBook->getBook()) == 0) // Checks if the first element needs to be deleted
		head = head->next;

	previous = head;
	current = head->next;
	while (current != NULL) // Runs through the list and checks whether they need to be removed
	{
		if (current->book->compareTo(newBook->getBook()) == 0) {
			previous->next = current->next; // When found the previous node will connect to the next node after current
			delete current; // This deletes node to prevent memory leak
			break;
		}
		previous = current;
		current = current->next;
	}
}

//----------------------------------------------------------------
//  Returns this list of books as a string.
//----------------------------------------------------------------
char* BookList::getBookList(char* list, size_t list_len) {

	list[0] = '\0';
	BookNode* current = head;

	while (current != NULL) {
		strcat_s(list, list_len, current->book->getBook());
		strcat_s(list, list_len, "\n");
		current = current->next;
	}

	return list;
}
