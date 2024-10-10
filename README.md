[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-2e0aaae1b6195c2367325f4f02e2d04e9abb55f0b24a779b69b11b9e10269abc.svg)](https://classroom.github.com/online_ide?assignment_repo_id=16178021&assignment_repo_type=AssignmentRepo)
# nti_template_py
i grunden var detta project tutorialen för flask som är en blog sida. Jag använde den som grund för att göra det som behövdes då jag tror inte jag skulle ha tillräkligt med tid för att lära mig flask tillräkligt bra för uppgiften. Jag har inte ändrat så mycket i filen ./flaskr/auth.py eller ./flaskr/db.py men resten av filerna har jag ändrat ganska mycket eller gjort helt själv. några av html filerna är också inte ändrade dock har jag behövt göra några egna. du kan hitta tutorialen här "https://github.com/pallets/flask/tree/main/examples/tutorial" för att se vad jag har gjort själv och de som är taget.
# requirements
a pushover account
pushover app installed on your phone

# setup
1. create a .venv [ py -3 -m venv .venv ]
2. install requirements.txt [ pip install -r ./requirements.txt ]
3. initialize the data base for the server [ flask --app flaskr init-db ]

# running the program
[ flask --app flaskr run --host=0.0.0.0 ]