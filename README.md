# estat: Electricity Statistics

A learning project electricity meter readings are recorded and used for all kinds of statistics.

## Installing local environment

You need to have postgresql installed, with a DB and user a password configured like in the postactivate file, found in the settings directory

1. Create a virtual environment in your project directory

        python -m venv estat

2. Copy geckodriver in the bin directory of the virtual environment.
   Get geckodriver for firefox from: https://github.com/mozilla/geckodriver/releases
3. Put in place the postactivate

        cp estat/estat/settings/postactivate /bin

4. Fill in your DB name, user and passwd

        vim bin/postactivate

5. Activate the virtual environment

        source estat/bin/activate

6. Go to the estat directory and clone the repository

        git clone https://github.com/stevenengelen/estat.git


7. Install the required pip packages

        pip install -r requirements.txt
