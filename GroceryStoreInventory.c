#include <stdio.h>

typedef struct Food_Groceries{	//struct for name, quantity, and price

	char itemName[25];
	int itemQuantity;
	float itemPrice;

}Grocery;




void additem(Grocery *pointer){		//additem function

	printf("Please enter the item's name\n");
	scanf("%s",pointer-> itemName);

	printf("Please enter the item's quantity\n");
	scanf("%d",&(*pointer).itemQuantity);

	printf("Please enter the item's price\n");
	scanf("%f",&(*pointer).itemPrice);

}




void editquantity(int number, Grocery items[number]){	//editquantity function

	if(number==0){

		printf("No items in department\n");

	}
	
	int i=0;
	int verify;
	int option;

	while(i<number)
	{
	printf("%d. %s\n",i+1,items[i].itemName);
	i+= 1;

	}

	while(verify==0 ||option>number||option<1)
	{

			printf("Invalid Entry. Try again\n");
			verify=scanf("%d",&option);
			getchar();

	}

	verify = 0;

	int newQuantity = 0;

	while(verify==0 ||newQuantity<0)
	{

			printf("What is the item's quantity?\n");
			verify=scanf("%d",&newQuantity);
			getchar();

	}

	items[option-1].itemQuantity=newQuantity;

}




void editcost(int number, Grocery items[number]){	//editcost function
	
	if(number==0){
		printf("No items in department\n\n");
	}

	int i=0;
	int option;
	int verify=0;
	float newCost=0;

	while(i<number)
	{

	printf("%d. %s\n",i+1,items[i].itemName);

	i+=1;

	}

	while(verify==0 ||option>number||option<1)
	{

			printf("Invalid entry. Try again\n\n");
			verify=scanf("%d",&option);
			getchar();

	}

	verify = 0;

	while(verify==0 ||newCost<0)
	{

			printf("What is the item's cost?\n");
			verify=scanf("%f",&newCost);
			getchar();

	}

	items[option-1].itemPrice=newCost;

}


void main(){	//main function

	Grocery Produce[100];

	Grocery Deli[100];

	Grocery Bakery[100];

	Grocery Frozen[100];

	int option=0;

	int produceNum;
	int deliNum;
	int bakeryNum;
	int frozenNum=0;

	do{

	int verify,option=0;

	printf("Main Menu: \n");
								//main menu
	printf("1. Add an item to inventory\n");
	printf("2. Change the quantity of an item in inventory\n");
	printf("3. Change the cost of an item in inventory\n");
	printf("4. Output inventory to file\n");
	printf("5. Exit program\n");

	while(verify==0 ||option>5||option<1){
	printf("Enter the number corresponding to the menu option\n");
	verify=scanf("%d",&option);
	getchar();
	}

	verify=0;

	if(option==1){

		printf("1. Add item to produce inventory\n");		//submenu
		printf("2. Add item to deli inventory\n");
		printf("3. Add item to bakery inventory\n");
		printf("4. Add item to frozen food inventory\n");
		while(verify==0 ||option>4||option<1){
			printf("Invalid entry. Try again\n");
			verify=scanf("%d",&option);
			getchar();
		}

		if(option==1){
			additem(&(Produce[produceNum]));
			produceNum++;
		}else if(option==2){
			additem(&(Deli[deliNum]));
			deliNum++;
		}else if(option==3){
			additem(&(Bakery[bakeryNum]));
			bakeryNum++;
		}else{
			additem(&(Frozen[frozenNum]));
			frozenNum++;
		}

	}else if(option==2){

		printf("1. Change the quantity of an item in the produce inventory\n");		//submenu
		printf("2. Change the quantity of an item in the deli inventory\n");
		printf("3. Change the quantity of an item in the bakery inventory\n");
		printf("4. Change the quantity of an item in the frozen food inventory\n");

		while(verify==0 ||option>4||option<1){

			printf("Invalid entry. Try again\n");
			verify=scanf("%d",&option);
			getchar();
		}
	
		if(option==1){
			editquantity(produceNum,Produce);
		}else if(option==2){
			editquantity(deliNum,Deli);
		}else if(option==3){
			editquantity(bakeryNum,Bakery);
		}else{
			editquantity(frozenNum,Frozen);
		}

	}else if(option==3){

		printf("1. Change the cost of an item in the produce inventory\n");		//submenu
		printf("2. Change the cost of an item in the deli inventory\n");
		printf("3. Change the cost of an item in the bakery inventory\n");
		printf("4. Change the cost of an item in the frozen food inventory\n");

		while(verify==0 ||option>4||option<1){

			printf("Invalid entry. Try again\n");
			verify=scanf("%d",&option);
			getchar();
		}
	
		if(option==1){

			editcost(produceNum,Produce);

		}else if(option==2){

			editcost(deliNum,Deli);

		}else if(option==3){

			editcost(bakeryNum,Bakery);

		}else{

			editcost(frozenNum,Frozen);
		}

		}else if(option==4){

			FILE *store;					//storage file
			store = fopen("GroceryDepartments.txt","w+");
		
			fprintf(store,"%s\n","Produce Department");

			for(int i=0;i<produceNum;i++){

				fprintf(store,"%s, ",Produce[i].itemName);
				fprintf(store,"%d, $%.2f\n",Produce[i].itemQuantity,Produce[i].itemPrice);
			}

			fprintf(store,"\n%s\n","Deli Department");

			for(int i=0;i<deliNum;i++){

				fprintf(store,"%s, ",Deli[i].itemName);
				fprintf(store,"%d, $%.2f\n",Deli[i].itemQuantity,Deli[i].itemPrice);
			}

			fprintf(store,"\n%s\n","Bakery Department");

			for(int i=0;i<bakeryNum;i++){

				fprintf(store,"%s, ",Bakery[i].itemName);
				fprintf(store,"%d, $%.2f\n",Bakery[i].itemQuantity,Bakery[i].itemPrice);
			}
		
			fprintf(store,"\n%s\n","Frozen Department");

			for(int i=0;i<frozenNum;i++){

				fprintf(store,"%s, ",Frozen[i].itemName);
				fprintf(store,"%d, $%.2f\n",Frozen[i].itemQuantity,Frozen[i].itemPrice);
			}

			fclose(store);

			printf("Inventory\n");

		}else{
			option=5;
                        break;
		}

	}while(option!=5);

}	//end