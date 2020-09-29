# Project Description

This is GUI Automation Framework designed using selenium web driver , python unit test , python pandas and HtmlTestRunner to verify google search functionality.

## Software Requirement

|  Name        |  Version      |
|--------------|---------------|
|Python        | 3.8.5         |
|Chrome        | 85.0.4183.121 |

Please install chrome driver if given driver is not compatible from [driver](https://sites.google.com/a/chromium.org/chromedriver/downloads)
Please store the driver under "drivers" directory

## Python Libraries

| library Name  |  Version |
|---------------|----------|
| pandas        | 1.1.2    |
| requests      | 2.24.0   |
| selenium      | 3.141.0  |
|html-testRunner| 3.141.0  |

## Pip installation :

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install python libraries.

Pandas

```bash
pip3 install pandas --no-build-isolation
```
Selenium
```bash
pip install selenium
```
requests

```bash
pip install requests
```
html-testRunner

```bash
pip install html-testRunner
```


## Starting Execution

1.Clone git repository

```bash
git clone https://github.com/shraddhargupta/relayr.git
```
2.Open command prompt and go to project location

3.Execute below command
```bash
python test/driver_script.py
```
4.After Execution Results will be stored under reports directory.

## Folder Structure

1.**test** : This folder contains file "driver_script.py" which will start execution
2. **reports**:This folder will store all html results generated .
3. **testdata**: This folder contains test data file "Driver.csv".
4. **drivers**: This folder contains web driver for browsers .
5.**config details**: config file stores all configuration related.
6. **screenshots** : This folder will store screenshots if any

## Future Enhancements
1.Webobject / elements will be stored in separate file.
2.Cross Browser Testing: Config based browser will be incorporated.
3.Reporting : More advance reporting can be implemented by providing customize HTML results.
4.Exception Handling:Currently project has very limited exception handling in place.
5.Headless Browser :This can be used For faster and unmonitored execution
```