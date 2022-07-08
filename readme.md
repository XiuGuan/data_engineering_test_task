# A. Team Data Engineering Exercise

This is our take-home assessment for data engineers. It will focus on:

1. SQL.
2. API services.
3. Cloud infrastructure (GCP/AWS).

Don't spend more than a few hours on it. It doesn't matter if the solution isn't fully complete. At least have a go at both exercises. Feel free to reach out if you have any additional questions.

Additional notes:

- You will need Docker installed locally to run the database container.
- To start the database container, run `bash ./scripts/start.sh`.
- Please implement your API solution in either Node.js or Python.

## 1. Reporting endpoint implementation

An internal team is building a report to display to our company leadership. The report will display the month-over-month growth of our company profit in a table that looks like this:

| Month         | Profit  | Growth from last month |
|---------------|---------|------------------------|
| January 2022  | $10,000 | 0%                     |
| February 2022 | $14,000 | 8%                     |
| March 2022    | $18,000 | 16%                    |

Profit from a single invoice is calculated as:

`profit = amount_total - amount_to_pay_to_builder`

Your task is to build the API end point that will service this request from our database. You can assume that:

- It will not require any authentication or authorization.
- The request parameters will include two parameters for filtering the invoices by their `created_date` value: `created_from` and `created_to`.
- The interface of the REST API should be well documented for client consumption.

_Stretch goals_

- Imagine that the size of the table was going to grow dramatically in a short space of time. Make changes to the code base to ensure that report requests will:
  - Not overload the database, and
  - Not take too long to display.

## 2. Data warehouse integration design

We want to integrate our invoice database with our new data warehouse, so that we can make our invoice data available for our BI tools. Our job is to design the process that makes the Postgres data available in the data warehouse. Create a design document in the `/docs` folder describing how you would implement this. Our requirements are:

- The data must be as fresh as possible.
- As we use the data for audit reporting, we must be 100% confident that the data in the warehouse matches the data in our Postgres database.

You can assume that:

- Our Postgres database is hosted in AWS RDS.
- Our data warehouse product is Google BigQuery.
- Our infrastructure stack is AWS/GCP. You can pick any tools from these cloud providers.

_Stretch goals_

- We want to add an automated alerting system on top of our data warehouse that will automatically send a payment reminder email to our Client if any of their invoices are due and they haven't paid yet. Describe how you would implement this.
