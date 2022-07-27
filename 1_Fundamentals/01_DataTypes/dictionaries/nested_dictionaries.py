
myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}
#print(myfamily.keys()) # => dict_keys(['child1', 'child2', 'child3'])
#print(myfamily.clear()) # => None | removes all elements

#print(myfamily) # => {'child1': {'name': 'Emil', 'year': 2004}, 'child2': {'name': 'Tobias', 'year': 2007}, 'child3': {'name': 'Linus', 'year': 2011}}

#print(myfamily["child2"]) # => {'name': 'Tobias', 'year': 2007}

print(myfamily["child3"]["year"]) # => 2011