def index_in(index,items):
    return index >= 0 and index <len(items)
    
def hash_them(keys, values):

    result = {}
    index = 0
    
    for key in keys:
        if index_in (index, values):
            result[key] = values[index]
        else:
            result[key] = None
    

       
        index += 1
    
          

    return result


print(hash_them(["key"], ["value"]))
print(hash_them(["key1", "key2"], ["value1"]))

