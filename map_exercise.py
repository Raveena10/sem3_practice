#map
#map(function,iter(list,tuple,set,dicionary))
def multiply(num):
    return num*num
def toUpper(str):
    return str.upper()
# result=map(multiply,(2,4,6,8))  #lambda var:return
# result=map(lambda i:i*i,(2,4,6,8))  #lambda var:return
res=map(toUpper,("software","sem","3"))
newlist=list(res)
newlist.append("HEY")
print(newlist)
# newlist1=tuple(res)
# newlist1.append("HEY tuple")
# print(newlist1)

dict_item={"a":"Car","b":"Bike","c":"Train"}
a=map(lambda i:(i[0]+"__",i[1]+"s"),dict_item.items())
print(dict(a))
k=map(lambda i:i+" key",dict_item.keys())
print(list(k))
