#include<iostream>
#include<cstring>//this is for getline
#include<cstdlib>			// rand()
#include<conio.h>//this is for system cls
using namespace std;
int inputuser();
int winner(string,string);
void displayrules();
int main()
{
cout<<"**Rock, Scissor ,Paper Game**"<<endl<<endl;
string name;
cout<<"Enter your name:";
//getline(cin,name);we can use both
cin>>name;
cout<<endl;
char input;
int score=0;
do
{
//	system("cls");it is optional
	displayrules();
	score=score+inputuser();
	cout<<endl<<endl<<"Would you like to play again press any key without n/N and press it to exit ";
    cin>>input;
	cout<<endl;	
}while(input!='n'&&input!='N');
cout<<name<<": your score is "<<score<<endl;
cout<<"*********"<<endl;
}

int inputuser()
{
	int input;
	string userinput;
cout<<"1. Rock"<<endl;
cout<<"2. Paper"<<endl;
cout<<"3. Scissor"<<endl;
label1:
cout<<"Enter your input:";
cin>>input;
cout<<endl;	
switch(input){
	case 1: userinput="Rock";
	break;
	case 2: userinput="Paper";
	break;
	case 3: userinput="Scissor";
	break;
	default: {
	cout<<"invalid option";
	goto label1; }
	
}

int computerinput=rand()%3 + 1;	
string cinput;

switch(computerinput){
	case 1: cinput="Rock";
	break;
	case 2: cinput="paper";
	break;
	case 3: cinput="Scissor";
	break;
	
}
cout<<"Computer choose:"<<cinput<<endl;
int output=winner(userinput,cinput);
switch(output){
	case 1:{cout<<"you win"; return 1;
		break;
	}
		case 0:{cout<<"computer win"; return 0;
		break;
	}
		case -1:{cout<<"match draw"; return 0;
		break;
	}
}
}
int winner(string userinput,string cinput)
{
	if(cinput=="Rock")
	{
		
		if(userinput=="Rock")
		{
			return -1;
		}
		else if(userinput=="Scissor")
		{
			return  0;
		}
		else if(userinput=="Paper")
		{
			return 1;
		}
	}
	if(cinput=="Scissor")
	{
		if(userinput=="Rock")
		{
			return 1;
		}
		else if(userinput=="Scissor")
		{
			return  -1;
		}
		else if(userinput=="Paper")
		{
			return 0;
		}
	}
	if(cinput=="Paper")
	{
		if(userinput=="Rock")
		{
			return 0;
		}
		else if(userinput=="Scissor")
		{
			return  1;
		}
		else if(userinput=="Paper")
		{
			return -1;
		}
	}
}
void displayrules()
{
	cout<<endl<<endl<<endl;
	cout<<"\t Game rules : "<<endl;
	cout<<"\t =Rock crushes the scissor"<<endl;
	cout<<"\t =Scissor cuts the paper"<<endl;
	cout<<"\t =Paper covers the rock"<<endl;
}