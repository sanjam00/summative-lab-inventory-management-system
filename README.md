# Inventory Management System (Flask + React)

## Overview

This is a full-stack inventory management single page application (SPA) built with Flask (backend) and React (fronend)
It allows users to manage inventory items and automatically enrich product data using the Open Food Facts API.


## Features

### Backend (Flask)

* RESTful API
* CRUD operations:

  * `GET /inventory` → view all items
  * `GET /inventory/<id>` → view one item
  * `POST /inventory` → add item
  * `PUT /inventory/<id>` → update item
  * `DELETE /inventory/<id>` → delete item
* JSON file used as a simple database
* External API integration (Open Food Facts)
* Automatic product data enrichment (name, brand, ingredients)


### Frontend (React)

* Displays inventory items in a clean and simple UI
* Add new items via form (collapsible)
* Edit existing items
* Delete items
* Search/filter inventory
* Notifications to improve user experience


## Installation & Setup

### Backend setup

```bash
cd server/src
python app.py
```

Backend runs on:

```
http://localhost:5000
```

### 3. Frontend setup

```bash
cd client
npm install
npm run dev   # or npm start depending on setup
```

Frontend runs on:

```
http://localhost:5173
```


## Testing

Basic tests are included using pytest.

Run tests:

```bash
pipenv install
pipenv shell
pytest
```

Tests cover:

* CRUD endpoints
* API responses
* basic functionality


## Future Improvements

* Barcode-based product lookup
* Better search accuracy
* Ability to choose from product matchup from Open Food Facts API
* UI enhancements (animations, modals, etc)
* User Authentication


## Author

Sanaeya James
Junior Developer

Built as a part of SWE course assignment.
