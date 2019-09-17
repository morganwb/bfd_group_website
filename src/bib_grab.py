import os
import bibtools as bt
from bibtools import ads
from pathlib import Path
from jinja2 import Template
import re

CONTENTDIR = "../content/publication/"
content_path = Path(CONTENTDIR)
temp_str = """+++
abstract = "{{ abstract }}"
abstract_short = "{{ abstract_short }}"
date = "{{ date }}"
image = ""
image_preview = ""
math = true
publication = "{{ journal }}"
publication_short = ""
selected = false
title = "{{ title }}"
url_code = "{{ url_code }}"
url_dataset = ""
url_pdf = "{{ url_pdf }}"
url_project = ""
url_slides = ""
url_video = ""

{% for author in authors %}

[[authors]]
    name = "{{ author }}"
    is_member = true
{% endfor %}
+++
{{ all }} 
"""

template = Template(temp_str)

app = bt.BibApp()
searchterms = ['author:Oishi,J','year:[2003 TO 2019]']
filterterms = ['database:astronomy']

records = ads._run_ads_search(app,searchterms,filterterms,field_list='abstract,author,bibcode,doi,title,pub,pubdate')
for r in records['response']['docs']:
    if 'abstract' in r:
        abstract = r['abstract'].replace('"','\\"')
    else:
        abstract = ""

    print("bibcode: {}, first author: {}, journal: {}".format(r['bibcode'],r['author'][0],r['pub']))
    # user_input = input("Exclude? [y for yes; default is no]")
    # if user_input == "y":
    #     continue
    title = r['title'][0].replace('"','\\"')
    filename = "{}.md".format(r['bibcode'])
    outfile = content_path/filename
    pub_date = re.sub('-00','-01',r['pubdate']) # replace weird zero in day field
    date = "{:}T00:00:00+00:00".format(r['pubdate'])
    outfile.write_text(template.render(title=title,journal=r['pub'],abstract=abstract,date=date,authors=r['author']))
