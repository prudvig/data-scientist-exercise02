## RTI CDS Analytics Exercise 02

Welcome to Exercise 02. This exercise provides data from the [National Transportation Safety Board](http://www.ntsb.gov/Pages/default.aspx)'s [database of aviation accidents](http://www.ntsb.gov/_layouts/ntsb.aviation/index.aspx). We'll ask you to perform some routine high-level analytic tasks with the data. 

### Using the Code

If you wish to submit via GitHub:
1. Fork this repository to your personal GitHub account and clone the fork to your computer. If you've received this repo as a zip file, ignore
    - **Note**: This does mean you will have a visible public fork of this repo on your github account.
2. Save and commit your answers to your fork of the repository, and push them back to your forked repository. Include code and writeup.
3. Provide a link to that fork of the repository in your submission.

If you wish to submit via an emailed zip file:
1. Clone this repository or download the code as a zip file (see image below)
2. Extract this repo (if downloaded as zip) and work locally with the code.
3. When finished, zip your project folder (code and writeup) and submit to the email you received the exercise from.

<img src="https://i.postimg.cc/KzwCd2Mg/Screen-Shot-2021-12-27-at-9-05-31-AM.png" alt="Downloading A Repo as a ZIP file" width="350">


### Some guidance

1. Use open source tools and ecosystems - Python or R. Do not use proprietary tools, such as SAS, SPSS, JMP, Tableau, or Stata. 
2. Use the Internet as a resource to help you complete your work. We do it all the time.
3. Comment your code such that a fellow data scientist who isn't familiar with this data or analysis could understand the steps you take.
4. There are many ways to approach and solve the problems presented in this exercise. 
5. For language specific information on how to read in XML and JSON files, use your favorite search engine.

### The Task

You will be exploring the data to develop a classification of narratives and writing up a summary of the data and your results. **The whole exercise should take no longer than 4 hours (self-timed)**.

Your **code** needs to perform the following tasks:
1. Read and standardize the json files in a way that facilitates further analysis (i.e. "flatten" them and link with `AviationData`)
2. Prepare descriptive statistics that convey an overview of the structured data.
3. Perform initial exploratory analysis of the narrative text, analyzing the use of words over time.
4. Use topic modeling or any other text clustering methodology to cluster/group the incidents based on the narrative text and/or probable cause descriptions. Come up with a short name for each topic or cluster you identify to make it easy to report on.
5. Create a chart that you feel conveys one important relationship in the data.

Your **writeup** should do the following:
1. Describe your methodology and results in 500 words or less.
  - Include the chart generated as of your write-up. Explain how the chart informs your analysis. 
  - You'll not be punished for going over 500 words, but it is a rough guideline of the length we expect.
2. Include a chart that you feel conveys one important relationship in the data.


_Additional Context:_

* Assume the audience for your write-up is a non-technical stakeholder. 
* Assume the audience for your code is a colleague who may need to read or modify it in the future. 

### The Data

There are 146 files in this repository (`data/`):

- `AviationData.xml`: This is a straight export of the database provided by the NTSB. The data has not been altered. It was retrieved by clicking "Download All (XML)" from [this page on the NTSB site.](http://www.ntsb.gov/_layouts/ntsb.aviation/index.aspx)
- `AviationData.csv`: This is a CSV version of the XML above, pre-converted to a tabular format so that it's easier to work with for this analysis. The script used for conversion is `parse_xml.py`

There are 144 files in the following format:

- `NarrativeData_xxx.json`: These files were created by taking the `EventId`s from `AviationData.xml` and collecting two additional pieces of data for each event: 
  - `narrative`: This is the written narrative of an incident.
  - `probable_cause`: If the full narrative includes a "probable cause" statement, it is in this field. 
