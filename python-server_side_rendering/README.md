# Python Server-Side Rendering

This directory contains Tasks 0 to 4 for the server-side rendering project. It includes one standalone Python templating function and several Flask apps using Jinja templates, file-based data sources, and SQLite.

## What We Completed

### Task 0: Simple templating program
- Implemented invitation generation in [task_00_intro.py](task_00_intro.py).
- Added input validation for:
	- Invalid template type
	- Invalid attendees type
	- Attendees not being a list of dictionaries
- Added required edge-case handling:
	- Empty template message: Template is empty, no output files generated.
	- Empty attendees message: No data provided, no output files generated.
- Implemented placeholder replacement for:
	- name
	- event_title
	- event_date
	- event_location
- Missing or None values are replaced with N/A.
- Generates output files named output_1.txt, output_2.txt, etc.

### Task 1: Basic Flask + Jinja pages
- Implemented Flask app in [task_01_jinja.py](task_01_jinja.py).
- Added routes:
	- /
	- /about
	- /contact
- Created reusable templates:
	- [templates/header.html](templates/header.html)
	- [templates/footer.html](templates/footer.html)
- Created page templates:
	- [templates/index.html](templates/index.html)
	- [templates/about.html](templates/about.html)
	- [templates/contact.html](templates/contact.html)

### Task 2: Dynamic template with loops and conditions
- Implemented in [task_02_logic.py](task_02_logic.py).
- Added /items route that reads items from JSON and renders [templates/items.html](templates/items.html).
- Template behavior:
	- Displays an unordered list when items exist
	- Displays No items found when the list is empty

### Task 3: Display data from JSON or CSV
- Implemented in [task_03_files.py](task_03_files.py).
- Added /products route with query parameters:
	- source=json
	- source=csv
	- optional id filter
- Created product template [templates/product_display.html](templates/product_display.html).
- Implemented required error handling:
	- Wrong source
	- Product not found

### Task 4: Extend products display with SQLite
- Implemented in [task_04_db.py](task_04_db.py).
- Extended /products route to support:
	- source=sql
- Added SQLite read logic and error handling for database issues.

## Project Structure

- Python task files:
	- [task_00_intro.py](task_00_intro.py)
	- [task_01_jinja.py](task_01_jinja.py)
	- [task_02_logic.py](task_02_logic.py)
	- [task_03_files.py](task_03_files.py)
	- [task_04_db.py](task_04_db.py)
- Templates:
	- [templates/index.html](templates/index.html)
	- [templates/about.html](templates/about.html)
	- [templates/contact.html](templates/contact.html)
	- [templates/header.html](templates/header.html)
	- [templates/footer.html](templates/footer.html)
	- [templates/items.html](templates/items.html)
	- [templates/product_display.html](templates/product_display.html)
- Data files:
	- [data/template.txt](data/template.txt)
	- [data/items.json](data/items.json)
	- [data/products.json](data/products.json)
	- [data/products.csv](data/products.csv)
	- [data/products.db](data/products.db)

## How To Run

### Task 0
Run your test file that imports generate_invitations from [task_00_intro.py](task_00_intro.py).

### Flask tasks
Run each app from this directory:

python3 task_01_jinja.py
python3 task_02_logic.py
python3 task_03_files.py
python3 task_04_db.py

Then open these routes in your browser:

- http://127.0.0.1:5000/
- http://127.0.0.1:5000/about
- http://127.0.0.1:5000/contact
- http://127.0.0.1:5000/items
- http://127.0.0.1:5000/products?source=json
- http://127.0.0.1:5000/products?source=csv
- http://127.0.0.1:5000/products?source=sql

## Notes

- Python syntax checks were completed successfully for all task files.
- If Flask is missing in your environment, install it before running Flask tasks.
