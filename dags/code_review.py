from datetime import timedelta, datetime

# Operators#
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator
from airflow.utils.dates import days_ago # handy scheduling tool that allows us to write the code in line 24

# Create a list of apple types
apples = ["pink lady", "jazz", "orange pippin", "granny smith", "red delicious", "gala", "honeycrisp", "mcintosh", "fuji"]

def print_date():
    """A very simple python function to call"""
    print(datetime.now())

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
# The DAG object; we'll need this to instantiate a DAG
from airflow import DAG

with DAG(
    'hello', # a unique name for our DAG
    description='A simple DAG to print "Hello World"', # a description of our DAG
    default_args=default_args, # pass in the default args.
) as dag:
    description = 'A simple DAG to print "Hello World"', # a description of our DAG
    default_args = default_args, # pass in the default args defined at line 19

    
    ### create simple tasks: ###
# The DummyOperator doesn't actually do anything and is used to show graph structure or for grouping tasks in a DAG
    dummy_task = DummyOperator(
        task_id='dummy'
    )
# The BashOperator allows you to run any bash command
    hello_task = BashOperator(
        task_id='print_hello', # this is the unique identifier of this task within the DAG
        bash_command='echo Hello World' # this is the command that will be run
    )
# The PythonOperator 
    date_task = PythonOperator(
        task_id="date_task", # this is the unique identifier of this task within the DAG
        python_callable=print_date # allows the DAG to execute the function print_date listed above 
    )

    # set the task order
    # The example below is using a list
    # the reason for this is to specify that we want 'hello_task' to precede 'date_task' & 'dummy_task'
    # and there are no dependencies between 'date_task' and 'dummy_task'
    hello_task >> [date_task, dummy_task]
