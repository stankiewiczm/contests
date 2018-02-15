#include<iostream>
#include<stdio.h>

using namespace std;

int main()
{
   int a[10];
   int i, l, u, n, m, key;
   bool finished = false;
   
   printf("Enter the size of an array: ");
   scanf("%d",&n);

   printf("Enter the elements in ascending order: ");
   for(i=0;i<n;i++)
      scanf("%d",&a[i]);

   printf("Enter the number to be search: ");
   scanf("%d",&key);  
   
   l = 0;      u = n-1;
   finished = ((a[l] == key) || (a[u] == key));
   
   while ((l <= u) && (not finished))
   {
      m = (l+u)/2;

//      printf("%i %i %i \n", l, u, m);
//      printf("%i %i %i \n", a[l], a[u], a[m]);

      if (a[m] < key)      // Look in the top half
         l = m+1;
      if (a[m] > key)      // Look in bottom half
         u = m-1;
      finished = (a[m] == key);

//      cout << m << a[m] << key << finished << endl << endl;
   };
   
   if (finished)
      printf("Element found\n");
   else
      printf("/me sad\n");
   return 0;
}
      
