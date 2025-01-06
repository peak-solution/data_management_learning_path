# Developing ASAM ODS EXD-API Plugins

Developing an EXD-API Plugin starts with getting the gRPC definition file (.proto file) from the [ASAM GitHub repository](https://github.com/asam-ev/ASAM-ODS-Interfaces). Use the gRPC tools to generate the initial server code from the .proto file. The gRPC tools support many different programming language and you best choose a programming languages which already provides a library for the file or data format you want to create your ExD Service for.

The ease-of-use and rich eco system makes Python a popular programming language for writing gRPC services and you can find some examples of Python based EXD-API Plugins like the [MDF4 EXD-API Plugin](https://github.com/peak-solution/asam_ods_exd_api_mdf4/blob/main/README.md) here or in the [totonga GitHub repository](https://github.com/totonga/).

Please note, that once you're done programming your EXD-API Plugin, it must be registered with the ASAM ODS Server and the according import service to make your data show-up in an ASAM ODS server eventually.

## License

Copyright © 2025 [Peak Solution GmbH](https://peak-solution.de)

The training material in this repository is licensed under a Creative Commons BY-NC-SA 4.0 license. See [LICENSE](../LICENSE) file for more information.
