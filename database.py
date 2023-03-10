from sqlalchemy import create_engine, text
import os


db_connection_string = os.environ['DB_CONNECTION_STRING']

engine = create_engine(
  db_connection_string,
  connect_args={
    "ssl" :{
    "ssl_ca": "/etc/ssl/cert.pem"
  }
  })


def load_jobs_from_db():
    with engine.connect() as conn:
    # Execute a SQL query to select all rows from the "jobs" table
      query = text('select * from jobs')
      result = conn.execute(query)

    # Iterate through the rows and convert them to dictionaries
    job = []
    for row in result.fetchall():
        result_dict = {}
        for index, column in enumerate(result.keys()):
            result_dict[column] = row[index]
        job.append(result_dict)
    return job
    
   