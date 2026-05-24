# PalPath: The Smart Breeding Calculator

##  Project Overview
PalPath is a lightweight, command-line utility designed to optimize breeding strategies in monster-catching games. By utilizing a recursive algorithm and a custom CSV database, it eliminates trial-and-error by instantly generating the most efficient breeding lineage and calculating the unique base species required to reach a top-tier target, accurately reflecting realistic game mechanics where parents can be reused.

##  File Structure
The project files are organized inside the `palpath` directory:
* `palpath/main.py`: The core application script containing the system logic and CLI interface.
* `palpath/breeding_recipes.csv`: The external database storing creature attributes (Element, HP, ATK, DEF) and breeding formulas.
* `palpath/README.md`: This comprehensive project documentation file.

##  How to Run
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

##  Concepts Applied
This project incorporates several concepts covered in the course to build a functional CLI tool:

* **Object-Oriented Programming (OOP):** Uses a `Creature` class to structure individual stats (Element, HP, ATK, DEF) and parent relationships.
* **Recursion & Sets:** Implements recursive functions to traverse and display the breeding tree. Python `Sets` are used to filter duplicate base creatures, reflecting the game mechanic where parents are reusable.
* **File I/O & Error Handling:** Reads data from `breeding_recipes.csv` using `csv.DictReader`, incorporating `try-except` blocks to handle missing or unreadable files.
* **Data Sorting (Lambda):** Utilizes custom `lambda` functions to sort the dictionary, allowing users to rank creatures by specific combat stats.
* **String Matching:** Uses the built-in `difflib` module to offer spelling suggestions if a user mistypes a creature's name.

---
*Created for COMP9001 Final Project.*

