# Data-Structures with Flask

Showcasing foundational data structure concepts using Python and Flask.

Query data via API that use different data structure concepts:

* linked lists
* hash tables
* binary search trees
* stacks and queues

---

## Setup

Dependencies can be found in [environment.yml](environment.yml)

Create Python environment:

* `conda create -f environment.yml`

* `conda activate datastruc`

Create database (or use existing):

* `python`

* `from server import db`

* `db.create_all()`

* `exit()`

A _sqlitedb.file_ file should be created. View the db via [SQLite Browser](https://sqlitebrowser.org/dl/).

Create dummy data (or use existing): `python gen_dummyData.py`

## Usage

**Run server to allow API queries:**

`python server.py`

Use _[Postman](https://www.postman.com/)_ for API testing. You can find examplary API call in _/resources_

---

##### _based on [Data Structures For Python Developers (w/ Flask) - Course](https://youtu.be/74NW-84BqbA)_