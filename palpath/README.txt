PALPATH: THE SMART BREEDING CALCULATOR
==================================================

[ PROJECT OVERVIEW ]
PalPath is a lightweight, command-line utility designed to optimize breeding strategies in monster-catching games. By utilizing a recursive algorithm and a custom CSV database, it eliminates trial-and-error by instantly generating the most efficient breeding lineage and calculating the unique base species required to reach a top-tier target.

[ FILE STRUCTURE ]
The project files are organized inside the 'palpath' directory:
- palpath/main.py: The core application script and CLI interface.
- palpath/breeding_recipes.csv: The external database storing creature attributes and breeding formulas.
- palpath/README.txt: This comprehensive project documentation file.

[ HOW TO RUN ]
This program relies entirely on Python's standard libraries. NO external installations (such as pip) are required.

1. Open your terminal or command prompt in the workspace root.
2. Navigate into the project directory by typing:
   cd palpath
3. Execute the script using Python 3 by typing:
   python3 main.py
4. Follow the interactive on-screen menu to explore the database.

[ KEY FEATURES & ADVANCED CONCEPTS DEMONSTRATED ]
This project was built focusing on robustness, efficient data manipulation, and software engineering best practices:

- Object-Oriented Programming (OOP): Creatures are instantiated as individual objects (Creature class) encapsulating their unique stats and relational parentage.
- Double Recursion & Set Logic: Employs a recursive depth-first search to traverse and print the hierarchical breeding lineage tree. Uses a separate recursive function paired with Python 'Sets' to collect base material requirements, automatically preventing duplicates.
- File I/O & Exception Handling: Dynamically reads data from 'breeding_recipes.csv' using csv.DictReader wrapped inside rigorous try-except blocks.
- Advanced Data Filtering & Lambda Sorting: Implements advanced in-memory queries allowing users to filter objects by element or dynamically rank the top 3 creatures using custom Lambda sorting keys.
- Fuzzy String Matching (Fault Tolerance): Integrates Python's built-in 'difflib' module to automatically catch and correct minor user typographical errors.

--------------------------------------------------
Created for COMP9001 Final Project.
