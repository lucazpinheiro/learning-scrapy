## learning scraping

Code for the projects I'm doing to learn how to use the scrapy framework.

It is pretty basic, I'm just begging to learn how to use the scrapy.

### requirements

```
Python 3.7
Pipenv installed
```

### running

Run:

```
pipenv shell
```

Then navigate to ```/getbooks/getbooks``` and run:

```
scrapy crawl books
```
this will print the result on the terminal.

Or run:

```
scrapy crawl books -o books.json
```
to create a ```JSON``` file with the collected data.


