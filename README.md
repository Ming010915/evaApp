# evaApp
## Unsolved Issues
- ~~The multiple users function has not been implemented yet.~~
- ~~The .csv file is reset after every restart of the app. (.csv cannot handle multiple users, solution: using SQLite database)~~
- Image name format and the method of choosing images randomly need refinement.
- A maximum of 3 reviews per image is not implemented yet.
- Overall UI design improvements are needed.

## Instructions
- Run the app.py file
- Open your web browser and go to http://127.0.0.1:5000/
- Choose the correct current user.
- Click on the buttons "Correct", "Partially Correct" or "Incorrect" to make decisions.
- Use the comment box to write additional feedbacks.
- All data will be stored in the .db file with the format: ImageName, Feedback, Comments, User1, User2, ...
- When no more images are available, the buttons will be disabled, and a message will indicate this.

## About SQLite
- https://www.sqlitetutorial.net/download-install-sqlite/
