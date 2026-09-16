NumPy Analyzer

About

NumPy Analyzer is a simple Python project made for practicing NumPy and OOP. It uses a menu so the user can perform basic array and statistical operations.

Files

```text
numpy_analyzer_project/
├── main.py
└── README.md
```

Requirements

Install NumPy if it is not already installed:

```text
pip install numpy
```

Run the project:

```text
python main.py
```

Features

• Create 1D, 2D and 3D NumPy arrays
• Indexing and basic slicing
• Combine and split arrays
• Addition, subtraction, multiplication and division
• Dot product and 2D matrix multiplication
• Search, sorting and filtering
• Sum, mean, median, standard deviation and variance
• Minimum, maximum and percentile
• Correlation coefficient
• OOP using the DataAnalytics class
• Constructor and encapsulation
• Private method
• @classmethod and @staticmethod
• Menu-driven interface

OOP Used

• DataAnalytics is the main class.
• __init__() initializes the array.
• __private_check() is a private method.
• object_count() is a class method.
• info() is a static method.

Assumptions

• Numbers are entered using spaces.
• 2D and 3D array sizes must match the number of entered values.
• For filtering, the program shows values greater than the entered number.
• Division by zero is displayed as 0.
• This is a basic student-level project.

Example

```text
===== NUMPY ANALYZER =====
1. Create Array
2. Show / Index / Slice
3. Combine Arrays
4. Split Array
5. Mathematical Operations
6. Search / Sort / Filter
7. Statistics
8. Correlation
9. Object Count
10. Program Info
11. Exit

Enter choice: 7
Sum: 150
Mean: 30
Median: 30
```
