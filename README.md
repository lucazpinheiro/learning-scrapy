## learning scraping

Code for the projects I'm doing to learn how to use the scrapy framework.

My idea is to take the 100 most recent posts on [DEV.to](https://dev.to/), extract the title, author, and tags. After that, I want to treat the data, to make sure the strings are well-formatted, loaded it to a database (most probably a Postgres DB).


### requirements

```
Python 3.7
Pipenv
```

### running

Run:

```
pipenv shell
```

Then navigate to ```/getposts/getposts``` and run:

```
scrapy crawl posts
```
this will print the result on the terminal.

Or run:

```
scrapy crawl posts -o posts.json
```
to create a ```JSON``` file with the collected data.


