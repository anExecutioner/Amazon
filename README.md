Hi!

Steps to run the script:

1. Pull the code to local repo
2. Activate venv for that do - cd repo_location then run command activate.ps1
3. run this command to install packages - pip install -r requirements.txt
4. add your username and password into utilities/input_data.py
5. to run script with less terminal logs - pytest
6. run script with more details - pytest -v
7. to generate html reports - pytest --html=reports/report.html
