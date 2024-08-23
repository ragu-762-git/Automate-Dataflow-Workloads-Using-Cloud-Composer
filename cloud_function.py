from googleapiclient.discovery import build

def trigger_df_job(cloud_event,environment):   
 
    service = build('dataflow', 'v1b3')
    project = "bold-landing-432711-u5"

    template_path = "gs://dataflow-templates-us-central1/latest/GCS_Text_to_BigQuery"

    template_body = {
        "jobName": "load-cric-data-to-bq-from-gcs",  # Provide a unique name for the job
        "parameters": {
        "inputFilePattern": "gs://crci-api-project-bkt/*.csv",
        "JSONPath": "gs://crci-api-project-bkt-metadata/schema.json",
        "outputTable": "bold-landing-432711-u5:cricket_dataset.icc_test_player_ranking",
        "bigQueryLoadingTemporaryDirectory": "gs://crci-api-project-bkt-metadata",
        "javascriptTextTransformGcsPath": "gs://crci-api-project-bkt-metadata/transform.js",
        "javascriptTextTransformFunctionName": "transform"
    }
    }

    request = service.projects().templates().launch(projectId=project,gcsPath=template_path, body=template_body)
    response = request.execute()
    print(response)
