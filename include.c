#include <stdbool.h>
#include <stdio.h>

bool include(const int* arr, size_t size, int item)
{
	for(int i=0; i<size; i++)
	{
		if(item == arr[i]) return true;
	}

    return false;
}

int main()
{
	const int arr[] = {0, 1, 2, 3, 5, 8, 13, 2, 2, 2, 11};
	int num;
	int len = sizeof(arr)/sizeof(int);
	scanf("%d", &num);

	printf(include(arr, len, num) ? "true\n" : "false\n");

	return 0;
}

