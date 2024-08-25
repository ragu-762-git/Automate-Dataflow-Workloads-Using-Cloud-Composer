import http.client
import csv
import json
from google.cloud import storage

# Set up the connection
conn = http.client.HTTPSConnection("cricbuzz-cricket.p.rapidapi.com")

headers = {
    'x-rapidapi-key': "1c9bd77dd6msha7445dbef538a90p164282jsn04f94d01c36c",
    'x-rapidapi-host': "cricbuzz-cricket.p.rapidapi.com"
}

# Make the request
conn.request("GET", "/stats/v1/rankings/batsmen?formatType=test", headers=headers)

# Get the response
res = conn.getresponse()
cric_data = res.read()

# Check the response code
if res.status == 200:
    print("Data fetched successfully")

    # Decode the data and parse it as JSON
    json_data = json.loads(cric_data.decode("utf-8"))
    data = json_data.get('rank', [])  # Extracting the 'rank' data
    csv_filename = 'batsmen_rankings_test.csv'

    if data:
        field_names = ['rank', 'name', 'country']  # Specify required field names

        # Write data to CSV file with only specified field names
        with open(csv_filename, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=field_names)
            #writer.writeheader()  # Write header row
            for entry in data:
                writer.writerow({field: entry.get(field) for field in field_names})

        
        bucket_name = "crci-api-project-bkt"
        storage_client = storage.Client()
        bucket = storage_client.bucket(bucket_name=bucket_name)
        destination_blob_name = f'{csv_filename}'

        blob = bucket.blob(destination_blob_name)
        blob.upload_from_filename(csv_filename)

        
        
        
        print(f"Data written to '{csv_filename}'and upload to the GCS bucket {bucket_name} as {destination_blob_name}")
    else:
        print("No data available from the API.")

else:
    print(f"Failed to fetch data. Status code: {res.status}")

# Close the connection
conn.close()


