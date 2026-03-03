JSON stands for JavaScript Object Notation — it’s a lightweight format for storing and exchanging data between systems, especially in web applications.

Think of it as a universal language for data:

Easy for humans to read and write (looks like Python dictionaries).

Easy for machines to parse and generate.

Basic Rules
Data is written as key–value pairs.

Keys are strings inside double quotes " ".

Values can be:

String "text"

Number 123

Boolean true / false

null

Array [ ] (list of values)

Object { } (another JSON structure)

Example
json
Copy
Edit
{
  "name": "Ali",
  "age": 21,
  "is_student": true,
  "skills": ["C++", "Python", "JavaScript"],
  "address": {
    "city": "Delhi",
    "pincode": 110001
  }
}
Here:

"name", "age", "skills", "address" → keys

"Ali", 21, true, etc. → values

Where JSON is used
APIs → when websites or apps talk to each other, they often send data in JSON.

Configuration files → many programs store settings in .json files.

Databases → NoSQL databases like MongoDB store documents in JSON-like format.

In Python
Python has a built-in json module to work with JSON.

python
Copy
Edit
import json

# Python dict to JSON
data = {"name": "Ali", "age": 21}
json_string = json.dumps(data)
print(json_string)   # {"name": "Ali", "age": 21}

# JSON to Python dict
python_data = json.loads(json_string)
print(python_data["name"])  # Ali
