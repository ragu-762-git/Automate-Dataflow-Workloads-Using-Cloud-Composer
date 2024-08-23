# Composer_Pipelines
This repository contains all the pipeline experiments that are to be practiced in GCP which includes the workflow orchestration.

Steps:
1. extract_and_push_gcs.py - Extract the data from the Cricbuzz api and load it into gcs bucket as csv file
2. dag.py - DAG runs the script extract_and_push_gcs.py every day 

3. cloud_function.py - once the csv file hits the gcs bucket, the event arc triggers the cloud function, which starts the dataflow template (Text files on GSC to BigQuery)

4. The transformation happens in the dataflow itself using the transform.js file. 
5. The dataflow job reads the schema.json file to refer it to the BQ table
