# Title
DE101 Bootcamp- Code Review Week 11

# Name
Nikisha Banks

# Technologies Used: 
Git hub, Visual Studio Code, Airflow, Docker

# Languages and tools used: 
DAG Python and Bash Operators

# Description:
In this project, I used Airflow to orchestrate a workflow that did the following:
  1.Create a file that contained my name
  2.Read my name from the file and say "Hello"
  3.Pick 3 random apples  

# Setup/Installation Requirements:
- To see the code files in this project:
  1. Clone the repo in Git Hub: 
                a. Click the green "code" button
                b. Under the "Local" tab, copy and paste the URL that is under HTTPS
- Set up Airflow 
  1. In your visual studio terminal of your choice, create and activate a virtual environment in your repository folder by typing the following commands: 
     1. python3.10 -m venv <virtual environment name>
     2. source <virtual environment name>/bin/activate 
  2. Run the setup.sh file by typing ./setup.sh. This scripts sets up your environment and installs the necessary components
  3. Create the following new directories in the same folder:
     1. ./logs
     2. ./plugins
     3. ./dags
  4. Pull down the latest version of Airflow by typing 	"curl -LfO 'https://airflow.apache.org/docs/apache-airflow/stable/docker-compose.yaml'"
  5. Create a Airflow user id by typing "echo -e "AIRFLOW_UID=$(id -u)\nAIRFLOW_GID=0" > .env"
  6. Start Airflow and all related containers by typing:
     1. docker-compose up airflow-init
     2. docker-compose up
  7. Leave that terminal running and then open a new terminal to continue working in
  8. In your browser, go to localhost:8080, this will take you to the Airflow Graphical User Interface
- Shutting down Airflow and docker
  1. Switch to the terminal that is running your Airflow commands
  2. Either press CTRL + C or type "docker compose down"
  3. Type "docker system prune --volumes" to remove all volumes from the docker container
  4. type "docker volume list" to confirm that there are no volumes
   
# Known Bugs
No known bugs

# Project Visuals
## DAG 
The DAG Diagram in this project shows the order of tasks and their dependencies, if any
  1. The flow starts with the 'echo_to_file' task, this task is a Bash Operator that creates a text file that writes a name
  2. The second task is the 'greeting_task', this task is a Python Operator task that calls the function 'print_hello' and reads the file created by the first task and prints a greeting of "hello" along with the name in the file
  3. The third thru fifth tasks are Python Operator tasks that calls the function 'random_apples' and returns a random apple chosen from a list called 'apples'
  4. The last task ends the DAG  
   
![Image](https://github.com/nbanks062523/CodeReview_week10/blob/main/images/nfl_sports_betting.drawio.png)
---
## Big Query Datasets
This section displays the tables, fields and data types contained in the sports betting dataset.

**Games Dimension Table Schema**
![Image](https://github.com/nbanks062523/CodeReview_week10/blob/main/images/Games_Dimension_Tble.png)
---
**Over/Under Fact Table Schema**
![Image](https://github.com/nbanks062523/CodeReview_week10/blob/main/images/Ovr_Undr_FctTble.png)
---
**Points Spread Fact Table Schema**
![Image](https://github.com/nbanks062523/CodeReview_week10/blob/main/images/fct_points_spread.png)
---
**Team Lookup Table Schema**
![Image](https://github.com/nbanks062523/CodeReview_week10/blob/main/images/TeamID_LookupSchema.png)
---
## Table Views Queries and Schemas
In this section, alternate "views" are created that have joined the tables together to allow for greater flexibility in analysis of the data.
---
**Games**
![Image](https://github.com/nbanks062523/CodeReview_week10/blob/main/images/Games_ViewTable.png)
![Image](https://github.com/nbanks062523/CodeReview_week10/blob/main/images/Query_GamesViewTable.png)
---
**Over/Under**
![Image](https://github.com/nbanks062523/CodeReview_week10/blob/main/images/Ovr_Undr_TbleView.png)
![Image](https://github.com/nbanks062523/CodeReview_week10/blob/main/images/Query_OvrUndrTbleView.png)
---
**Points Spread**
![Image](https://github.com/nbanks062523/CodeReview_week10/blob/main/images/PointSpread_ViewTable.png)
![Image](https://github.com/nbanks062523/CodeReview_week10/blob/main/images/Query_PointSpreadViewTble.png)

## Sample Page from Sports Betting Dashboard
Below is a screenshot of one of the pages on the sports betting dashboard. Some of the metrics represented in this page are: 
  - A season by season comparison of wins between the home and away teams
  - A team by team overview of the percentage of times the winning team scored over the winning line
  - The Average scores of each game from 1978 to 2023

 ![Image](https://github.com/nbanks062523/CodeReview_week10/blob/main/images/Dashboard_NB.png) 

# License
*Copyright 2024, Data Stack Academy Fall 2023 Cohort*

*Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:*

*The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.*

*THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.*# code_review_wk11
