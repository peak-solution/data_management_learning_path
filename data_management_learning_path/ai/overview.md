# Work with AI: ODSBox-AIConnect Overview

## What is ODSBox-AIConnect?

**ODSBox-AIConnect** is a Model Context Protocol (MCP) service that enables AI-assisted workflows for working with ASAM ODS data. It's built on top of the [odsbox-jaquel-mcp](https://github.com/totonga/odsbox-jaquel-mcp) project and integrates seamlessly with VS Code's Copilot Chat, allowing you to use natural language to explore, query, and analyze ASAM ODS data.

## How It Works

Rather than manually writing complex queries and analysis scripts, you can:

1. **Connect to your ASAM ODS server** — Provide connection details or use environment variables
2. **Ask questions in plain English** — Use VS Code Copilot Chat to explore your data
3. **Generate code and analysis workflows** — Let AI assist in creating Jupyter notebooks, Python scripts, and data visualizations
4. **Verify and refine results** — Review generated code and prompts for accuracy

## Key Features

- **Schema Inspection** — Explore available entities, relationships, and data structures
- **JAQueL Query Assistance** — Build, validate, and explain ASAM ODS queries using natural language
- **Data Access & Analysis** — Retrieve timeseries and submatrix data with AI-guided workflows
- **Code Generation** — Automatically generate Python scripts for bulk data fetching and visualization
- **Measurement Comparison** — Generate Jupyter notebooks for comparing measurements and analyzing correlations



## Learning Path

### 📘 Simple Data Interaction
Start here to understand the basics: [Simple Data Interaction](01_simple_data_interaction.md)

Learn how to connect to an ASAM ODS server and ask AI-powered questions about your data.

### 📊 Creating Analysis Notebooks
Next, create reproducible analysis workflows: [Creating Analysis Notebooks](02_simple_analysis_notebook.md)

Use AI to generate Jupyter notebooks for thermal analysis or other measurement comparisons.

### 🎨 Creating Analysis Applications
Finally, build interactive applications: [Creating Analysis Applications](03_simple_analysis_application.md)

Leverage AI to create simple Python applications with user interfaces for data exploration and visualization.

## Example Use Cases

- **Data Exploration** — Quickly understand what data is available in your ASAM ODS server
- **Query Development** — Generate JAQueL queries using natural language descriptions
- **Performance Analysis** — Compare measurements and identify correlations with AI assistance
- **Report Generation** — Create Jupyter notebooks for automated reporting and analysis
- **Data Migration** — Understand data models and generate migration scripts

## Resources

- **[odsbox-jaquel-mcp GitHub](https://github.com/totonga/odsbox-jaquel-mcp)** — Full project documentation and advanced usage
- **[MCP Playground Examples](https://github.com/peak-solution/asam_ods_mcp_playground)** — Installation, configuration, and reference implementations
- **[ASAM ODS Standard](https://www.asam.net/standards/detail/ods/)** — Official ASAM ODS documentation

## Next Steps

Ready to get started? Head to [Simple Data Interaction](01_simple_data_interaction.md) to begin your first AI-assisted ASAM ODS workflow!

---

**License:** Creative Commons BY-NC-SA 4.0  
**Based on:** [odsbox-jaquel-mcp](https://github.com/totonga/odsbox-jaquel-mcp) by totonga
