## einthusan-cli
Einthusan CLI tool to extra streaming url. 

## Config
Change `URL` in einthusan-dl.py to use your own `API` server. To deploy your own server please follow the instruction below.

## Deploying to Heroku

[![Deploy](https://www.herokucdn.com/deploy/button.png)](https://heroku.com/deploy)

### Manually

0. Ensure you have the [Heroku toolbelt](https://toolbelt.heroku.com) installed and set-up.

1. Clone this repo: `git clone https://github.com/iphoting/youtube-dl-api-server-heroku`.

2. Provision a Heroku app: `cd youtube-dl-api-server-heroku; heroku create <your-app-name>`.

3. Push to deploy the app: `git push -u heroku master`.

4. Check its runtime logs: `heroku logs`, and status: `heroku ps`.

5. Your API server version is now available at: `https://<your-app-name>.herokuapp.com/api/version`.
