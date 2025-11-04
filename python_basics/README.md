🐍 Basic Python Project

This repository contains a Jupyter Notebook with examples of basic Python code, along with a few supporting files used to demonstrate essential programming concepts such as data structures, functions, file handling, and simple data analysis.

📁 Folder Structure
python_basics/
│
├── python_basics.ipynb               # Main Jupyter Notebook with examples and explanations
├── python_basics_requirements.yml    # List of dependencies (if any)
├── greetings.py                      # Python module - Support file
├── 10_04_challenge_art.txt           # Text file - Support file
├── 10_04_challenge_art_encoded.txt   # Text file - Support file
├── 10_02_us.csv                      # CSV file - Support file
├── 10_02_ma_prime.csv                # CSV file - Support file
├── my_package/                       # Python package - Support folder
│   └── __init__.py                   # Python module - Support file
│   └── math_utils.py                 # Python module - Support file
│   └── strin_utils.py                # Python module - Support file
└── README.md                         # Project documentation

🚀 Getting Started
1. Clone the repository
git clone https://github.com/anderssonclima/python_training.git
cd python_training

2. Set up a virtual environment with the requirements (remember to replace "$env:USERPROFILE\python_basics.yml" by the current path of etl.yml)
download and save yml file in local folder, then use the following command in terminal:
conda env create -n python_basics --file "$env:USERPROFILE\python_basics.yml"
conda activate python_basics

💡 How to Run the Notebook

Launch Jupyter Notebook or JupyterLab:

jupyter notebook


Open the file python_basics.ipynb.

Run the cells in order to explore:

🧩 Support Files

The support files are used to:

Provide input data for examples.

Demonstrate how to read and write files.

Reuse helper functions from .py modules.

🧠 Learning Goals

By exploring this notebook, you’ll learn how to:

Write clean and efficient Python code.

Understand the basics of Python programming.

Work with Jupyter notebooks.

Organize small Python projects.

📚 Requirements

Python 3.11+

Jupyter Notebook

👨‍💻 Author

Andersson Lima
MSc in Business Analytics | MBA - Financial Management