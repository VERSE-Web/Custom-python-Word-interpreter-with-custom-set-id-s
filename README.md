# 🔤 Custom Python Word Interpreter

This is a simple Python-based interpreter that converts characters into a unique custom ID format. It supports letters (uppercase and lowercase), digits (including single-digit negatives), and a range of special characters.

**ID format:**
- `#` — Letters  
- `$` — Numbers (only supports single-digit values like `1` or `-2`)  
- `@` — Special characters

---

## 📘 Features

- 🔡 Maps letters, numbers, and symbols to a custom ID format
- 🔁 Reverse mappings included for future decoding
- 🖥️ Command-line interface
- 🔧 Easy to extend and customize

---

## ⚙️ How to Run

> **Python 3.11+ is required**

1. Clone the repository:

```bash
git clone https://github.com/VERSE-Web/Custom-python-Word-interpreter-with-custom-set-id-s.git
cd Custom-python-Word-interpreter-with-custom-set-id-s
Run the interpreter:

bash
Copy
Edit
python interpreter.py
💡 Example
Input:

text
Copy
Edit
Hello@2
Output:

text
Copy
Edit
Id Values{ # = letters, $ = numbers (Only support for 1 digit values like 1 or -2), @ = special characters }
Codes: ['#00034', '#00005', '#00012', '#00012', '#00015', '@00020', '$00002']
🧱 Project Structure
interpreter.py – main interpreter logic

data.py – mappings for characters and reverse lookup

pyproject.toml (optional) – for Python project configuration

🙋 Author
Mehran-Ul Islam
📍 GitHub Profile
📝 License: MIT

🛠️ To-Do
 Add decoding (ID → character)

 Write unit tests (pytest)

 Package for PyPI

 Create GUI or web interface (optional)

🤝 Contributing
Contributions are welcome!
Please open an issue or pull request if you’d like to help improve the project.

📄 License
This project is licensed under the MIT License.
