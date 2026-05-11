# Creating Analysis Applications with AI

In this guide, you'll use AI-powered Copilot Chat to build interactive Python applications with user interfaces for exploring and analyzing ASAM ODS data. This extends the notebook-based workflows into standalone tools.

## Overview

This playground demonstrates:
- Designing application architecture with AI
- Generating complete Python applications with UI frameworks
- Creating interactive dashboards and data exploration tools
- Deploying applications for team use

**Time to complete:** 30-45 minutes

## Recommended Frameworks

For interactive applications, consider these frameworks:

- **Streamlit** — Simple, rapid UI development with Python (recommended for beginners)
- **Dash** — More advanced dashboards and web applications
- **PyQt / Tkinter** — Desktop applications with rich UI

This guide focuses on **Streamlit** for its ease of use.

## Step 1: Define Your Application

Determine what your application should do. Examples:

- **Data Explorer** — Browse measurements, filter by criteria, view details
- **Dashboard** — Real-time monitoring of measurement values
- **Analysis Tool** — Run analysis workflows with user-configurable parameters
- **Report Generator** — Create PDF reports from selected data

## Step 2: Ask Copilot to Design the Application

In Copilot Chat, describe your application:

```
I want to build a Streamlit application that lets users:
1. Connect to an ASAM ODS server
2. Browse measurements from a selected test
3. View temperature data with a line chart
4. Compare measurements side-by-side
```

Copilot will:
1. Ask clarifying questions about UI layout and features
2. Suggest library choices (Streamlit, Dash, etc.)
3. Outline application structure
4. Generate complete code

## Step 3: Generate and run Application Code

Copilot will create a Streamlit application structure.
Launch the application:

```bash
streamlit run app.py
```

Streamlit will:
- Start a local development server (usually `http://localhost:8501`)
- Open your application in the default browser
- Auto-reload on code changes

## Step 4: Test and Refine

Interact with your application:
1. **Test all features** — Connect, browse data, create charts
2. **Identify issues** — Note any bugs or missing functionality
3. **Ask Copilot for improvements** — Request UI enhancements or new features

Example refinement requests:

```
Add a date range picker to filter measurements
```

```
Create a comparison view to display two measurements side-by-side
```

```
Add statistics (mean, max, min, std dev) below the chart
```

```
Add login functionality to control data access
```

## Tips & Best Practices

1. **Start small** — Create a minimal working app, then add features
2. **Use session state** — Streamlit sessions persist UI state
3. **Cache expensive operations** — Use `@st.cache_data` to avoid recomputing
4. **Validate inputs** — Check user inputs before querying ASAM ODS server
5. **Handle errors gracefully** — Show user-friendly error messages
6. **Document code** — Add comments and docstrings
7. **Test thoroughly** — Verify all user interactions

## Next Steps

- **Learn more Streamlit** — Visit [Streamlit documentation](https://docs.streamlit.io/)
- **Advanced ODS queries** — Review [odsbox-jaquel-mcp](https://github.com/totonga/odsbox-jaquel-mcp) documentation
- **Share your app** — Deploy and share with your team
- **Extend functionality** — Add databases, APIs, or other integrations

---

**Congratulations!** You've completed the AI playground series. You now have skills to:
- Explore ASAM ODS data interactively
- Generate analysis notebooks with AI
- Build standalone applications

**Next steps:** Explore the [odsbox-jaquel-mcp GitHub](https://github.com/totonga/odsbox-jaquel-mcp) for advanced techniques and the [MCP Playground](https://github.com/peak-solution/asam_ods_mcp_playground) for more examples.
