## How to create files for README

In order to sync Markdown files to your Guides, your Changelog, or your Custom Pages, you'll need to add certain attributes to the top of each page via a YAML front matter block. See below for an example:

```
---
title: Syncing Docs via CLI / GitHub
category: 62056dee230e07007218be06
---

Page content goes here...
```

### Where to find the category ID

First you need to create it on your readme docs. With the category created, you need to recover its ID.

Make a request to the [Get all categories](https://docs.readme.com/main/reference/getcategories) endpoint.

In the authorization header, add your docs API_KEY, which can be found in the API Keys under the configurations tab.


#### Python request

The Python code in the [request.py file](./request.py) is also ready to recover all categories from readme.

You need to create a `.env` file and add a `README_API_KEY` variable to it.