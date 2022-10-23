
#include <iostream>
#include <cctype>

using namespace std;

int main()
{
    int count = 1;
    int index, size;
   
    const int ALPHABET_SIZE = 26;
    // Two arrays will be parallel
    char letters[ALPHABET_SIZE] = {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
                                   'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'};
    int freq[ALPHABET_SIZE] = { 0 };

    const int STR_LEN = 80;
    char string[STR_LEN];

    cout << "Enter a sentence." << endl;
    cin.getline(string, STR_LEN);

    size = strlen(string);
    for (int i = 0; i < size; i++) 
    {
        if (string[i] != ' ' && string[i] != ',' && string[i] != '.') // Checks if char is punctuation or space if not
        {
            index = toupper(string[i]) - 65; // 65 is 'A' in ASCII // It will be assigned to index as the  index of letters
            freq[index]++;
        }
        else if (string[i] == ' ') { // Counts number of words
            count++;
        }
    }
    cout << count << " words" << endl;

    for (int j = 0; j < ALPHABET_SIZE; j++) // For loop will print the instances of the letter and the letter if the instances is not 0
    {
        if (freq[j] != 0)
            cout << freq[j] << ' ' << letters[j] << endl;
    }

    return 0;
}
/*
Enter a sentence.
I say Hi.
3 words
1 a
1 h
2 i
1 s
1 y

C:\Users\luiss\source\repos\Project_2\Debug\Project_2.exe (process 4524) exited with code 0.
To automatically close the console when debugging stops, enable Tools->Options->Debugging->Automatically close the console when debugging stops.
Press any key to close this window . . .

*/