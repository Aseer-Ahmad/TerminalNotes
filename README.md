 # TerminalNotes
Small python script run using Terminal alias for ubuntu linux.
No GUI notes for linux are comparable to the Windows [Sticky notes].

This script provides an easy trip to take notes and manage them on terminals itself.
As easy and simple as Ctrl+Alt+T and write "note".
That's it.

This beginner script would provide to:
1. Search through files based on names
2. Search through content based on keywords

Now, for one to be able to use this.
We simply have to add a $PATH to .bashrc file.

One can accomplish this by using the helper.py.   
But before running it, keep both the scripts at the same location. {preferably in the /home/{username}/ directory}

Now open your terminal and run helper.py      
$ python helper.py

This will create a new directory at /home/{username}/bin and a file inside it.

After that open terminal(Ctrl+alt+T) 
$ gedit ~/.bashrc

Now, go to the last line and write:
PATH=$PATH:/home/{username}/bin

Now back in terminal execute the following commands:   
  $ source ~/.bashrc 
  $ source ~/.profile   
  $ . ~/.bashrc

AND IT's DONE!!
Just open a new terminal anywhere and type  <note> to begin.

PS: if a permission denied error comes up, go to /home/{username}/bin directory.
Open terminal and write the following:
$ chmod 744 note

