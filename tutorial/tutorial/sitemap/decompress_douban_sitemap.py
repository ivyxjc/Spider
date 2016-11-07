import gzip


file=gzip.open("E:\\Coding\\douban_data\\sitemap1.gz",'rb')

for i in range(2998,3800):
    file=gzip.open("E:\\Coding\\douban_data\\sitemap{}.gz".format(i),'rb')
    open("E:\\Coding\\douban_data\\sitemap_xml\\sitempa{}.xml".format(i),'wb').write(file.read())