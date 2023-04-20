#include <iostream>
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

  for(int i=0; i<10; i++){
    cout<<i<<" "<<i%3<<endl;
  }

}

int main(){

   //cout<<add(10, 20);

   show_operators();

  //say_hello();

  return 0;
}
