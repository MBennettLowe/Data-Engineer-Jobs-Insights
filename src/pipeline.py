import dlt
import pandas as pd

def kaggle_source():
    df = pd.read_csv("/workspaces/Data-Engineer-Jobs-Insights/data/raw/data_engineer_jobs/DataEngineer.csv")
    
    for record in df.to_dict(orient="records"):
        yield record

# Pipeline with automatic normalization
pipeline = dlt.pipeline(
    pipeline_name="kaggle_pipeline",
    destination="duckdb",
    dataset_name="jobs_data"
)

# Run the pipeline
info = pipeline.run(kaggle_source(), table_name="jobs")

# Print the load data
print(info)