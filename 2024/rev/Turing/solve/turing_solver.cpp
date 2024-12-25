#include"stdio.h"
#include"string.h"

int main()
{
	char command[1024]="aaiasiasassaiaasaiaiaaasssiasisaasiasissaiaasaiasisaisaisaiiaasaiassissaiasiid";
	unsigned int arr[]={0x81,0x6a,0x7f,0x6b,0x78,0x75,0x6e,0x7a,0x67,0x5e,0x83,0x6a,0x67,0x70,0x61,0x6f,0x81,0x73,0x6f,0x77,0x74};
	int index=0;
	for(int count=0;count<strlen(command);count++)
	{
		switch(command[count])
		{
			case 'a':
				arr[index]-=5;
				break;
			case 's':
				arr[index]+=3;
				break;
			case 'x':
				arr[index]=arr[index]^arr[index-1];
				break;
			case 'i':
				index++;
				break;
			case 'd':
				for(int i=0;i<21;i++)
					printf("%c",arr[i]);				
		}
	}
}