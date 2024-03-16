                              **Folder changes detector User Manual**
This is the User Manual of the program that shows every modification done to a specific folder on your PC.
In order to run the program without any problems, you should follow these steps:
1. Open your compiler. It is mandatory to have an installed compliler like Microsoft Virtual Studio Code or any other Python compiler. **Online compilers DON'T WORK** as I have tested.
2. Once the compiler is set up, open a new python file and paste the code in.
3. Search for line 60 where is the file location.
4. Replace the file location with the location of the folder you want to verify.
5. If you run VSCode, there shouldn't be any problems in Problems field.
6. Run the code.
7. On the terminal, there should appear: Choose one of the options: Info / Status (or type "exit" in order to exit):.
8. Type "Info" in order to show the file name and it's size (The way you enter the option is not unique. You can type InFO and the program will detect it).
9. Type "Status" in order to show the file name and the date it has been modified (Same as the Info, it doesn't matter how you enter it(ex: STatuS)).

That's all you need to do in order to use this program. I'll give you some information about the program.
This program is made to show every change in a folder **On WINDOWS** the folder can be changed by pasting the folder location instead of the data in line 60.
The program updates itself every 5 seconds so, no matter when you change the files in the folder, the program will notify you via the terminal.
Other features are:
1. New files are detected too, they are shown in the terminal.
2. Deleted files are shown in the moment they are deleted.
3. The code has an easy structure that you can learn on.
4. It's fairly easy to upgrade it, for example to introduce a custom folder location.
5. With some more advanced skills, you can implement a batch verify system.

That's all you need to know in order to use this detector. Have fun using it and I hope that it will be upgraded with better versions. 
