#include <iostream>

#define ll long long 

using namespace std;

int gcd(int a, int  b)
{
   if (b == 0)
      return a;
   return gcd(b, a%b);
}


int inverse(int a, int m)           // Inverse of a mod m
{
//   cout << "Entering inverse() " << a << m << endl;
   if (gcd(a,m) != 1)
      return -1;
   a = a%m;
   if (a == 1)
      return 1;
   return ( (1 - inverse(m,a)*m)/a ) % m;

}


int main()
{
   int a, b;
   cout << "First number: ";
   cin >> a;
   cout << "Second number: ";
   cin >> b;
   cout << gcd(a,b) << endl;
r//   cout << a%b << endl;
   cout << inverse(a,b) << endl;
   return 0;
}
