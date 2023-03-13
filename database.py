from  sqlalchemy import create_engine, text

db_connection_string ="mysql+pymysql://darze6ylcmfbn0ed7zj2:pscale_pw_cc70S7xieHOVesMxuOYJfnVHsOK6QAlkkDKfOUsxHCO@us-east.connect.psdb.cloud/lamscareers?charset=utf8mb4"

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
      query = text('select title,location,salary from jobs')
      result = conn.execute(query)

    # Iterate through the rows and convert them to dictionaries
    jobs = []
    for row in result.fetchall():
        result_dict = {}
        for index, column in enumerate(result.keys()):
            result_dict[column] = row[index]
        jobs.append(result_dict)
        return jobs
      