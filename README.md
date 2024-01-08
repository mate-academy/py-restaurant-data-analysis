# Restaurant data analysis

- Read [the guideline](https://github.com/mate-academy/py-task-guideline/blob/main/README.md) before start


### Task

You're given part of restaurant's [db](app/db.sqlite3) with product, order & order_items info.
Your task is to extract data from db using SQL queries & perform data analysis on it.
Detailed step-by-step task you will find [here](app/main.ipynb).

Over-all notes:
- Do not use any ORM for data extraction - perform only raw SQL queries using `sqlite3` module.
- You can use `group by` on SQL level or on pandas level - it's your choice.
- If you think, that some additional analytics should be applied - just make it.
