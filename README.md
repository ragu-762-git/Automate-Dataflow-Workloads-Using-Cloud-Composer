Project Description:

The DAG is set to extract bastsmen ranking from the cricbuzz api on every day morning 6 am and load the CSV file into GCS bucket. Once the file hits the bucket, the Event arc trigger executes the cloud function which is set to trigger a dataflow job. The job transforms the data to JSON strings format to write it into BigQuery after imposing the provided schema. 

Steps:
1. extract_and_push_gcs.py - Extract the data from the Cricbuzz api and load it into gcs bucket as csv file
2. dag.py - DAG runs the script extract_and_push_gcs.py every day morning 6 am.
3. cloud_function.py - once the csv file hits the gcs bucket, the event arc triggers the cloud function, which starts the dataflow template (Text files on GSC to BigQuery)
4. The transformation happens in the dataflow itself using the transform.js file. 
5. The dataflow job reads the schema.json file to refer it to the BQ table.
6. The cloud composer executes the DAG through the managed cloud composer environment. 

Note: The cloud function python file version - 3.8 

Room for improvement:
1. Since the DAG is scehduled daily, the current cloud function just overwrites the data in BQ table; instead we can append the data to BQ.
2. It is not necessary the schema of the data can be same on everyday ; so generalize the code to create the schema and create the table if not exists. We can provide the possible set of schemas on the .YAML file and we can write the data to BQ table only if the schema of the file matches any of the schemas from the .YAML file predefined by us. 
3. The current DAG is performing only one task (operator). We can increase the number of tasks performed by the DAG.
4. Instead of using the job template provided by the Dataflow itself, we can define our own pipeline's source, transformations in Apache Beam and sink and make this as a task for a DAG. 
