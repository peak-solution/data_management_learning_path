# Use Notebooks in Microsoft Visual Studio Code

[Microsoft Visual Studio Code](https://code.visualstudio.com/) is a great tool to work with Notebooks on your desktop.

You can either clone the whole repository or download a specific Notebook
![Download Notebook](/images/download_jpynb.png)

To execute Notebooks in your Microsoft Visual Studio Code environment, install the respective *Python Data Science extension pack*
![Install Jupyter Extension](/images/vs_extension.png)

Once installed you can modify and execute Notebooks, change the contained Python code, add new code and documentation cells, re-run the Notebook, explore and visualize DataFrames, ...

And in case you have a valid Copilot license you'll also get your AI assistant.

[Use Notebooks in GitHub Codespaces](codespaces.md) to get the same experience in the cloud - check it out!

Note: When a Notebook has been completely executed, the connection to the ASAM ODS server will be closed (see last code cell). To re-run a specific code cell either re-run the code cell containing the `con_i = ConI(url=...` or consider "Execute Above Cells" in the code cell menu.
