#include"stdio.h"
#include"string.h"

char arr[]="XCVBNM0123456789QWERTYUIOPASDFGHJKLZXCVBNM012345";
char flag[]="VV88AA225599OOKKQQSSGG88OOQQ88KK88KK22AABB550099BB99GGGG4488QQQQ99WW88QQ";

int main()
{
	printf("SparkCTF{");
	for(int i=0; i<strlen(flag);i+=2)
	{
		// Find the character in the array
		int ind;
		char ch;
		for(ind=6;ind<strlen(arr);ind++)
			if(arr[ind]==flag[i])break;
		
		printf("%c",arr[(ind-5)%strlen(arr)]);
	}
	printf("}");
	return 0;
}