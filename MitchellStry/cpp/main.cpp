#include <iostream>
#include <vector>
using namespace std;

void say_hello(){
	const int D=100;
	//const cannot be modified and will give an error if you try
	int A=1, B=2;
	int a=1;
	double b=1.0;
	float c=2.0;
	string d="Feliz Navidad!";
	std::cout<<"hello world\n"<<a<<" " <<b<< " "<<c<< " " <<d<<std::endl;
}
double add(double x, double y){
	return x+y;
}
void show_operators(){
	for(int i=0;i<10;i++){
		cout<<i<<endl;
	}
	int a=0;
	while(a++<10){
		//a++; counts to 10
		cout<<a<<endl;
		//a++; only counts to 9
	}
	cout<<"logical examples\n"<<endl;
	a=0;
	int b=1;
	if(a==0 && b==0){
		cout<<"Case 1\n"<<endl;
	}
	else{
		cout<<"Case 2\n"<<endl;
	}


	if(a==1 || b==1){
		cout<<"***Case 1\n"<<endl;
	}
	else{
		cout<<"***Case 2\n"<<endl;
	}

	int A=(a==0)? 5:-5;
	cout<<"A="<<A<<endl;
}
void incrementele(vector<double>& x, int i){
	        x[i]=100*i;
}
void showrefpointers(){
	int a=10;
	int* a_pt= &a;
	cout<<"a="<<a<<endl;
	cout<<"adress of a is"<<a_pt<<endl;
	cout<<"a again but dereferencing="<<*a_pt<<endl;
	//cout<<"value at an incremented ptr value="<<*(a_pt+100)<<endl;
	/*
	double A[5]={1000.0, 2.0, 3.4, 17.0, 5.0};
	double* A_pt;
	
	cout<<*A_pt<<endl;

	for(int i=0; i<10; i++){
		cout<<*(A_pt++)<<" "<<A[i]<<endl;
	
	}
	*/
	cout<<"STL Example\n"<<endl;
	vector<double> B(10,0.0);
	for(int i=0; i<10; i++){
		cout<<"i="<<i<<" "<<B[i]<<endl;
		incrementele(B,i);
		cout<<"after function call, i ="<<B[i]<<endl;
	}
}
class human{
	public:

	double height;
	int age;
	std::string name;
	human(std::string _name, int _age, double _height){ name=_name; age=_age; height=_height;}
	void say_hello(){ cout<<"my name is "<< name<<endl;}
};
int main(){
	//show_operators();
	//cout<<add(10,20)<<"\n";
	//say_hello();
	showrefpointers();
	human person1("Mitchell",23,181.0);
	person1.say_hello();
	cout<<"age is "<< person1.age<<" height is "<<person1.height<<endl;
	human* pers_pt=&person1;
	(*pers_pt).say_hello();
	pers_pt->say_hello();
	return 0;
}
/*
 *This is commented out.
 */
//this one line is commented out.

