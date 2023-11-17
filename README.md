# NoteXplorer-API
This is an API which scrapes information about upcoming Hackathons and Tech Programs from different websites and enlists them.
It is part of a project called [**NoteX**](https://github.com/The-NoteX/NoteX)

# Tech Stack Used
- Python
- Selenium
- Docker
- Fast API

# Build Instruction
- Clone the repo <br>
  ```sh
     git clone https://github.com/TeeWrath/NoteXplorer-API.git 
  ```
- Move to Repository Directory <br>
  ```sh 
  cd NoteXplorer-API 
  ```
- Build Docker Container <br>
  ```sh
  docker build -t main.py  .
  ```
- Use the container and activate the API <br>
  ```sh
  docker run -d -p 8000:80 --name fastapi-container main.py
  ```
- Use the following endpoint <br>
  ``` http://10.50.5.86:8000/hackathons```

# Contribution Guidelines
- Clone the repositoy in your local system.
- Go through the application and find issues or features that you wish to add.
- Go to issues and create your issue.
- Wait for issue to be assigned.
- Work on your issue
- Create a pull request
- Wait for it to be reviewed and merged
- Congratulations !! You have just contributed to Hackathon API.
