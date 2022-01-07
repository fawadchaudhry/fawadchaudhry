#include <stdio.h>
#include <stdlib.h>
void Chart(char gameboard[11][11], int begin){
	//Begin using 0
  if(begin==0){
	for(int i=0;i<11;i++){
		printf("\n");
		for(int j=0; j<11;j++){
			printf("%*c ",2 ,gameboard[i][j]);
		}
	}
} 

	//Begin using 1
  if(begin==1){
	for(int i=0;i<11;i++){
		printf("\n");
		for(int j=0; j<11;j++){
			if(gameboard[i][j]=='S'){
				printf("%*c ",2 ,'O');
			}else{
			printf("%*c ",2 ,gameboard[i][j]);
			}
		}
	}
	}
	printf("\n");
}
//Start gameboard
int Move(char gameboard[11][11],int begin, int left){
  char show;
  int verify;
  int y;
  int x=-1;
	Chart(gameboard,begin);
	do{
		printf("Be sure to select a differnt spot\n");
		verify=0;
		y,x=-1;
		while(verify!=1 || y<0 ||y>9){
			printf("Please enter depth location\n");
			verify=scanf("%d",&y);
			getchar();
		}

		verify=0;

		while(verify!=1 || x<0 ||x>9){
			printf("Please enter width location\n");
			verify=scanf("%d",&x);
			getchar();
		}
		x++;
		y++;

	}while(gameboard[y][x]=='X' || gameboard[y][x]=='H');

	if(gameboard[y][x]=='S'){
		printf("Hit!\n");
		gameboard[y][x]='H';
		printf("The opponent lost a piece!");
	}else{
		printf("Miss!\n");
		gameboard[y][x]='X';
		printf("The opponent has the same amount of pieces");
	}
	printf("Press any key to proceed\n");
	scanf("%c",&show);
	return left;
}
//First Ship
void Shipfive(char gameboard[11][11]){
  int up,down,left,right;
  int x, y,verify,input=-1;
  int checker;
	printf("Please enter depth location of the 5x1 ship\n");

	while(verify!=1 || y<0 ||y>9){
		verify=scanf("%d",&y);
		getchar();
	}
	verify=0;
	printf("Please enter width location of the 5x1 ship\n");

	while(verify!=1 || x<0 ||x>9){
		verify=scanf("%d",&x);
		getchar();
	}
	x++;
	y++;

	do{
		verify=0;
		checker=0;
		up,down,left,right=0;

		printf("Which orientation? (Please select the corresponding number)\n");	

		if((y-4)>0){
			printf("%d. Up\n",++checker);
			up=checker;
		}
		if((y+4)<10){
			printf("%d. Down\n",++checker);
			down=checker;
		}
		if((x-4)>0){
			printf("%d. Left\n",++checker);
			left=checker;
		}
		if((x+4)<10){
			printf("%d. Right\n",++checker);
			right=checker;
		}

		verify=scanf("%d",&input);
		getchar();

	}while(verify!=1 || input>checker ||input <=0);

	if(input==up){
	
		for(int i=0;i<5;i++){
			gameboard[y-i][x]='S';
		}

	}else if(input==down){
	
		for(int i=0;i<5;i++){
			gameboard[y+i][x]='S';
		}

	}else if(input==left){
	
		for(int i=0;i<5;i++){
			gameboard[y][x-i]='S';
		}

	}else if(input==right){
	
		for(int i=0;i<5;i++){
			gameboard[y][x+i]='S';
		}

	}

}
//Second Ship
void Shipthree(char gameboard[11][11]){
  int up,down,left,right;
  int x, y,verify,input=-1;
  int checker;
	
	do{
		verify=-1;
		printf("Please enter depth location of the 3x1 ship. Ships cannot overlap\n");

		while(verify!=1 || y<0 ||y>9){
			verify=scanf("%d",&y);
			getchar();
		}

		verify=0;

		printf("Please enter width location of the 3x1 ship. Ships cannot overlap\n");
	
		while(verify!=1 || x<0 ||x>9){
			verify=scanf("%d",&x);
			getchar();
		}
		x++;
		y++;
	}while(gameboard[y][x]=='S');
	do{
	
		verify=0;
		checker=0;
		up,down,left,right=0;
		printf("Which orientation? (Please select the corresponding number)\n");	
	
		for(int i=1;i<3;i++){
			if(gameboard[y-i][x]=='S' || (y-2)<1){
				up=0;
				break;
			}else if(i==2){
				printf("%d. Up\n",++checker);
				up=checker;
			}
		}
		for(int i=1;i<3;i++){
			if(gameboard[y+i][x]=='S' || (y+2)>10){
				down=0;
				break;
			}else if(i==2){
				printf("%d. Down\n",++checker);
				down=checker;
			}
		}

		for(int i=1;i<3;i++){
			if(gameboard[y][x-i]=='S' || (x-2)<1){
				left=0;
				break;
			}else if(i==2){
				printf("%d. Left\n",++checker);
				left=checker;
			}
		}

		for(int i=1;i<3;i++){
			if(gameboard[y][x+i]=='S' || (x+2)>10){
				right=0;
				break;
			}else if(i==2){
				printf("%d. Right\n",++checker);
				right=checker;
			}
		}

		verify=scanf("%d",&input);
		getchar();

	}while(verify!=1 || input>checker ||input <=0);

	if(input==up){
	
		for(int i=0;i<3;i++){
			gameboard[y-i][x]='S';
		}

	}else if(input==down){
	
		for(int i=0;i<3;i++){
			gameboard[y+i][x]='S';
		}

	}else if(input==left){
	
		for(int i=0;i<3;i++){
			gameboard[y][x-i]='S';
		}

	}else if(input==right){
	
		for(int i=0;i<3;i++){
			gameboard[y][x+i]='S';
		}

	}

}
// Third Ship
void Shipfour(char gameboard[11][11]){
  int up,down,left,right;
  int x, y,verify,input=-1;
  int checker;
	do{
		do{
		verify=-1;
		y,x,input=-1;
		printf("Please enter depth location of the 4x1 ship. Ships cannot overlap\n");

		while(verify!=1 || y<0 ||y>9){
			verify=scanf("%d",&y);
			getchar();
		}
		verify=0;

		printf("Please enter width location of the 4x1 ship. Ships cannot overlap\n");

		while(verify!=1 || x<0 ||x>9){
			verify=scanf("%d",&x);
			getchar();
		}
		x++;
		y++;

		}while(gameboard[y][x]=='S');
		verify=0;
		checker=0;
		up,down,left,right=0;

		printf("Which orientation? (Please select the corresponding number)\n");	

	for(int i=1;i<4;i++){
			if(gameboard[y-i][x]=='S' || (y-3)<1){
			up=0;
			break;
			}else if(i==3){
			printf("%d. Up\n",++checker);
			up=checker;
			}
	
		}

	for(int i=1;i<4;i++){
			if(gameboard[y+i][x]=='S' || (y+3)>10){
			down=0;
			break;
			}else if(i==3){
			printf("%d. Down\n",++checker);
			down=checker;
			}
	
		}

	for(int i=1;i<4;i++){
			if(gameboard[y][x-i]=='S' || (x-3)<1){
			left=0;
			break;
			}else if(i==3){
			printf("%d. Left\n",++checker);
			left=checker;
			}
	
		}

	for(int i=1;i<4;i++){
		if(gameboard[y][x+i]=='S' || (x+3)>10){
			right=0;
			break;
			}else if(i==3){
			printf("%d. Right\n",++checker);
			right=checker;
			}
		}
		if(checker==0){
			printf("Pick a different coordinate\n");
		}else{
			verify=scanf("%d",&input);
			getchar();
		}

		}while(verify!=1 || input>checker ||input <=0 ||checker==0);
		}

		
void main(){
  char gameboard1[11][11];
  char gameboard2[11][11];
  int begin=0;
  int player1life=12;
  int player2life=12;
  	//Player One's gameboard
	gameboard1[0][0]=' ',gameboard1[0][1]='0',gameboard1[0][2]='1',gameboard1[0][3]='2',gameboard1[0][4]='3',gameboard1[0][5]='4',gameboard1[0][6]='5',gameboard1[0][7]='6',gameboard1[0][8]='7',gameboard1[0][9]='8',gameboard1[0][10]='9';
	gameboard1[1][0]='0',gameboard1[2][0]='1',gameboard1[3][0]='2',gameboard1[4][0]='3',gameboard1[5][0]='4',gameboard1[6][0]='5',gameboard1[7][0]='6',gameboard1[8][0]='7',gameboard1[9][0]='8',gameboard1[10][0]='9';

	//Player Two's gameboard
	gameboard2[0][0]=' ',gameboard2[0][1]='0',gameboard2[0][2]='1',gameboard2[0][3]='2',gameboard2[0][4]='3',gameboard2[0][5]='4',gameboard2[0][6]='5',gameboard2[0][7]='6',gameboard2[0][8]='7',gameboard2[0][9]='8',gameboard2[0][10]='9';
	gameboard2[1][0]='0',gameboard2[2][0]='1',gameboard2[3][0]='2',gameboard2[4][0]='3',gameboard2[5][0]='4',gameboard2[6][0]='5',gameboard2[7][0]='6',gameboard2[8][0]='7',gameboard2[9][0]='8',gameboard2[10][0]='9';

	for(int i=1;i<11;i++){
		for(int j=1; j<11;j++){
			gameboard1[i][j]='O';
			gameboard2[i][j]='O';
		}
	}
  printf("Battleships!\n");
  Chart(gameboard1,begin);
  printf("Player 1 turn\n");
  Shipfive(gameboard1);
  Chart(gameboard1,begin);
  Shipthree(gameboard1);
  Chart(gameboard1,begin);
  Shipfour(gameboard1);
  Chart(gameboard1,begin);
  system("clear");
  printf("Player 2 turn\n");
  Chart(gameboard2,begin);
  Shipfive(gameboard2);
  Chart(gameboard2,begin);
  Shipthree(gameboard2);
  Chart(gameboard2,begin);
  Shipfour(gameboard2);
	//Clear the terminal after turn changes or game ends
system("clear");
	printf("Player 1 starts\n");
	begin=1;
	do{

	printf("Player 1's turn\n");

	player2life=Move(gameboard2,begin,player2life);
	//Clear Terminal for Player 2
	system("clear");		

	if(player2life==0){
		printf("Player 1 wins!\n");
		break;
	}

	printf("Player 2's turn.\n");
	player1life=Move(gameboard1,begin,player1life);
	system("clear");

		if(player1life==0){
			printf("Player 2 wins!\n");
			break;
		}
	}while(1);
} //The end