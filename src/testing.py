import duckdb

# connect to your DuckDB file
con = duckdb.connect("/workspaces/Data-Engineer-Jobs-Insights/src/kaggle_pipeline.duckdb")

# show tables
print(con.execute("SELECT COUNT(*) FROM jobs_data.jobs").fetchall())