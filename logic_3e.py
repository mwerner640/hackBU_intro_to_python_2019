#as you saw in part 3d your python code can respond to conditions
#an easy way to do this is with if/else blocks

a = 23
if a==87:
    print("how?")
elif a<16:
    print("wait...what?")
else:
    print("it worked!")
    
#this code should print it worked!
#can you explain why?

a = 23
if a==87:
    print("how?")
elif a<16:
    print("wait...what?")
elif a>5:
    print("look now.")
else:
    print("it worked!")
    
#this code should print only look now.
#your computer tests each of the statements
#after an if or elif 
#when it finds a True one it completes only the block under it
#and skips the rest
#if you have two "if"s in a row, the second if won't be skipped
#only "elif"s or "else" get skipped

#many different statements cam be put after an if/elif
#an == indicates two statements are equivalent != is the opposite
#other logic symbols include <, <=, >, >=
#in python 'and' indicates intersect and 'or' indicates union

if 5==5 and 4<=27:
    print("this should print)

if True:
    print("this should print")
    
#write a function that utilizes logic symbols
