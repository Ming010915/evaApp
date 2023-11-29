# evaApp
## Unsolved Issues
- ~~The multiple users function has not been implemented yet.~~
- ~~The .csv file is reset after every restart of the app. (.csv cannot handle multiple users, solution: using SQLite database)~~
- Image name format and the method of choosing images randomly need refinement.
- ~~A maximum of 3 reviews per image is not implemented yet.~~
- Overall UI design improvements are needed.
- ~~Normalisation of the database is needed.~~
- ~~Generate a .csv file from the database.~~

## Instructions
- Run the app.py file
- Open your web browser and go to http://127.0.0.1:5000/
- Choose the correct current user.
- Click on the buttons "Correct", "Partially Correct" or "Incorrect" to make decisions.
- Use the comment box to write additional feedbacks.
- All data will be stored in the .db file with the format: ImageName, Feedback, Comments, Username.
- When no more images are available, the buttons will be disabled, and a message will indicate this.
- After running the final.py file, the process, which includes pivoting the table, will result in the generation of a .csv file.

## About SQLite
- https://www.sqlitetutorial.net/download-install-sqlite/