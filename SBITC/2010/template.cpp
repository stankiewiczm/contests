#include <iostream>
using namespace std;

int i, n[20];

int main()
{
  i = 0;
  while (i < 20)
  {
		cin >> n[i];
		i++;
	};
  for (i = 0; i < 20; i++)
    cout << n[i] << " ";
  cout << endl;
}

