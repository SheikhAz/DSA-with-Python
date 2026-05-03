count = 0
def name():
    global count
    if count == 4:
        return
    count += 1
    name()
    print('hello Sheikh')
        
name()