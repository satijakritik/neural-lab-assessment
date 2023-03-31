# neural-lab-assessment
Implementation of the Neural Lab technical assessment

## Implementation for MacOS

### Testing streamlit

1. Install pipenv
```
pip3 install pipenv
```
2. Create and activate the Pipenv environment in your project directory
```
pipenv shell
```
3. Test streamlit
```
streamlit hello
```
### Running q1

1. Ensure that the 'stats_full_stack_dev.csv' is in the working directory
2. Run the 'fill_time_stamps.py' file to replace the NaN values in the csv file's 'time_stamp' column with dummy values from the past 1hr
```
python3 fill_time_stamps.py
```
3. Activate the virtual environment in the terminal window
```
pipenv shell
```
4. Run q1.py using streamlit
```
streamlit run q1.py
```

### Running q2

1. Activate the virtual environment in the terminal window
```
pipenv shell
```
2. Run the server
```
uvicorn fast_api:app --reload
```
3. Repeat step 1 in a new terminal window
4. Run q2.py using streamlit
```
streamlit run q2.py
```
