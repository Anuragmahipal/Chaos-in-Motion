# Lorenz System Visualization

This project visualizes the **Lorenz system of differential equations** using two numerical methods:

1. **Custom Runge-Kutta 4 (RK4) implementation**  
2. **SciPy’s built-in solver (`solve_ivp` with RK45)**  

The results are animated together on the same graph to compare the trajectories of both methods.

---

## 🔬 Lorenz Equations
The Lorenz system is defined as:

\[
\frac{dx}{dt} = \sigma (y - x)
\]  
\[
\frac{dy}{dt} = x (\rho - z) - y
\]  
\[
\frac{dz}{dt} = xy - \beta z
\]  

where typical parameters are:
- σ = 10  
- ρ = 28  
- β = 8/3  

---

## 🚀 Features
- Implements the **Runge-Kutta 4th order method (RK4)** manually.  
- Uses **`scipy.integrate.solve_ivp`** with RK45 for comparison.  
- Animated 3D visualization of both trajectories in a single plot.  
- Easy-to-extend for other dynamical systems.  

---

## 📦 Requirements
Make sure you have the following installed:

```bash
pip install numpy scipy matplotlib
````

---

## ▶️ Usage

Run the Python script to generate the animation:

```bash
python lorenz_visualization.py
```

This will display a **3D animation** of the Lorenz attractor with two trajectories:

* **Cyan** → RK4 (manual implementation)
* **Orange** → RK45 (SciPy built-in)

---

## 📊 Example Output

*(Insert an image or GIF of your Lorenz attractor animation here once you generate it)*

---

## 🛠️ Project Structure

```
lorenz-project/
│── lorenz_visualization.py   # Main script
│── README.md                 # Project documentation
```

---

## 🌟 Future Improvements

* Add more solvers (e.g., Euler, Heun’s method).
* Performance benchmarks between methods.
* Interactive sliders for parameters (σ, ρ, β).

---

## 📜 License

This project is open-source under the MIT License.

```

---

👉 Do you want me to also give you the **GitHub badges (stars, forks, license, etc.)** at the top of your README for a more professional look?
