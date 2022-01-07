#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>
#include <math.h>
#include <string.h>

int main() {
	char password[20]; 
	int checkUpper=0;
	int checkNumber=0;
	int checkSpecial=0;
	printf("Enter a password (up to twenty characters) including:\n\t At Least one uppercase\n\t At least one number\n\t At least one special character:\n");
	scanf(" %s", password);
	for(int i=0;i<=19;i++){

		if(isupper(password[i])) {

		checkUpper++;

		}

		if(isdigit(password[i]) ) {
		
		checkNumber++;
		
		}

		if(ispunct(password[i]) ) {
		
		checkSpecial++;
		
		}
	}
	if(checkUpper>=1 && checkNumber>=1 && checkSpecial>=1){

		printf("Your password is %s\n", password);

	} else {

		printf("Invalid password\n");
	}
}