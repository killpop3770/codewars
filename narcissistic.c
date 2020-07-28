#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdbool.h>

// A Narcissistic Number is a positive number which is 
//the sum of its own digits, each raised to the power of 
//the number of digits in a given base. In this Kata, we 
//will restrict ourselves to decimal (base 10).
// For example, take 153 (3 digits):
//     1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153

bool narcissistic(int num)
{
	int len = snprintf( NULL, 0, "%d", num );
	char str[len];
	sprintf(str, "%d", num);
	int cnt = 0;
	int temp = 0;

  	for (int i=0; i<len; i++)
  	{
  		temp = str[i]-48;
  		cnt += pow((double)temp, len);
  	}

  	if(num==cnt)
  	{
  		printf("%d == %d\n", num, cnt);
  		return true;
  	}
  	else
  	{
  		printf("%d != %d\n", num, cnt);
    	return false;
    }
}

int main()
{
	int num;
	scanf("%d", &num);
	printf(narcissistic(num) ? "true\n" : "false\n");
}

//high answer
// #include <stdbool.h>
// #include <math.h>

// bool narcissistic(int num)
// {
//     int p = log10(num) + 1;
//     int n = num;
//     do
//         num -= pow(n % 10, p);
//     while (n /= 10);
//     return !num;
// }