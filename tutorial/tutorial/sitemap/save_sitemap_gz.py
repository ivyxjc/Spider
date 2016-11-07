from tutorial.sitemap.sitemap import SiteMap
import json
import os

s=SiteMap()
for i in range(989,1010):
    s.save_sitemap_detail(i)
