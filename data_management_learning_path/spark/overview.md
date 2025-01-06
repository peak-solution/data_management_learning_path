# Peak ODS Adapter for Apache Spark

The Peak ODS Adapter for [Apache Spark](https://spark.apache.org/) allows you to interact with [ASAM ODS](https://www.asam.net/standards/detail/ods/wiki/) data using Spark SQL and DataFrames.

Furthermore, the Peak ODS Adapter for Apache Spark also allows to export your data to the big data world by providing the ASAM ODS Big Data Connector functionalities to you.

![Powered by Apache Spark](/images/Spark.png)

## Overview

The *Peak ODS Adapter for Apache Spark* defines the ODS connectivity as a Data Source format like all other Spark Adaptors. So you use the *Peak ODS Adapter for Apache Spark* Data Source formats to get the data into the Spark DataFrame (`read`).

The *Peak ODS Adapter for Apache Spark* supports three Data Source formats:

* *odsinstances*: Use `format("odsinstances")` to get instance data. The Spark DataFrame you're working on will contains all application attributes as columns and all instances of the loaded entity (application element) as rows.


  **Notebook**: [📓 Work with instance data](Spark_ODS_instance_data.ipynb)

* *ods*: Use `format("ods")` to get measurement (bulk) data. Your Spark DataFrame will contain all channels (MeaQuantities) as columns. When querying data from multiple measurements, it will be concatenated in the DataFrame. The first column in the DataFrame contains the information to which measurement (submatrix) the specific row belongs.


  **Notebook**: [📓 Work with measurement data](Spark_ODS_measurement_data.ipynb)

* *mappedodsinstances*: Use `format("mappedodsinstances")` to read instance data according to the ASAM ODS Big Data Connector standard. With the help of an ASAM ODS Export Definition File you define which attributes of a certain entity to be loaded, you can map the attribute to a different name (alias) and you can implicitly join other entities of your data model (schema).


  **Notebook**: [📓 ASAM ODS Big Data Connector](Spark_ODS_big_data.ipynb)

Note: You can use other Spark Data Source formats, such as for instance `"avro"`, for exporting the DataFrame (`write`).

## Compare Spark DataFrame and Pandas DataFrame

Due to lazy evaluation and an optimized execution plan, Spark DataFrames can cope with massive datasets that exceed the memory potential of a single device and leverage the computing capabilities of Spark. 

On the other side, Spark DataFrames require distributed computing surroundings and cluster configuration, which provides complexity compared to a single-machine solution like Pandas DataFrames.

For a more detailed discussion on the differences between Spark and Pandas DataFrames, see for example: [Difference between Spark DataFrame and Pandas DataFrame](https://www.tutorialspoint.com/difference-between-spark-dataframe-and-pandas-dataframe)

## License

Copyright © 2025 [Peak Solution GmbH](https://peak-solution.de)

The training material in this repository is licensed under a Creative Commons BY-NC-SA 4.0 license. See [LICENSE](../LICENSE) file for more information.
