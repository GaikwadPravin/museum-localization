#include<iostream>
#include<vector>
using namespace std;
  int reverse(int x)
  {
    vector<int> v;
    int i;
    while(x!=0)
    {
      v.push_back(x%10);
      x=x/10;
    }
    for(i=0;i<v.size();i++)
    {
      cout<<v[i];
    }

  }

   int main()
   {

     reverse(32);

   }
