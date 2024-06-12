"""
Commenting skills:

NOTE: this file runs just fine, this is for you to learn to use the debugger!

TODO: above every line of code comment what you THINK the line below does.
TODO: execute that line and write what actually happened next to it.

See example for first print statement.

TODO: Start a list of important programming vocabulary in your readme.md for 
this week. E.g. the word "calling" means something in a programming context, 
what does it mean?
"""
import platform

# I think this will print "hello! Let's get started" by calling the print function.
print("hello! Let's get started")  # it printed "hello! Let's get started"

#This line assigns a list of strings to this variable, 'some_words' 
some_words = ["what", "does", "this", "line", "do", "?"] #it has assigned a list to some_words because on line 23-24, it does iterate through this list. 

#I think this line iterates through the some_words list 
for word in some_words: #iterated through all the elements in the some_words list. 
    #I think this line prints out 'word', which are elements in the some_words list.
    print(word) # it printed elements from the list 

#I think this line iterates through the some_words list
for x in some_words: #iterated through all the elements in the some_words list. 
    print(x) # it printed elements from the list 

#I think this line prints the 'some_words' list 
print(some_words) #it printed the 'some words' list 

#I think this line finds the length of the some_words list and checks to see if the length of the list is more than 3. If yes, it will print out "some_words contains more than 3 words"
if len(some_words) > 3: #checks the conditions of the if statement 
    print("some_words contains more than 3 words") #prints out "some_words contains more than 3 words" 

#I think this line defines a function called usefulFunction()
def usefulFunction():
    """
    You may want to look up what uname does before you guess
    what the line below does:
    https://docs.python.org/3/library/platform.html#platform.uname
    """
    #I think this line gets information about the current computer that is operating on and prints out the specs. 
    print(platform.uname()) #prints out my computer's operating system, name, release, version and machine. 


usefulFunction()
