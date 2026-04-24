'''
Generators

--> This is a special type of function that return an iterator which one at a time

yield

-->It will take a pause and again resume,this is not a normal keyboard which cannnot be used in nrml function

Next()

-->This is used to get next value from a generator
-->when the value is finished,it will stop the iterator
'''

##def generator():
##    yield 1
##    yield 2
##    yield 3
##an=generator()
##print(next(an))
##print(next(an))
##print(next(an))

##def sq_gen(n):
##    for i in range(n):
##        yield i*i
##for val in sq_gen(5):
##        print(val)

##def power(j):
##    for i in range(j):
##        yield i**i
##for val in power(5):
##    print(val)


##for i in range(1,10):
##   print(i*i)

def sq(n):
    for i in range(n):
        print(i*i)
sq(10)





















        
        
        
