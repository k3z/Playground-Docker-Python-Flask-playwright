# Pyton Flask APP boilerplate

This is a simple Python Flask app boilerplate.

## Prerequisite

- Python 3.11.x

## Install on MacOs and Linux like

The recommended way to work with this app is to use Docker. Please refer to the README in the project folder root. If you prefer not to use Docker, follow the steps below:

1. Open a terminal and navigate to the project directory.
2. Create a virtual environment using the following command:

```
python3 -m venv venv1
```

3. Activate the virtual environment:

```
source venv1/bin/activate
```

4. Install the required Python packages:

```
pip install -r requirements.txt
```

## Starting the App

If you are not using Docker, make sure the virtual environment is activated before starting the app.

To start the flask service, run the following command:

```
cd ./
source venv1/bin/activate
```

## Start flask service.

```
flask --app app run
```

Output

```
 * Serving Flask app 'app'
 * Debug mode: off
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on http://127.0.0.1:5000
```

Go to http://127.0.0.1:5000

Output

```
Hello World
```

## Deactivate venv

```
deactivate
```
