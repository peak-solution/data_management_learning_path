# Developing ASAM ODS External Data Services

Developing an External Data Service (ExD Service) starts with getting the gRPC definition file (.proto file) from the [ASAM GitHub repository](https://github.com/asam-ev/ASAM-ODS-Interfaces). Use the gRPC tools to generate the initial server code from the .proto file. The gRPC tools support many different programming language and you best choose a programming languages which already provides a library for the file or data format you want to create your ExD Service for.

The ease-of-use and rich eco system makes Python a popular programming language for writing gRPC services and you can find some examples of Python based ExD services like the [MDF4 ExD Service](https://github.com/peak-solution/asam_ods_exd_api_mdf4/blob/main/README.md) here or in the [totonga GitHub repository](https://github.com/totonga/).

Please note, that once you're done programming your ExD-Service, it must be registered with the ASAM ODS Server and the according import service to make your data show-up in an ASAM ODS server eventually.

## License

Copyright © 2024 [Peak Solution GmbH](https://peak-solution.de)

The training material in this repository is licensed under a Creative Commons BY-NC-SA 4.0 license. See [LICENSE](../LICENSE) file for more information.