# ChainSentinel Endpoint Example
A very simple Flask endpoint to use as ChainSentinel example.

ChainSentinel app and documentation can be found at [ChainSentinel.co](https://www.chainsentinel.co).

## Usage
Requires: Python3, Pipenv

### Pipenv
Run `pipenv install` on this application folder to install a virtual environment with the required packages.
Run `pipenv shell` to spawn a shell inside the virtual environment.

### Flask
Set the `FLASK_APP` environmental variable: `export FLASK_APP=endpoint.py`
(optional) Set the Flask environment to development: `export FLASK_ENV=development`
Run the Flask application: `flask run`

### Expose the application
Expose the application either by deploying it (for instance at Heroku) or simply using a tool such as [LocalTunnel](https://www.npmjs.com/package/localtunnel).

### ChainSentinel
Create an account on [ChainSentinel.co](https://www.chainsentinel.co).
Create a new hook for you NEO Smart Contract and set the application as the endpoint.
ChainSentinel will attempt to authenticate your application and if everything is working, it will succeed.
If ChainSentinel listens to an event from your SmartContract, the endpoint will be called with the event data.
