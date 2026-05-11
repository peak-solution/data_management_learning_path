# Simple Data Interaction with ASAM ODS

In this guide, you'll learn how to connect to an ASAM ODS server and use AI-powered Copilot Chat to explore and ask questions about your data. This is the starting point for understanding your ASAM ODS data structure and content.

## Overview

This playground demonstrates:
- Connecting to an ASAM ODS server
- Querying basic data information
- Using AI to generate queries and understand data
- Exploring the test hierarchy (Tests → Measurements → Data)

## Step 1: Open Copilot Chat

1. Open VS Code
2. Press `Ctrl+Shift+I` to open Copilot Chat panel
3. You should see "ODSBox-AIConnect" available in the tool suggestions

## Step 2: Connect to ASAM ODS Server

In Copilot Chat, type:

```
Connect to ASAM ODS server
```

In case you're not connected yet, Copilot will ask for connection details. You can use the same connection information as in your Jupyter notebooks:

```
url="https://docker.peak-solution.de:10032/api", auth=("Demo", "mdm")
```

Copilot will use the `ods_connect` tool to establish a connection.

## Step 3: Explore Available Data

Once connected, ask Copilot:

```
What kind of data is contained in the server?
```

```
How many measurements are in the latest test campaign?
```

```
Show me the structure of a measurement
```

Copilot will translate your questions into JAQueL queries using the `query_describe` and `query_execute` tools.

## Step 4: Generate a Query

To learn how to write queries yourself, ask:

```
Generate a JAQueL query to find all measurements from test 'Campaign_01'
```

Copilot will:
1. Create a query skeleton using `query_generate_skeleton`
2. Show you the query syntax
3. Explain what the query does in plain English

## Next Steps

- **Data Analysis:** Head to [Creating Analysis Notebooks](02_simple_analysis_notebook.md) to create reproducible analysis workflows
- **Build Applications:** Move to [Creating Analysis Applications](03_simple_analysis_application.md) to build interactive tools
- **Deep Learning:** Review the [odsbox-jaquel-mcp documentation](https://github.com/totonga/odsbox-jaquel-mcp) for advanced techniques

## Tips & Best Practices

1. **Be specific in prompts** — Instead of "analyze the data," try "Find measurements with temperature > 100°C and show statistics"
2. **Ask for explanations** — Use "Explain this JAQueL query" to learn syntax
3. **Verify generated code** — Always review AI-generated queries before executing on large datasets
4. **Use examples** — Reference specific measurement names or test IDs to get more accurate results

## Example Prompts

Use these starting prompts to guide your exploration:

- `What entities are available in the database?`
- `Show me the test hierarchy structure`
- `Find measurements where the stator winding temperature exceeds 100`

---

**Next:** [Creating Analysis Notebooks](02_simple_analysis_notebook.md)
