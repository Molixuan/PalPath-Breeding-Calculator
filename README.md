# PalPath: The Smart Breeding Calculator

## 📌 Project Overview
PalPath is a lightweight, command-line utility designed to optimize breeding strategies in monster-catching games. By utilizing a recursive algorithm and a custom CSV database, it eliminates trial-and-error by instantly generating the most efficient breeding lineage and calculating the unique base species required to reach a top-tier target, accurately reflecting realistic game mechanics where parents can be reused.

## 📂 File Structure
The project files are organized inside the `palpath` directory:
* `palpath/main.py`: The core application script containing the system logic and CLI interface.
* `palpath/breeding_recipes.csv`: The external database storing creature attributes (Element, HP, ATK, DEF) and breeding formulas.
* `palpath/README.md`: This comprehensive project documentation file.

## 🚀 How to Run
This program relies entirely on Python's standard libraries. **No external installations (such as pip) are required.**

1. Open your terminal or command prompt in the workspace root.
2. Navigate into the project directory:
    ```bash
    cd palpath
    ```
3. Execute the script using Python 3:
    ```bash
    python3 main.py
    ```
4. Follow the interactive on-screen menu to explore the database.

## ✨ Key Features & Advanced Concepts Demonstrated
This project was built focusing on robustness, efficient data manipulation, and software engineering best practices:

* **Object-Oriented Programming (OOP):** Creatures are instantiated as individual objects (`Creature` class) encapsulating their unique stats (Element, HP, ATK, DEF) and relational parentage, treating memory-loaded data as a lightweight relational entity.
* **Double Recursion & Set Logic:** * Employs a recursive depth-first search to traverse and print the hierarchical breeding lineage tree with dynamic visual indentation.
  * Uses a separate recursive function paired with Python `Sets` to collect base material requirements. Since parents do not disappear after breeding in-game, the set automatically prevents duplicates, giving the user an accurate "shopping list" of unique base species to catch.
* **File I/O & Exception Handling:** Dynamically reads data from `breeding_recipes.csv` using `csv.DictReader` wrapped inside rigorous `try-except` blocks to handle potential file corruption or missing dependencies gracefully.
* **Advanced Data Filtering & Lambda Sorting:** Implements advanced in-memory queries (Option 3) allowing users to filter objects by element or dynamically rank the top 3 creatures based on combat stats (HP, ATK, DEF) utilizing custom `Lambda` sorting keys.
* **Fuzzy String Matching (Fault Tolerance):** Integrates Python's built-in `difflib` module to automatically catch and correct minor user typographical or casing errors, enhancing user experience and preventing system crashes.

---
*Created for COMP9001 Final Project.*
