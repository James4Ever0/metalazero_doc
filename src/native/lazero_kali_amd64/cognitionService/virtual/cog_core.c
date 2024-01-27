#include <string.h>
#include <stdio.h>

int main(){
	char* a="abcdef";
	char* b="123";
	//char* b="abc";
	printf("%s\n",strstr(a,b));
}
