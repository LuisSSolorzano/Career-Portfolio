#include <cstring>
#define TITLE_LEN 81

//********************************************************************
//  Book.cpp
//
//  Represents a single book.
//*******************************************************************

class Book {

public:
	Book(const char *newTitle) {
		strcpy_s(title, TITLE_LEN, newTitle);
	}

	char *getBook() {
		return title;
	}

	int compareTo(char* that_title) // compares strings to see which one is greater
	{
		size_t l1 = size(), l2 = size(that_title);
		size_t smallest = l1 >= l2 ? l2 : l1;

		for (size_t i = 0; i < smallest; ++i)
			if (title[i] > that_title[i]) return 1;
			else if (title[i] < that_title[i]) return -1;

		return l1 - l2;
	}


	static size_t size(char * s)
	{
		size_t size;
		for (size = 0; s[size] != '\0'; size++);
		return size;
	}

	size_t size()
	{
		return size(title);
	}



private:
	char title[TITLE_LEN];
};
