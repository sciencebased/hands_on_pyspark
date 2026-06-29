"""Quick check that the Apache Spark 4 environment works end to end.

Run with the project venv active:
    source .venv/bin/activate
    python smoke_test.py
"""

from pyspark.sql import SparkSession


def main() -> None:
    spark = (
        SparkSession.builder.appName("setup-check")
        .master("local[*]")
        .config("spark.ui.enabled", "false")
        .getOrCreate()
    )
    print("Spark version:", spark.version)

    df = spark.createDataFrame([(1, "a"), (2, "b"), (3, "c")], ["id", "label"])
    print("Row count:", df.count())
    df.show()

    spark.stop()
    print("OK: Spark session ran successfully")


if __name__ == "__main__":
    main()
