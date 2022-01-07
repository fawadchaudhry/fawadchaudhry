#include <stdio.h>

	struct student {
	char firstname[20];
	char lastname[20];
	unsigned int studentNumber;
	char program[30];
	float twelvegpa;

	};
	
void main(){
	struct student student1;
	struct student *studentPtr=&student1;
	printf("Please enter the first name\n");
	scanf("%s",studentPtr ->firstname);
	getchar();

	printf("Please enter the last name\n");
	scanf("%s",studentPtr ->lastname);
	getchar();

	printf("Please enter the student number\n");
	scanf("%u",&(*studentPtr).studentNumber);
	getchar();

	printf("Please enter the program\n");
	scanf("%s",studentPtr -> program);
	getchar();
	
	printf("Please enter the GPA\n");
	scanf("%f",&(*studentPtr).twelvegpa);
	getchar();
	
	void  Print(struct  student  *studentPtr){  
  	printf("First  Name:  %s\n",studentPtr->firstname);  
  	printf("Last  Name:  %s\n",studentPtr->lastname);  
  	printf("Student  Number:  %u\n",studentPtr->studentNumber);
 	printf("Program:  %s\n",studentPtr->program);  
  	printf("GPA  on  12  point  scale:  %.2f\n",studentPtr->twelvegpa);  
	}  
	
	float twelvegpa = studentPtr -> twelvegpa;
	float fourgpa;
	
	if(twelvegpa<12.01 && twelvegpa>10.89){

fourgpa=4.0;

}else if(twelvegpa<10.89 && twelvegpa>10.59){

fourgpa=3.9;

}else if(twelvegpa<10.59 && twelvegpa>10.29){

fourgpa=3.8;

}else if(twelvegpa<10.29 && twelvegpa>9.99){

fourgpa=3.7;

}else if(twelvegpa<9.99 && twelvegpa>9.69){

fourgpa=3.6;

}else if(twelvegpa<9.69 && twelvegpa>9.39){

fourgpa=3.5;

}else if(twelvegpa<9.38 && twelvegpa>9.09){

fourgpa=3.4;

}else if(twelvegpa<9.09 &&twelvegpa>8.79){

fourgpa=3.3;

}else if(twelvegpa<8.79 &&twelvegpa>8.49){

fourgpa=3.2;

}else if(twelvegpa<8.49 &&twelvegpa>8.19){

fourgpa=3.1;

}else if(twelvegpa<8.19 &&twelvegpa>7.89){

fourgpa=3.0;

}else if(twelvegpa<7.89 &&twelvegpa>=7.59){

fourgpa=2.9;

}else if(twelvegpa<7.59 &&twelvegpa>7.29){

fourgpa=2.8;

}else if(twelvegpa<7.29 &&twelvegpa>6.99){

fourgpa=2.7;

}else if(twelvegpa<6.99 &&twelvegpa>6.69){

fourgpa=2.6;

}else if(twelvegpa<6.69 &&twelvegpa>6.39){

fourgpa=2.5;

}else if(twelvegpa<6.39 &&twelvegpa>6.09){

fourgpa=2.4;

}else if(twelvegpa<6.09 &&twelvegpa>5.79){

fourgpa=2.3;

}else if(twelvegpa<5.79 &&twelvegpa>5.49){

fourgpa=2.2;

}else if(twelvegpa<5.49 &&twelvegpa>5.19){

fourgpa=2.1;

}else if(twelvegpa<5.19 &&twelvegpa>4.89){

fourgpa=2.0;

}else if(twelvegpa<4.89 &&twelvegpa>4.59){

fourgpa=1.9;

}else if(twelvegpa<4.59 &&twelvegpa>4.29){

fourgpa=1.8;

}else if(twelvegpa<4.29 &&twelvegpa>3.99){

fourgpa=1.7;

}else if(twelvegpa<3.99 &&twelvegpa>3.69){

fourgpa=1.6;

}else if(twelvegpa<3.69 &&twelvegpa>3.39){

fourgpa=1.5;

}else if(twelvegpa<3.39 &&twelvegpa>3.09){

fourgpa=1.4;

}else if(twelvegpa<3.09 &&twelvegpa>2.79){

fourgpa=1.3;

}else if(twelvegpa<2.79 &&twelvegpa>2.49){

fourgpa=1.2;

}else if(twelvegpa<2.49 &&twelvegpa>2.19){

fourgpa=1.1;

}else if(twelvegpa<2.19 &&twelvegpa>1.79){

fourgpa=1.0;

}else if(twelvegpa<1.79 &&twelvegpa>1.59){

fourgpa=0.9;

}else if(twelvegpa<1.59 &&twelvegpa>1.29){

fourgpa=0.8;

}else if(twelvegpa<1.29 &&twelvegpa>0.99){

fourgpa=0.7;

}else if(twelvegpa<0.99 &&twelvegpa>0.89){

fourgpa=0.6;

}else if(twelvegpa<0.89 &&twelvegpa>0.69){

fourgpa=0.5;

}else if(twelvegpa<0.69 &&twelvegpa>0.59){

fourgpa=0.4;

}else if(twelvegpa<0.59 &&twelvegpa>0.39){

fourgpa=0.3;

}else if(twelvegpa<0.39 &&twelvegpa>0.29){

fourgpa=0.2;

}else if(twelvegpa<0.29 &&twelvegpa>0.09){

fourgpa=0.1;

}else if(twelvegpa>-0.01){

fourgpa=0;

}

	Print(studentPtr);
	printf("The 4-point GPA of %s %s is %f",studentPtr ->firstname,studentPtr ->lastname,fourgpa);
}