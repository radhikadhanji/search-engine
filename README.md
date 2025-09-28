# Search Engine (WIP)

I am currently creating a search engine with Python and intend to document the process further on my blog in my personal website. At the moment, the crawler explores a Wikipedia webpage, parses the data from that webpage and adds to three SQL tables - the webpage itself and it's information, the outlinks for the webpages and the backlinks for the webpages. I have also created an indexer which, at the moment, is being tested with arbitrary data - the indexer maps the common words in a text to their frequency within the text, and in the future it will add this frequency information to each row in the webpages table corresponding to the URL of the referenced webpage. 

I am also in the process of migrating the database handling to Supabase as the database after crawling is too large to sufficiently store on Github.

Process:
# 1) Crawler - mostly complete (need to migrate handling of database to Supabase)
# 2) Indexer - partially complete, need to link mapped data to the webpages table
# 3) Query Engine - not started
# 4) Client - not started
