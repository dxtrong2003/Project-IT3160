import webbrowser
import os
import subprocess

cwd = os.getcwd()

file_path = cwd + '\data\osmmap.html'

webbrowser.open_new_tab(file_path)

subprocess.run(["python", "flaskAPI.py"])