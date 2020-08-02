#include <stdio.h>

int unusual_five()
{
	//printf("%d - %d\n", ('f'-0), ('a'-0));
	//printf("%d\n", ('f'%'a'));
	
	char ch[5];
	int i = sizeof(ch);
	printf("%d\n", i);
	return 0;
}

int main()
{
	unusual_five();
}