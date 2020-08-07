#include <stdio.h>
#include <stdlib.h>

int points(char* games[], int len) 
{
	int count = 0;  
	int x, y;

	for(int i=0; i<len; i++)
  	{
		sscanf(games[i], "%d:%d", &x, &y);
		if(x>y) count += 3;
		if(x==y) count += 1;

//==================================================

     // int a = games[i][0] - '0';
     // int b = games[i][2] - '0';
     // count += (a>b)*3+(a==b); 

//==================================================

     // count += (games[i][0] > games[i][2]) ? 3
     //       : (games[i][0] == games[i][2]) ? 1
     //       : 0;
	} 
  
	return count;
}



int main(int argc, char const *argv[])
{
	char* arr1[] = {"1:2", "2:3", "0:0", "3:1"};
	int len = 4;
	int p = points(arr1, len);
	printf("%d\n", p);

	return 0;
}