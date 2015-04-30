def how_many_blocks_can_see (blocks):
    if len(blocks) == 0:
        return 0
    
    seen = 1
    print("I am here")
    current_max = blocks[0]
    
    for block in blocks:
        if block > current_max:
            seen += 1
            current_max = block


    return seen

#result(how_many_blocks_can_see([5,6,1,2,8])
#print(result)


n = input("Enter n:")
n = int(n)

start = 1
block_height = []

while start <= n :
       height = input("Enter height:")
       height = int(height)

       block_height += [height]

       start += 1


print(how_many_blocks_can_see(block_height))
