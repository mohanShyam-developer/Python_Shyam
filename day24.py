'''
File handling:
-----------------------
  File handler is an object of file to maintain several functions of file such as creating,reading
  writing and update also deleting the file.

How to open file:
-----------------------  
1.Open()-----> should close with close()
   This open() function takes 2 parameters
   1.File name
   2.Mode

2.with open()--->manually it will close ,no need to write!

   Modes:("r","w","a","x","b","t")
     Mode	     Description
     'r'   -->	 Read (default)
     'w'   -->	 Write (overwrites file)
     'a'   -->	 Append (adds to file)
     'x'   -->	 Create new file (error if exists)
     'b'   -->	 Binary mode
     't'   -->	 Text mode (default)

'''
'''f=open("demo.txt","r")
print(f.read(13))
f.close()
'''


##
##
##import re
##any="this method can read the enire file and return into list with"
##so=re.findall("[a-z]",any)
##print(so)
##
##some="by using this function,it will only find first sequence in the "
##an=re.search("[a]",some)
##print(an)







'''
Regular Expression(RsgEx) :
------------------------------------
This regular expression or RegEx is a sequence of charecters that forms a  searching pattern .
To use this we have to import re ,which will unlock the package.

Functions:
--------------
1.Findall - This function is used to find all the  sequence of charecters in the string.
syntax - re.findall( metachar,variable_name ).

2.Search - by using this u can find only 1st sequence in the string.
syntax - re.search ("matachar",variable_name).

import re
any = "python is  a language" 
so = re.findall( "a",any )
an = re.search("a"any)
print(so)

Metacharecters -  are used to form searching pattern.
---------------------
1.[ ] - in this we can search for [a-z],[A-Z],[0-9]
import re
any = "This function is us2ed to find al1l the  seque9nce of charecters in the string "
so = re.findall("[0-9a-z]",any) #[ ]metacharecter
an = re.search("[a-z]",any) 
print(so,an)

2.   . - This will form a searching pattern as it will take any single charecter for .   .
import re
we = "hello"
the = re.findall("h....o",we)
thing = re.search("he..o",we) #  .  metacharecter
print(the)
print(thing)

3. ^ - this is used to  find the  string is starting with the sequence or not.
syntax - re.findall()
'''


'''import re
any = "python is  a language" 
so = re.findall( "a",any )
print(so)'''



##import re
##
##any="This meta character will form a searching pattern as it take any one or more character"
##
####an=re.findall("ch.?",any)
####print(an)
##
####an=re.findall("Th.{25}",any)
##an=re.findall("that|will",any)
##print(an)
##
##import re
##txt="The rain in 56 Spain"
##
####x= re.findall("\AThe",txt)
##x=re.findall(f"\s",txt)
##print(x)
##if x:
##    print("Yes, there is atleat one match")
##else:
##    print("No,there is not match")


'''
Time and Date
======================
&d-->Day
%H-->Hour
%M-->Min
%s-->sec
%p-->AM/PM
%A-->Day name
%B-->Month name

'''
##import datetime
##now=datetime.datetime.now()
##print(now)

import datetime
today=datetime.date.today()
print(today.strftime("%d-%m-%y"))
print(today.strftime("%a"))
print(today.strftime("%h"))





























































