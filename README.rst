#########
Word-Guru
#########


Released: 10-August-2017

############
Introduction
############

This is a simple "Word-checker" for the game "Word Guru" 
(`Englisch <https://play.google.com/store/apps/details?id=com.wordgames.wordconnect.flat&hl=en>`__,   
`German <https://play.google.com/store/apps/details?id=com.wordgames.wordconnect.de&hl=en>`__).
The game went pretty viral in the last months (Mai - Juli 2017) so I thought I'd might code a little "solver" for it. 
The main idea of "Word Guru" is to build words out of a set of predefined letters. 
This can get tricky when there a lot of letters given and many words to find. 
The code I've wrote needs a dictionary of words to work (longer is better). 
I've provided a set of German words that you can use as a dictionary. 
If you're looking for a set of English words you might find some 
`here <https://github.com/dwyl/english-words>`__.
You can also check out this page for `other <https://github.com/wooorm/dictionaries/tree/master/dictionaries>`__ languages.
You could easily use these for other projects like `here <https://github.com/aherbrich/Hangman>`__.

###########
Quick Setup
###########

Before running the "Word-checker" be sure to go into the code and replace the path with the one where you've saved the textfile with words.

::

    # Replace with correct filepath
    self.filepath = ".../Word-Guru/GermanWords/Words.txt"

This could look like following after doing so:

::

  self.filepath = "C:/Users/Admin/Documents/Python/Word-Guru/GermanWords/Words.txt"
  
If you're going to run the game in the shell you can skip the next steps and follow on with the third part
where I will explain how to run the code (although I recommend still reading it to understand the code better). 
Should you be using a IDE then you invariably have three things to do. 


* I've added a variable

  ::

    self.via_shell = True

  which is set to True by default. Just change this to False.
  
* Since you will not input your letters via the shell you will therefore have too manuelly type them into the code:

  ::
    
    self.word = None
  
  This is the line you are looking for. Here you will add your letters. After doing so it should look something like this:
  
  ::
  
    self.word = "TSUQNOA"
    
  Don't worry about case sensetivity, I took care of it. Note that the variable ``self.word`` doesnt fit to well and the set of 
  letters is meant by this. The last thing you have to do is define the length of the word you're looking for.
  
  ::
  
    self.len_of_output = 0
    
  This variable is set to 0 what means every length is accepted. Change it to something specific if you know what you're looking for.
  When you're finished you can carry on with the next part which I've already mentioned above :)
  
#####################
When running the code
#####################

To run the code via the shell (IDE users can just run the code now and skip everything from here on)
go to the word-guru directory and use the following command:

::

  $ python Word-Checker.py
  
Due to the fact that this wont work yet you will have to add two things:

* Your set of letters
* The length of the word you are looking for (length 0 = all word lengths will be accepted)

After adding that, your command could look like this:
::

  $ python Word-Checker.py TSUQNOA 4
  
If so you're ready to run the code.
