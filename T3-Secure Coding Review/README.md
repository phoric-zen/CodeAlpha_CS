## Secure Coding Review

## 📌 Overview

This project focuses on performing a secure code review of a basic application. The goal is to identify potential vulnerabilities and apply best practices to ensure secure coding standards are followed. The process includes manual code inspection and the use of static analysis tools.

---

## 🎯 Objectives

- Review source code for common security vulnerabilities.
- Use automated tools to enhance detection.
- Document and fix the identified issues.
- Promote secure software development practices.

---

## 🧰 Technologies & Tools Used

- **Language:** Python 3
- **Static Analysis Tool:** [Bandit](https://github.com/PyCQA/bandit)
- **Manual Review Techniques:** OWASP top 10 checklist
- **Text Editor/IDE:** VS Code / PyCharm

---

## 📁 Project Structure

```
T3_Secure_Coding_Review/
├── insecure_code/
│   └── vulnerable_app.py            # Code with security flaws
├── fixed_code/
│   └── secure_app.py                # Remediated version of the app
├── tools_report/
│   └── bandit_report.txt            # Output from static analysis
├── vulnerability_report.md         # Documentation of issues & fixes
└── README.md                        # This file
```

---

## 🛠️ Setup & Analysis Instructions

### ✅ 1. Clone the Repository

```bash
git clone https://github.com/your-username/T3_Secure_Coding_Review.git
cd T3_Secure_Coding_Review
```

### ✅ 2. Run Static Analysis with Bandit

Install Bandit (if not already installed):

```bash
pip install bandit
```

Run Bandit on the insecure code:

```bash
bandit -r insecure_code/ > tools_report/bandit_report.txt
```

### ✅ 3. Manual Review Checklist

Manually inspect code in `insecure_code/` and check for:

| Vulnerability         | Example                  |
|-----------------------|--------------------------|
| SQL Injection         | Unparameterized queries  |
| XSS                   | Directly rendering input |
| Command Injection     | `os.system(user_input)`  |
| Insecure Deserialization | Use of `eval()` or `pickle` |
| Hardcoded Secrets     | API keys in code         |
| Missing Input Validation | No sanitization        |

Record findings in `vulnerability_report.md`

---

## 🔍 Sample Findings

### ❌ Vulnerability: Command Injection

- **File:** `vulnerable_app.py`
- **Line:** 27
- **Issue:** Uses `os.system(user_input)` directly
- **Fix:** Use `subprocess.run(shlex.split(user_input))` with validation

---

## ✅ Fix Implementation

All fixed issues are located in:

```
fixed_code/secure_app.py
```

These include:

- Proper input validation
- Removal of insecure function calls
- Secure handling of user data

---

## 🧪 Testing the Fixes

After applying fixes, re-run Bandit:

```bash
bandit -r fixed_code/
```

Check that no critical or high severity issues remain.

---



---

## 👤 Author

# phoric_zen  


---

## 📎 License

This project is licensed under the MIT License. See the `LICENSE` file for details.
