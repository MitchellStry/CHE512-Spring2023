#include <iostream>
#include <vector>
#include <cmath>
#include <fstream>

using namespace std;

double time_step_q(double q, double p, double mass, double dt){

  double q_new;

  q_new = q + dt * (p/mass);

  return q_new;
}

double time_step_p(double p, double f, double dt){

  double p_new;

  p_new = p + f * dt;

  return p_new;
}


double energy_func(double q, double k){

  double energy;

  energy = 0.5*k*q*q;

  return energy;
}


double force_func(double q, double k){

  double force;

  force = -k*q;

  return force;
}


int main(){

  std::vector<double> X;
  std::vector<double> P;
  std::vector<double> T;
  std::vector<double> E_pot;
  std::vector<double> E_kin;
  std::vector<double> E_tot;

  double x0;
  double x;
  double p;
  double p0;
  double k;
  double mass; 
  double dt;
  double e_pot;
  double f;
  double e_kin;
  int nsteps;
 
  dt = 0.01;
  nsteps = 10000;
  x0 = -1.0;
  p0 = 0.0;
  k = 0.1;
  mass = 1.0;

  x = x0;
  p = p0;

  std::ofstream f1("E_tot.txt");
  std::ofstream f2("E_pot.txt");
  std::ofstream f3("E_kin.txt");
  std::ofstream f4("X.txt");
  std::ofstream f5("P.txt");
  std::ofstream f6("T.txt");


  for (int i = 0; i < nsteps; ++i) {

    X.push_back(x);
    P.push_back(p);
    T.push_back(i * dt);
    e_pot = energy_func(x, k);
    f = force_func(x, k);
    E_pot.push_back(e_pot);
    e_kin = 0.5 * p * p / mass;
    E_kin.push_back(e_kin);
    E_tot.push_back(e_kin + e_pot);

    x = time_step_q(x, p, mass, dt);
    p = time_step_p(p, f, dt);

    f1 << e_pot + e_kin << "\n";
    f2 << e_pot << "\n";
    f3 << e_kin << "\n";
    f4 << x << "\n";
    f5 << p << "\n";
    f6 << i * dt << "\n";

  }

  f1.close();
  f2.close();
  f3.close();
  f4.close();
  f5.close();
  f6.close();

  return 0;
}




