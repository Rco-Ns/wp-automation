# wp-automation
This repo is for submiting exercise Software Engineer Development in Test.

## Setup 
1. first you must install python on your local machine.
2. after python installed then install selenium in python `pip install selenium`
3. download browser driver, example i use chrome driver [chrome-driver](https://selenium-python.readthedocs.io/installation.html#drivers)

## How to run
### Exercise 1 Scenario 1
1. cd `exercise-1-scenario-1`
2. run `python scenario1.py`

### Exercise 1 Scenario 2
1. cd `exercise-1-scenario-2`
2. run `python scenario2.py`

### Exercise 2
1. cd `exercise-3`
2. before we started please change some value in variabels in file `module.py`
```
username = "your-github-username" // change with your username github
pwd = "your-github-password" // change with your password github
myGistsURL = "https://gist.github.com/your-gists-url" // change with your gists URL
gitHubURL = "https://github.com/login"
```
#### 1. Add Gists
run `python test_add_gists.py`

#### 2. Delete Gists
run `python test_delete_gists.py`

#### 3. Get List Gists
run `python test_get_my_gists.py`
