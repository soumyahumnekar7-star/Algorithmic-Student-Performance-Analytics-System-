# Student Marks Analyzer & Algorithmic Benchmarking Tool

A lightweight, modular Python application built for the **Problem Solving and Python Programming** course (1st Year CSE-AIML). 

This project processes, cleans, and analyzes student performance metrics using native Python data structures and manual algorithmic logic—without relying on third-party libraries like Pandas or NumPy.

---

## 📌 Features

* **Data Cleaning & Deduplication:** Filters out duplicate student records based on unique Student IDs using Set operations while preserving input order.
* **Array Operations (Manual Implementation):**
  * In-place array reversal using a two-pointer approach.
  * Score-based array partitioning (splitting records above/below a threshold grade).
  * Selection-based search algorithm to find the $K^{\text{th}}$ lowest score without built-in sort functions.
* **Synthetic Data Generation:** Generates synthetic score batches using a custom **Linear Congruential Generator (LCG)** pseudo-random algorithm.
* **Performance Benchmarking:** Compares real-world execution speeds between sequential List linear searches ($\mathcal{O}(N)$) and Dictionary hash lookups ($\mathcal{O}(1)$).

---

## 📁 Repository Structure

```text
student-marks-analyzer/
│
├── statement.md       # Detailed problem statement, target audience, and scope
├── README.md          # Project overview, setup, and execution guidelines
├── main_app.py        # Terminal UI and main execution loop
├── data_utils.py      # Input validation, set-based deduplication, and grading logic
├── array_algo.py      # Algorithmic array reversals, partitioning, and K-th element logic
└── performance.py     # LCG random number generator and search speed benchmarking
