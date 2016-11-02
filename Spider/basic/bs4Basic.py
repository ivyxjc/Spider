from bs4 import BeautifulSoup
import re

soup = BeautifulSoup('<b class="boldest">Extremely bold</b>',"html.parser")
tag = soup.b
#tag的属性
print(tag['class'])
print(tag.attrs)
print(type(tag))
print(tag)


print("-------")

#tag都有name，更改name会使得所有通过该BS对象生成的HTML文档
soup = BeautifulSoup('<b class="boldest">Extremely bold</b>',"html.parser")
tag = soup.b
print(tag)
print(tag.name)
tag.name="blockquote"
print(tag)

print("-------")
soup = BeautifulSoup('<b class="boldest">Extremely bold</b>',"html.parser")
tag = soup.b
#更改属性
tag['class']="verybold"
tag['id']=1
print(tag)
#删除属性
del tag['class']
print(tag)
print(tag.get('class'))

#多值属性的返回类型是list:
print("---------------")
css_soup = BeautifulSoup('<p class="body strikeout"></p>',"html.parser")
print(css_soup.p['class'])

#如果某个属性看起来好像有多个值,但在任何版本的HTML定义中都没有被定义为多值属性,
# 那么Beautiful Soup会将这个属性作为字符串返回
print("-----------")
id_soup = BeautifulSoup('<p id="my id"></p>',"html.parser")
print(id_soup.p['id'])
# 'my id'


print("-----------")
soup = BeautifulSoup('<b class="boldest">Extremely bold</b>',"html.parser")
print(soup.name)
tag = soup.b
print(tag.string)
print(type(tag.string))
tag.string.replace_with("No long bold")
print(tag)


print("------------")
markup = "<b><!--Hey, buddy. Want to buy a used parser?--></b>"
soup = BeautifulSoup(markup,"html.parser")
comment = soup.b.prettify()
print(comment)
print(type(comment))

print("-------------")

html_doc = """
<html><head><title>The Dormouse's story</title></head>

<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""

soup=BeautifulSoup(html_doc,"html.parser")
print(soup.head)
print(soup.p)
print(soup.find_all('p'))
print(soup.p['class'])
print("+++++++")
print(soup.head.contents)
print(soup.head.contents[0])
print("----------")
print(soup.title.contents)
print(soup.title.contents[0])
print("----------")
for i in soup.head.children:
    print(i)
print(soup.p.children)

print("++++++++++")
print(soup.head.contents)
for child in soup.head.descendants:
    print(child)

print(len(list(soup.children)))
print(len(list(soup.descendants)))

print(":::::::::::::")
print(soup.head.string)

print("----------")
for string in soup.stripped_strings:
    print(repr(string))


print("+-+-+-+_=-+")
for parent in soup.a.parents:
    if parent is None:
        print(parent)
    else:
        print(parent.name)

print("+++++++++++")
print(soup.a.next_sibling.next_sibling)

print("+++++++++++")
for sibling in soup.a.next_siblings:
    print(repr(sibling))

print("_______++++++++++")
last_a_tag=soup.find("a",id="link1")
print(last_a_tag)
print("_______++++++++++")
print(last_a_tag.next_sibling)
print("_______++++++++++")
print(last_a_tag.next_element)

print("-----------")
for element in last_a_tag.next_elements:
    print(repr(element))

print("-----------")
for tag in soup.find_all(re.compile("^p")):
    print(tag['class'])