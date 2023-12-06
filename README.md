# Hackernews
<div align="center">
<img width="30%" src="https://uploads-ssl.webflow.com/5e5e26b57a149fc28773c703/5eaf3dc2f728bb4e333a1546_hacker-news-logo.jpeg">
</div>


### Description
A django application that gets data from hackernews api and store to its database periodically. Incluciding basic fetures peovided through the api endpoint. With a vue + typescript frontend to display the data & TailwindCSS for styling.


# Features
 - A Django rest framework api for
    - Displaying latest stories
    - Filtering stories
    - Searching stories
    - Getting a particular story
    - Creating, Deleting, Updating Stories
 - Scheduled new story update with django-apscheduler
 - Storing stories and comments to the database


# Code Walkthrough
## Backend
#### **backend/task.py**
**fetch_story(story_id):** Fetches individual story data from Hacker News API and updates the Django database with the story details.

**fetch_top_stories_and_comments():** Gets each individual story id, invokes fetch_story() to process each story, and stores them in the database.
backend/views.py

**fetch_comment(story_data, comment_id):** Fetches the comments if kids are available in stories, Also stores the associated story as the parent parameter of the comment creating a **One -- many relationship**

**start(request)**: Initiates a background scheduler that triggers the fetching of Hacker News stories.

### Management/commands
**task_runner.py:**
This file helps run the scheduler task present in task.py at the beginning of the server automatically, with additional aid from -
+ __init__.py
+ apps.py
  
### API Endpoints:
**LatestStoriesView:** Retrieves the latest stories from the database.

**FilteredStoriesView:** Retrieves filtered stories based on categories.

**StorySearchView:** Allows searching for stories using specific keywords.

**StoryDetailView:** Retrieves, updates, or deletes individual stories.(it allows only the deleting and updating of personally created stories)

### Usage
**StoryDetailView:** This also provides enpoint in the URL pattern stories/<int:pk>/ corresponding to this view and handles GET, POST, PUT, and DELETE HTTP requests for a specific story based on its primary key (pk).
Retrieving a Story (GET request):
Send a GET request to retrieve a specific story by its ID:

http
Copy code
GET /stories/<story_id>/
This will return the details of the story with the specified ID.

Creating a Story (POST request):
Send a POST request with the necessary data to create a new story:

http
Copy code
POST /stories/
Content-Type: application/json

{
  "title": "New Story Title",
  "by": "Author",
  "descendants": 0,
  "score": 0,
  "text": "Story content",
  "time": "2023-12-31T00:00:00Z",
  "type": "story",
  "created_in_api": true
}
This will create a new story with the provided details.

Updating a Story (PUT request):
Send a PUT request with the updated data to modify an existing story:

http
Copy code
PUT /stories/<story_id>/
Content-Type: application/json

{
  "title": "Updated Story Title",
  "by": "New Author",
  "text": "Updated story content"
  ...
}
This will update the details of the story with the specified ID.

Deleting a Story (DELETE request):
Send a DELETE request to remove a story:

http
Copy code
DELETE /stories/<story_id>/

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
npm install 
```

#

### Running the App's Backend


--> To run the App, we use :
```bash
npm run dev


```

> ⚠ Then, the development server may be started at http://127.0.0.1:5173/

## Recommended IDE Setup

- [VS Code](https://code.visualstudio.com/) + [Volar](https://marketplace.visualstudio.com/items?itemName=Vue.volar) (and disable Vetur) + [TypeScript Vue Plugin (Volar)](https://marketplace.visualstudio.com/items?itemName=Vue.vscode-typescript-vue-plugin).





#
## Todo
* make it stop running immediately all the task for that job has been recieved