from datetime import timedelta, datetime
import random
import io 

# Operators#
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator
from airflow.utils.dates import days_ago # scheduling tool that allows us to write the code in line 24


######## Functions that will be called later #############################
# List of apple types
apples = ["pink lady", "jazz", "orange pippin", "granny smith", "red delicious", "gala", "honeycrisp", "mcintosh", "fuji"]

# This function will open a text file, read the name from the file and print the name with a hello
file_path = '/opt/airflow/dags/code_review.txt'

def print_hello(file_path):
    with open(file_path,'r') as f:
    name = f.read()
    print(f"hello {name}")
    
# This function will randomly select an apple, put it into a string and print the string
def random_apples(apples):
    random_apple= random.choice(apples)
    print(f"Your apple is: {random_apple}")

############# Config ########################
# Create a dictionary of default args for scheduling and retries. 
# This allows us to pass arguments into a DAG object

default_args = {
    #Scheduling section
    'start_date': days_ago(2), # The start date for DAG running. This function allows us to set the start date to two days ago
    'schedule_interval': timedelta(days=1), # How often our DAG will run. After the start_date, airflow waits for the schedule_interval to pass then triggers the DAG run
    #Retries section
    'retries': 1, # How many times to retry in case of failure
    'retry_delay': timedelta(minutes=5), # How long to wait before retrying
}

################### DAG instantiation ##########################

from airflow import DAG

with DAG(
    'code_review_steps', # a unique name for our DAG
    description='A DAG that says hello by name and picks random apples"', # a description of our DAG
    default_args=default_args, # pass in the default args.
) as dag:

    
    ### TASKS ###

# This task will write a name to a text file
    write_name_task = BashOperator(
        task_id='write_name', # this is the unique identifier of this task within the DAG
        bash_command='echo "Nikisha" >  /opt/airflow/dags/code_review.txt' # this is the command that will be run
    )
    
# This task uses a Python operator to call the function 'print_hello()'
    hello_task = PythonOperator(
        task_id='say_hello', # this is the unique identifier of this task within the DAG
        python_callable = print_hello # allows the DAG to execute the function print_hello listed above 
    )

# The DummyOperator doesn't actually do anything and is used to show graph structure or for grouping tasks in a DAG
    dummy_task = DummyOperator(
        task_id='dummy'
    )
    # set the task order
    # The example below is using a list
    # the reason for this is to specify that we want 'hello_task' to precede 'date_task' & 'dummy_task'
    # and there are no dependencies between 'date_task' and 'dummy_task'
    hello_task >> [date_task, dummy_task]
