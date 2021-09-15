# Data-Structures

Showcasing foundational data structure concepts using Python and Flask. Query data via API that use _linked lists_, _hash table_, _binary search tree_ as well as _stacks_ and _queues_ data structure concepts.

---

## Setupt

**Create Python environment:**

`conda create -f environment.yml`
`conda activate datastruc`

**Create database (or use existing):**

`python`
`from server import db`
`db.create_all()`
`exit()`

A _sqlitedb.file_ file should be created. View the db via [SQLite Browser](https://sqlitebrowser.org/dl/).

**Create dummy data (or use existing):**

`python gen_dummyData.py`

**Run server to allow API queries:**

`python server.py`

Use _[Postman](https://www.postman.com/)_ for API testing.

---

##### _based on [Data Structures For Python Developers (w/ Flask) - Course](https://youtu.be/74NW-84BqbA)_