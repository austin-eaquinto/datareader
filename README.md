# datareader
a program that reads any type of file and iterprets the desired data

[GitHub Repo Link](https://github.com/austin-eaquinto/datareader)

[Matplotlib and PyQt Connection?](https://matplotlib.org/stable/users/explain/figure/backends.html)

## Virtual Environment Set Up

Using virtual environments and a requirements.txt file is a critical best practice for Python projects, especially when collaborating with others. Here's why and how to set it up:

- Isolation: Virtual environments keep project dependencies isolated from your system-wide Python and other projects.

- Reproducibility: requirements.txt ensures everyone uses the exact same versions of libraries (e.g., pandas, matplotlib, PyQt), avoiding "it works on my machine" issues.

- Dependency Management: Simplifies installing/updating libraries for all collaborators.

## Step-by-Step Guide

Navigate to root of project
````
cd path/to/project-root
````
Create a virtual environment (e.g., named "RogerVenv")
````
python -m venv RogerVenv #or py -m venv RogerVenv
````

Activate the Virtual Environment
````
.\venv\Scripts\activate    #Windows
source venv/bin/activate   #Mac
````

Once inside the virtual environment you can install project libraries/dependencies using:
````
pip install -r requirements.txt
````

If you created your virtual environment with a different name, be sure to add it to the .gitignore file
````
/myVenv
````

Deactivate (exit the environment):
Run this in your terminal:
````
deactivate
````
## Venv Troubleshooting
If you are having issues in the project not recognizing an already imported library, make sure to check that the Python interpreter is using your virtual environment instead of your system Python

In VSCode:
- Open the command palette (Ctrl+Shift+P or Cmd+Shift+P).
- Search for Python: Select Interpreter.
- Choose the Python executable inside your virtual environment (e.g., myVenv/Scripts/python.exe on Windows, myVenv/bin/python on macOS/Linux).


In VSCode, your terminal should show the name of your virtual environment towards the bottom right. This is one way to verify you are in the virtual environment. The terminal may not always display that you are in the virtual environment but there are ways to check. You can also verify that the virtual environment is active with the following command:
````
pip --version  # Check if the path includes your venv (e.g., "myVenv\Lib\site-packages")
````

## Add New Dependencies to Project

If new libraries/dependencies are needed, ensure that you are in the virtual environment and proceed with the following:

````
pip install library-dependency-name
````

Export all installed packages (with versions) to requirements.txt:
````
pip freeze > requirements.txt
````

Share requirements.txt with the team. Commit this file to Git so others can replicate the new environment:
````
git add requirements.txt
git commit -m "Add requirements.txt"
git push
````