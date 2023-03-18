from sqlalchemy import create_engine, text
import os, json



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

def load_job_from_db(id):
  with engine.connect() as conn:
    result = conn.execute(
      text("SELECT * FROM jobs WHERE id = :val"),
      {"val":id}
    )
    rows = result.mappings().all()
    if len(rows) == 0:
      return None
    else:
      return dict(rows[0])

def add_application_to_db(job_id, data):
  with engine.connect() as conn:
    query = text("INSERT INTO applications (job_id, fullname, email, linkedin, education, work_experience, resume_url ) VALUES(:job_id, :fullname, :email, :linkedin, :education, :work_experience, :resume_url)")
    conn.execute(query, {"job_id": job_id, **data})