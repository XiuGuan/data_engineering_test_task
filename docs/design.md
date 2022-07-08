# Data warehouse integration design

## Requirements
We want to integrate our invoice database with our new data warehouse, so that we can make our invoice data available for our BI tools. Our job is to design the process that makes the Postgres data available in the data warehouse.

### Points
- The data must be as fresh as possible.
- As we use the data for audit reporting, we must be 100% confident that the data in the warehouse matches the data in our Postgres database.
- We want to add an automated alerting system on top of our data warehouse that will automatically send a payment reminder email to our Client if any of their invoices are due and they haven't paid yet. Describe how you would implement this.


### Tech Stack
- Our Postgres database is hosted in AWS RDS.
- Our data warehouse product is Google BigQuery.
- Our infrastructure stack is AWS/GCP. You can pick any tools from these cloud providers.
 
## Design Solution
The overall design is to set up the connection between the PostgreSQL and Google Cloud Platform. The connection needs to be (1) Complete; (2) Accurate; (3) Secure; (4) Fast. 

The chosen tech stack:
- AWS Lambda
- AWS IAM
- AWS Security Manager
- AWS Cloudwatch 

The workflows and pipelines are: Firstly set up the initial load to load all the historical data from PostgreSQL in AWS RDS to Google CLoud Platform, after that the daily refresh is the event to trigger the AWS Lambda function which sends the new data to GCP. Apart from that, there is one more secuirty checking process, which is every time once the Lambda function get triggered from AWS side, it also has a reversed trigger from GCP side to compare the data alignment, if not then the Lambda will trigger again to get the missing data. 
