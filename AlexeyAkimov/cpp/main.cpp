#include <iostream>
#include <vector>
using namespace std;



void say_hello(){

  int D = 100;
 
  D = 200;

  int A = 1, B = 2;
//  int A = 1; int B = 2; 
  long long int a = 1; 
  double b = 1.0;
  float c = 2.0;
  std::string d = "Feliz Navidad!";


  std::cout<<"Hello World\n"<<a<<" "<<b<<" "<<c<<" "<<d<<std::endl<<A<<endl<<B;

}

double add(double x, double y){
                                          return x + y; 
}


void show_operators(){

  cout<<"For loop example\n";
  for(int i=0; i<10; i++){
    cout<<i<<" "<<i%3<<endl;
  }


  cout<<"while loop example\n";
  int a = 0;
  while(a<10){
   
    a++;
    cout<<a<<endl;
    //a++;
  }

  cout<<"Logical examples\n";

  a = 0; 
  int b = 1;
 
  if( a==0 && b==0 ){
    cout<<"Case 1\n";
  }
  else{
    cout<<"Case 2\n";
  } 


  if( a==1 || b==1 ){
    cout<<"***Case 1\n";
  }
  else{
    cout<<"***Case 2\n";
  } 


  int A = (a==0)? 5 : -5;

  cout<<"A = "<<A<<endl;


}


void increment_element(vector<double>& x, int i){

  x[i] = 100*i;

}



void show_references_and_pointers(){

  int a = 10;
  int* a_pt = &a; 


  cout<<"a = "<<a<<endl;
  cout<<"address of a is = "<<a_pt<<endl;
  cout<<"a again but via dereferencing ="<<*a_pt<<endl;

  cout<<"value at an incremented ptr value"<<*(a_pt+=100)<<endl;


  double A[5] = {1000.0, 2.0, 3.4, 17.0, 50.0};
  double* A_pt; 
  A_pt = A;

  cout<<*A_pt<<endl;

  for(int i=0; i<5; i++){
   cout<<i<<"  "<<*(A_pt++)<<"  "<<A[i]<<"  "<<endl; //*(A_pt+i*sizeof(float))<<endl;
  }
  

  
  cout<<"STL example\n";
  vector<double> B(10, 0.0);
  for(int i=0; i<10; i++){
    cout<<"i = "<<i<<" "<<B[i]<<endl;

    increment_element(B, i);

    cout<<"after function call, i = "<<i<<" "<<B[i]<<endl;


  }

}


class Human{

  public:

  double height;
  int age;
  std::string name;

  Human(std::string _name, int _age, double _height){  name = _name; age = _age; height = _height; }

  void say_hello(){  cout<<"my name is "<<name<<endl; }
  
};




int main(){

  //cout<<add(10, 20);

  //show_operators();

  //show_references_and_pointers();

  Human person1("Alexey", 37, 191.0); 

  person1.say_hello();

  cout<<"Age is "<<person1.age<<"  height is "<<person1.height<<endl;


  Human* pers_pt = &person1;

  (*pers_pt).say_hello();
  pers_pt->say_hello();





  //say_hello();

  return 0;
}
