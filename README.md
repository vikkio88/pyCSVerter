# pyCSVerter
In this folder you will find my solution to the Data pipeline case-study test

### How to use it
Just go on this folder with a command prompt with python(>=3) installed and in the path and just:
```
$ python pycsverter.py
```

To ask for available commands:
```
**********************
	pyCSVerter - Parser
**********************


	type 'help' for a command list


> help
```

you will have this other prompt
```
> help

Documented commands (type help <topic>):
========================================
help  load  outputs  parse  print  quit  reload  results_info  save  sort


>
```

you can also type
```
> help COMMAND
```
To have more info about a single command.
***Example***
```
> help sort
Sort by a field name: sort FIELD

> help load
Load the parsed and validated data from csv (you can specify a new file path)

>
```


# Requirements

My program fulfill the following requirements:

1. Read data from the given CSV file `example.csv`. The first line is a header
   which describes all field names.

2. Validate the data
   - All string fields may not contain non-ASCII characters.

3. the data output can be saved in one(or all) of the following formats: XML, JSON, SQLite Database,
YAML, HTML and CSV. The output will be in the same directory as the input:
filename: validated_output.FORMAT_CHOOSEN

# Bonus tasks

I implemented the following:

* Make the tool extensible to new output formats
 - The only thing you need is to write another Formatter, (lib.formatters) base on the interface in the same folder, and add the configuration in the config file.
* We care more about code quality (readability, software architecture) than about performance - although fast execution is a plus.
 - I documented as much as I could, and python itself is really readable without any effort.
 - About the performance I am quite surprised that is quite fast, just the sqlite3 writing is taking a bit more than expected
* Unit tests would be nice
 - I implemented some unittests drafts, I did not cover the whole codebase, it was going to require too much time.
* Add options to sort/group the data before writing it
 - I implemented the sort (reversed if you sort twice) on the command prompt, as example
 ```
 > print 0
 {...stars:5...}
 > sort stars
 > print 0
 {...stars:1...}
 > sort stars
 > print 0
 {...stars:5...}
 ```
