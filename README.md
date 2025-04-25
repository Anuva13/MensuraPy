<h1 align="center">
<img src="https://raw.githubusercontent.com/Anuva13/MensuraPy/main/branding/mensurapylogo.svg"
width="300">
</h1><br>

**MensuraPy** is a Python package that provides accurate and user-friendly functions to calculate the **area**, **perimeter**, **surface area**, and **volume** of 2D and 3D geometric shapes. Designed for learners, educators, developers, and engineers alike, it makes geometry calculations easy and consistent, supporting multiple units.


- **Documentation:** 
- **Source code:** https://github.com/Anuva13/MensuraPy/tree/main/MensuraPy
- **Bug reports:** https://github.com/Anuva13/MensuraPy/issues
- **Report a security vulnerability:** https://github.com/Anuva13/MensuraPy/security

## 🚀 Features

- Area calculation for 2D shapes like square, rectangle, circle, triangle, ellipse, and more
- Perimeter calculation for standard 2D and 3D shapes
- Surface area computation for cubes, cuboids, spheres, cones, cylinders, etc.
- Volume calculation for 3D shapes with unit consistency
- Support for multiple units (mm, cm, m, etc.)
- Built-in exception handling
- Modular and extensible structure

## 📦 Installation

```bash
pip install mensurapy
``` 

## 🛠 Usage

```python
from mensurapy import area, perimeter, surface_area, volume

print(area("rectangle", "5m", "10m"))           # 50.0 m²
print(perimeter("circle", "7cm"))               # 43.96 cm
print(surface_area("cube", "4m"))               # Total Surface Area: 96.0 m²
print(volume("cylinder", "3m", "10m"))          # 282.74 m³
```
## 📚 Supported Shapes

2D Shapes
Square, Rectangle, Circle, Triangle, Parallelogram, Trapezium, Ellipse, Rhombus

3D Shapes
Cube, Cuboid, Sphere, Cone, Cylinder, Pyramid, Prism, Hemisphere, Ellipsoid

## 🧪 Testing

To run tests for MensuraPy:

1. Clone the repository.
2. Navigate to the project directory
3. Run the tests using

```bash
python3 -m unittest discover tests
```

