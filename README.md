# DataEngineerTask


For this assignment you will create a Python program that does the following:

Load the data https://raw.githubusercontent.com/localytics/data-viz-challenge/master/data.json (in a programmatic way, no manual download)
Process the data in the following way:
Output the following columns: age, device, date, count, amount_sum.
date has the format of YYYY-MM-DD and is based on client_time.
count is the count of entries.
amount_sum is the sum the values in the amount field.
Only entries of female ("gender": "F") and Californian ("state": "CA") users should be considered.
Write the result as a CSV file total_events.csv to AWS S3.

## <a name="req">Get started</a>
### Installation

You will want to have Anaconda installed. More information here: https://docs.anaconda.com/anaconda/install/

The environment has been saved to the file: packagesADD.yml

1. Go to the directory in the command line where you have placed this repo.

2. This file may be used to create an environment using:
-------------------
$ conda env create --file packagesADD.yml
-------------------

This environment was created using the platform: win-64 

3. Activate the enviroment with:
------------------
$ conda activate envADD
------------------

4. Open Jupyter notebook from your envADD active environment through your commandline with:
------------------
$ jupyter notebook
------------------

### Run on local machine

- Activate the environment using 
----------------
$ conda activate envADD
-----------------
- Place the file 'secrets.py' in your local folder where you have the environment. Usually, here: C:\Users\{UserName}\.conda\envs\envADD\lib

- Open the file `DataEngineeringTask.ipynb` and run all cells

- You can also run the file `DataEngineeringTask.py`. Make sure you are using the provided environment or that the necessary libraries have been installed.

- To write the csv file to the s3 bucket you will need the secrets. As you can imagine, I will be sending the secrets directly to you and I will not upload the secrets to the git repo ;)
