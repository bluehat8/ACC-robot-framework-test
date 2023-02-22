# *All libraries and frameworks*
pandas
robotframework
robotframework-metrics
Selenium2Library
ScreenCapLibrary
jira

## /*How to install all libraries*/
use pip install [Library-framework name] to intall all libraries

Examples:

pip install robotframework
pip install robotframework-Selenium2Library
pip install robotframework-ScreenCapLibrary
pip install pandas


## *Robotmetrics for html report*

How to use in robotmetrics in project:

# Step 1 Install robotmetrics

**Case 1: Using pip**

pip install robotframework-metrics==3.3.3

***Case 2: Using setup.py (clone project and run command within root)***

python setup.py install

***Case 3: For latest changes use following command (pre-release or changes in master)***

pip install git+https://github.com/adiralashiva8/robotframework-metrics

# Step 2 Execute robotmetrics command to generate report

***Case 1: No change in output.xml file name (assumig user is in same folder)***

robotmetrics

***Case 2: output.xml under 'Result' folder***

robotmetrics --inputpath ./Result/ --output output1.xml

# For more info on command line options use:

robotmetrics --help

