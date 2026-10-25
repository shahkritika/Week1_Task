# Full-Stack Developer Internship - Week 1: Day 1

**Programme:** Full-Stack Developer Intern (Week 1 of 4)  
**Date:** Sunday, 25 October 2026  
**Intern Name:** Kritika Shah  
**Topic:** Python Core Fundamentals & Git Essentials  

---

## 📌 Overview

This repository contains the solutions and execution instructions for **Day 01** of the Full-Stack Developer Internship program.

- **Morning Module:** Python Core (variables, data types, casting, string manipulation, vowel counting, f-strings).
- **Afternoon Module:** Git Basics & Environment Setup (virtual environment configuration, `.gitignore`, structured commits, remote repository synchronization, and PDF documentation report).

---

## 📂 Repository Structure

```text
Week1-Day1Task/
├── .gitignore                   # Python & virtual environment ignore rules
├── README.md                    # Project documentation and execution instructions
├── run_all.py                   # Master script to execute all morning exercises
├── morning_tasks/
│   ├── a1.py                    # A1: 5 variables of different types + type()
│   ├── a2.py                    # A2: Read number & convert to int, float, str
│   ├── a3.py                    # A3: Reverse string, uppercase, vowel count
│   └── a4.py                    # A4: User info formatting with f-strings
```

---

## 🚀 Tasks & Solutions Summary

### 🌅 Morning · Python Core

#### **A1: Variable Creation & Type Inspection**
- **Objective:** Create 5 variables of distinct types and display their value and type using `type()`.
- **Types Covered:** `int`, `float`, `str`, `bool`, `list`.
- **Script:** [`morning_tasks/a1.py`](morning_tasks/a1.py)

#### **A2: Number Input & Type Casting**
- **Objective:** Read a numeric value from input and convert it into `int`, `float`, and `str`, printing the value and type of each.
- **Script:** [`morning_tasks/a2.py`](morning_tasks/a2.py)

#### **A3: Sentence Processing (Reverse, Uppercase, Vowel Count)**
- **Objective:** Read a sentence; print the reversed string using slice notation `[::-1]`, uppercase using `.upper()`, and count total vowels with breakdown.
- **Script:** [`morning_tasks/a3.py`](morning_tasks/a3.py)

#### **A4: User Info & F-Strings**
- **Objective:** Read `name`, `age`, and `city`; format and print clean sentences using Python 3 f-strings.
- **Script:** [`morning_tasks/a4.py`](morning_tasks/a4.py)

---

### 🌇 Afternoon · Git Basics & Setup

1. **Virtual Environment (`venv`)**:
   - Initialized Python 3.12 virtual environment:
     ```bash
     python -m venv venv
     ```
   - Verified active environment using `pip list`.
2. **Git Repository Setup**:
   - Cloned remote GitHub repository: `https://github.com/shahkritika/Week1-Day1Task.git`
3. **Ignore Configuration (`.gitignore`)**:
   - Configured `.gitignore` to prevent tracking virtual environments (`venv/`), build caches, and local temporary files.
4. **Structured Git Commit Workflow**:
   - Organized changes into 3 clear, atomic commits with informative commit messages:
     1. `feat(morning): implement Day 1 Python core tasks (A1-A4)`
     2. `chore(git): update .gitignore for Python virtual environments and temporary files`
     3. `docs: add comprehensive README documentation and Day 1 task guide`
5. **Push to GitHub**:
   - Synchronized all commits to the remote `main` branch.

---

## 🛠️ How to Run Locally

### 1. Clone the repository
```bash
git clone https://github.com/shahkritika/Week1-Day1Task.git
cd Week1-Day1Task
```

### 2. Activate Virtual Environment
- **Windows (PowerShell):**
  ```powershell
  .\venv\Scripts\Activate.ps1
  ```
- **Linux / macOS:**
  ```bash
  source venv/bin/activate
  ```

### 3. Run all tasks at once
```bash
python run_all.py
```

### 4. Run individual tasks
```bash
python morning_tasks/a1_variables.py
python morning_tasks/a2_number_conversion.py
python morning_tasks/a3_string_operations.py
python morning_tasks/a4_fstrings_user_info.py
```

---
