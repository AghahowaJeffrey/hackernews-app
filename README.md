# Hackernews
<div align="center">
<img width="30%" src="https://uploads-ssl.webflow.com/5e5e26b57a149fc28773c703/5eaf3dc2f728bb4e333a1546_hacker-news-logo.jpeg">
</div>


### Description
A django application that gets data from hackernews api and store to its database periodically. With a vue + typescript frontend to display the data & CSS for styling.


# Features
 - A Django rest framework api for
    - Displaying latest stories
    - Filtering stories
    - Searching stories
    - Getting a particular story
    - Creating, Deleting, Updating Stories
 - Scheduled new story update with django-apscheduler
 - Storing stories and comments to the database




### Cloning the repository

--> Clone the repository using the command below :
```bash
git clone https://github.com/AghahowaJeffrey/hackernews-app
```

--> Installing pipenv virtual environment
```bash
pip install pipenv
```

--> Move into the directory where we have the project files : 
```bash
cd hackernews
cd backend

```

--> Create a virtual environment and install needed pages :
```bash
# Let's install needed packages inside the pipenv enviroment
pipenv install 
```

#
### Running the App's Backend


--> To run the App, we use :
```bash
cd backend
python manage.py runserver

```

> ⚠ Then, the development server may be started at http://127.0.0.1:8000/

#
### Running the Frontend App

--> Move into the directory where we have the project files : 
```bash
cd frontend

```

--> Installing all needed Dev Dependencies from package.json :
```bash
pipenv install 
```

#

### Running the App's Backend


--> To run the App, we use :
```bash
npm run start


```

> ⚠ Then, the development server may be started at http://127.0.0.1:8000/

## Recommended IDE Setup

- [VS Code](https://code.visualstudio.com/) + [Volar](https://marketplace.visualstudio.com/items?itemName=Vue.volar) (and disable Vetur) + [TypeScript Vue Plugin (Volar)](https://marketplace.visualstudio.com/items?itemName=Vue.vscode-typescript-vue-plugin).





#
## Todo