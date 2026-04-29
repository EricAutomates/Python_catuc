#include <iostream>
using namespace std;

void drawDiamond(int size)
{
    // upper part
    for (int i = 1; i <= size; i++)
    {
        for (int s = 0; s < size - i; s++)
            cout << " ";

        for (int j = 0; j < (2 * i - 1); j++)
            cout << "*";

        cout << endl;
    }

    // lower part
    for (int i = size - 1; i >= 1; i--)
    {
        for (int s = 0; s < size - i; s++)
            cout << " ";

        for (int j = 0; j < (2 * i - 1); j++)
            cout << "*";

        cout << endl;
    }
}

int main()
{
    int size;

    cout << "enter size: ";
    cin >> size;

    drawDiamond(size);

    return 0;
}

/* testing multi line comment. 

still got it.*/