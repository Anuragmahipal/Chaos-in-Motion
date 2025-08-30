
#include <bits/stdc++.h>
using namespace std;

const double sigma = 10.0;
const double rho   = 28.0;
const double beta  = 8.0 / 3.0;

const double dt = 0.01;
const int steps = 10000; 

struct State {
    double x, y, z;
};

State lorenz(const State &s) {
    State ds;
    ds.x = sigma * (s.y - s.x);
    ds.y = s.x * (rho - s.z) - s.y;
    ds.z = s.x * s.y - beta * s.z;
    return ds;
}

State rk4_step(const State &s, double dt) {
    State k1 = lorenz(s);

    State s2 = { s.x + 0.5*dt*k1.x,
                 s.y + 0.5*dt*k1.y,
                 s.z + 0.5*dt*k1.z };
    State k2 = lorenz(s2);

    State s3 = { s.x + 0.5*dt*k2.x,
                 s.y + 0.5*dt*k2.y,
                 s.z + 0.5*dt*k2.z };
    State k3 = lorenz(s3);

    State s4 = { s.x + dt*k3.x,
                 s.y + dt*k3.y,
                 s.z + dt*k3.z };
    State k4 = lorenz(s4);

    State next;
    next.x = s.x + (dt/6.0) * (k1.x + 2*k2.x + 2*k3.x + k4.x);
    next.y = s.y + (dt/6.0) * (k1.y + 2*k2.y + 2*k3.y + k4.y);
    next.z = s.z + (dt/6.0) * (k1.z + 2*k2.z + 2*k3.z + k4.z);

    return next;
}

int main() {
    State s = {1.0, 1.0, 1.0};

    ofstream fout("lorenz.csv");
    fout << "x,y,z\n"; 

    for (int i = 0; i < steps; i++) {
        fout << s.x << "," << s.y << "," << s.z << "\n";
        s = rk4_step(s, dt);
    }

    fout.close();
    return 0;
}

