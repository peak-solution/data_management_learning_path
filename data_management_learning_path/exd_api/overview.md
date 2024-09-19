# EXD-API Plugins Overview

The conversion of legacy data into standard data formats often requires data conversion. This can lead to an increased volume of data due to data copies and to an interruption of existing tool chains that use this data.

To avoid these conflicts, ASAM ODS has introduced the *External Data API* with version 6.2. The *External Data API* enable access to legacy data through microservices that expose the metadata and mass data they contain we call such a service an *EXD-API Plugin*.

As a member of the ASAM ODS working group, Peak Solution was significantly involved in the definition of *External Data API* and the Peak ASAM ODS Server has supported the *External Data API* from the very beginning.

## Working principle of ASAM ODS EXD-API Plugins

EXD-API Plugins exchange data via the [Google gRPC protocol](https://grpc.io/).

The data provided by the EXD-API Plugin splits into two different operations: meta data retrieval (GetStructure) and bulk/channel data retrieval (GetValue). The meta data is returned in form of name-value pairs and is used to provide descriptive and semantic information about the data and so offering extended searching capabilities.

![EXD-API Plugin calling sequence](/images/ExternalData.png)

Looking at a typical calling sequence, you can see that once a new file (or data item) has been detected (1), the  EXD-API Plugin is called (GetStructure) by the importer to deliver the meta data of that specific file (2). The EXD-API Plugin then reads the file (3), creates the return structure (4) and returns the requested data (5).
One part of the returned meta data - often in combination with the file and the folder name - is then being used to identify and create the data context, respective the needed data hierarchy (6).
The other part is then being used to create the data structure in the server for receiving the bulk/channel data in subsequent calls and for (optionally) providing the file for download (7).

Now all needed data and information is available in the ASAM ODS server, such that clients can start using the data.
To do so, they connect to the ASAM ODS server (8) and typically start explore the hierarchical data structure (9) until the point is reached accessing the actual channel data (10).

To access the channel data, the ASAM ODS server delegates the client call to the EXD-API Plugin (11) by calling GetValue - including information about the file and the channel(s) in request. The EXD-API Plugin use this information to open the file, retrieve the data (12) and return it to the ASAM ODS Server (13) which relays it back to the client (14). From the client perspective there is no difference between a call directly handled by the ASAM ODS server or delegated to an EXD-API Plugin.

## License

Copyright © 2024 [Peak Solution GmbH](https://peak-solution.de)

The training material in this repository is licensed under a Creative Commons BY-NC-SA 4.0 license. See [LICENSE](../LICENSE) file for more information.
