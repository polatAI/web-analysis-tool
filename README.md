Tools and Features

There are two tools in the folder.

Tool: analysis-tool.py
This tool performs the main operations we discussed. To run this tool, insert your API key into the API Key section in the source code, and then execute the tool.
Once the tool is running, it will prompt you to provide a list of domain names. After you provide the list, it will perform detailed analysis, website traffic, and subdomain detection for each domain in the list, and save the results in separate files.

Tool: site-searcher.py
This tool performs two operations:

It takes the domain names from the list you provide and lists 40 similar websites for each domain, saving them in a file.
It calls the API to list high-engagement websites related to the keywords you provide, saving them in a file. For example, if the keyword is "bitcoin," it will list 100 websites related to bitcoin.
Running the Tools

Your domain list, keyword list, and other requirements should be in the same folder as the tools.

The results will be saved in a file within the folder where the tools are located.

To run the tools, open the command prompt and navigate to the folder where the tools are located.

You can use the command "python3 analysis-tool.py" for the first tool, or "python3 site-searcher-2.py" for the second tool.

The tools have been localized and improved. Thank you!

Note: Make sure to place your API key in the respective API Key section in the source code; otherwise, the tools will not work correctly.

Feel free to reach out to me if you have any issues.



DEVELOPER: SEYFULLAH POLAT# web-analysis-tool
It is a tool that allows you to make a detailed analysis about a website. Web traffic, region, revenue etc.
