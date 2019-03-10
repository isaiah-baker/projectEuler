#include <iostream>

using namespace std;

int main()
{
	cout << "factor this: ";
	long num;
	cin >> num;
	int large=0;
	
/* */

	for( int i=2; num!=1; ++i)
	{
		while( num%i==0)
		{
			num/=i;
			large=i;
		}
		cout << "i is: " << i << endl << "num is: " << num << endl;
	}	
	
	cout<<"The required number is: "<< large << endl << endl;
	
	return 0;
}