# Solution to run the code

## 1. Reporting endpoint implementation
### Step 1: Install all the needed requirements
- Install the `Python 3.6+`
- Run the code `pip install requirements.txt` to install the needed dependencies
- Set the working directory to the root directory

### Step 2: Run the dockered PostgreSQL database and flask app
- Run `bash ./scripts/start.sh`
- Execute the command `python3 ./scripts/app.py`

### Step 3: Change the input parameters and see the changes 
- Navigate to the url: `http://127.0.0.1:5000` and put the parameters there to query the database and get the expected reports: `http://127.0.0.1:5000/?created_from=2022-04-20&created_to=2022-06-06`
- Change the `created_from` and `created_to` parameters to see the updates of the report table

### Bonus points
About the question that if the size of the table was going to grow dramatically in a short space of time, what to do to change the code base. For the current solution, the code being sent to database is an aggregated view, which will only return the needed data, it can:
- Prevent the large size of data returned in the browser side
- In the SQL query, the filter happened before the actually aggregation and the sub view tables are already helping the efficient code running