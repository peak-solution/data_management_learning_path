# Peak ODS Adapter for Apache Spark

The Peak ODS Adapter for [Apache Spark](https://spark.apache.org/) allows you to interact with [ASAM ODS](https://www.asam.net/standards/detail/ods/wiki/) data using Spark SQL and DataFrames.

Furthermore, the Peak ODS Adapter for Apache Spark also allows to export your data to the big data world by providing the ASAM ODS Big Data Connector functionalities to you. 

![Powered by Apache Spark](/images/Spark.png)

## Overview

The Peak ODS Adapter for Apache Spark allows exporting ASAM ODS instance and measurement (mass) data in a format suitable for big data analysis tools in the ways defined by the ASAM ODS standard: AVRO/JSON for instance data and Parquet for mass data.

However, the Peak ODS Adapter for Apache Spark allows using all build-in Spark Data Sources for writing, so you're free to choose the most suitable format for your application.

NOTE::
Don't get confused with Data Source formats. The Peak ODS Adapter for Apache Spark defines the ODS connectivity as a Data Source format like all other Spark Adaptors. So you use the Peak ODS Adapter for Apache Spark Data Source formats to get the data into the Spark DataFrame (`read`) and the other Spark Data Source formats for exporting the DataFrame (`write`).

## Export ODS Big Data

Exporting data according to the ASAM ODS Big Data standards is a two step approach:

- First you "select" the data to be loaded from the Peak ODS Server.
- Then you specify how your Spark DataFrame is stored.

The next two sections will describe in more detail how to do this for instance data and mass data.

### Read Instance Data using an Export Definition File

To read instance data according to the ASAM ODS Big Data Connector standard, define "mappedodsinstances" as Data Source format.

Define the export definition file by specifying the file name as "mappingrulefile" option.

Define a specific rule of the Export Definition File to be executed - in our example "MeaResultExport".

```python
df = spark.read.format("mappedodsinstances")\
    .options(**odsOptions)\
    .option("mappingrulefile","mdmexportdefinition.xml")
    .load("MeaResultExport")
```

NOTE::
Within an ASAM ODS Export Definition File you can select which attributes of a certain entity to be loaded, you can map the attribute to a different name (alias) and you can implicitly join other entities of your data model (schema).

After loading the data you can export the data to Avro:

```python
df.write.format("avro").save("mearesult.avro")
```

NOTE::
You can also write to Avro using the "odsinstance" Data Source format of the Peak Spark ODS Adapter.

### Read ODS measurement (mass) data

Use the "ods" format as Data Source, to load measurement data.

Depending which measurements you load, your DataFrame will contain different measurement quantities and thus different columns.

In addition, the DataFrame will contain a special column "idref" which contains a globally unique identifier to identify the measurement to which the values of the actual row belong - which is especially useful in case several measurements are contained in the same DataFrame.

You can additionally load the data as binary (packed) and in chunks (to avoid big blobs) as well as treating column (local column) names as "case sensitive":

```python
df = spark.read.format("ods")\
    .options(**odsOptions)\
    .option("mode", "packed")\
    .option("maxChunkCount", 10000)\
    .option("caseSensitive", "true")\
    .load("where MeaResult.Id = 3")
```

After loading the data you can export the data to Parquet:

```python
df.write.parquet("mearesult_id_3")
```