# Creating Analysis Notebooks with AI

In this guide, you'll use AI-powered Copilot Chat to automatically generate Jupyter notebooks for measurement analysis. This is ideal for creating reproducible workflows like thermal analysis, crash analysis, or performance comparisons.

## Overview

This playground demonstrates:
- Using AI to design analysis workflows
- Generating complete Jupyter notebooks
- Running analysis and generating visualizations
- Saving notebooks for reproducibility and sharing

## Step 1: Define Your Analysis Goal

First, determine what analysis you want to perform. Some examples:

- **Thermal Analysis** — Compare temperature measurements across test campaigns
- **Performance Comparison** — Analyze acceleration or efficiency metrics
- **Data Quality Check** — Identify anomalies or missing values
- **Correlation Analysis** — Find relationships between different measurements

## Step 2: Ask Copilot to Create a Notebook

In Copilot Chat, describe your analysis goal:

```
I want to create a thermal analysis of measurements from test campaign 'Campaign_01'. 
Show temperature trends and identify peak values.
```

Copilot will:
1. Ask clarifying questions (e.g., date range, temperature thresholds)
2. Generate a complete Jupyter notebook with:
   - Connection setup code
   - JAQueL queries to retrieve data
   - Data cleaning and preprocessing
   - Analysis and visualization code
   - Statistical summaries

## Step 3: Review and refine the Generated Notebook


If the generated notebook needs adjustments, provide feedback:

```
Add a second plot comparing temperature from two different test campaigns
```

```
Include error handling for cases where data is missing
```

```
Add a summary table with statistics for each measurement
```

Copilot will update the notebook accordingly.


## Tips & Best Practices

1. **Be descriptive** — Provide context about your data and analysis goals
2. **Start simple** — Begin with basic analysis, then add complexity
3. **Verify queries** — Have Copilot explain generated JAQueL queries before execution
4. **Test on small data** — Use `$rowlimit` to test queries on a subset first
5. **Document assumptions** — Add markdown cells explaining data filters and calculations
6. **Version control** — Commit notebooks to Git for tracking changes

## Next Steps

- **Build Applications:** Use analysis workflows as a foundation for [Creating Analysis Applications](03_simple_analysis_application.md)
- **Advanced Queries:** Learn more in the [Simple Data Interaction](01_simple_data_interaction.md) guide
- **Explore:** Check out the [odsbox-jaquel-mcp documentation](https://github.com/totonga/odsbox-jaquel-mcp) for advanced analysis techniques

---

**Next:** [Creating Analysis Applications](03_simple_analysis_application.md)
