import one
print('Top Level in two.py')
one.func()
if __name__ =="__main__":
    print('two.py is being run directly')
else:
    ('two.py has been imported')