# Web Scraper Workflow

## Planning

### Website identity

In order to grab the data from websites, we must first investigate the website, and how it is structured. Some things to look out for:

1. **what is the website about?**

Just some things that websites can be about are selling products, education, hosting content, listings, etc.

2. **what are some important functionality?**

Some key functionality that we can think about are which buttons are of interest to press, search function, page elements like images/videos, etc.

3. **what are some key information that we want to grab?**

Some websites contain articles that we might want to grab, or images/videos, or job listings.

### Clues in the URL

The URL contains some key information that we can immediately grab. Just from the URL, we can deduce the following:

1. The base URL (example: www.linkedin.com, www.google.com, www.facebook.com)

2. The specific site location, or node (example: /articles/story-1.html, /videos/cat-video-1032, /gallery/album-1/images/1-pets)

Other things we can see in the URL are **query parameters**. For example, when searching for a "software developer" in "Australia", the URL changes to suit that query:

```
https://au.indeed.com/jobs?q=software+developer&l=Australia
```

The query parameters here are "**?q=software+developer&l=Australia**." There are three parts to look for in the query parameters:

1. **Start**: In our case, the beginning is denoted by a question mark.

2. **Information**: The pieces of information constituting one query parameter are encoded in key-value pairs, where related keys and values are join together by an equals sign (key=value). In our case, we see two key value pairs: **q=software+developer** and **l=Australia**.

3. **Separator**: Every URL can have multipl query parameters, separated by an ampersand (&) symbol, which is also our case.

These can offer clues into how to retrieve data from the website's database. There are sites that are static, however, which don't need to use databases to display information.

### The Webpage

The webpage itself can be investigated, using developer tools. When on the target webpage, open the developer tools by pressing F12 in the browser of your choice. We will use Microsoft Edge for this project.

The developer tools show the elements on the webpage in what is known as the Document Object Model (AKA "DOM"). The HTML elements shown are clickable, where one can expand, collapse, and even edit the element right on the browser. 