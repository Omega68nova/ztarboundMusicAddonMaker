# ztarboundMusicAddonMaker
A python script that automatically makes addons for the Ztarbound/FU music player from a bunch of .ogg music files and a icon, ready to be uploaded to the steam workshop.\n\n
\n\n
To use:\n\n
1.- Put the wanted music files (.ogg format is required) and a png file that will be the icon of the mod in the same folder as the script. \n\n
2.- Open the script in notepad and change the following variables to your preffered ones (the text between the quotes is what must be changed, and the text after the # symbol explains what they do):\n\n
    GroupName ="ABC"                                         #A shortened name of the group. \n\n
    FullGroupName="Abecedary Burst Condemnation"             #The full name of the music group used for description.\n\n
    FullIconFileName = "icon.png"                            #The name of the icon file.\n\n
    Author ="Omega68"                                        #The name of the author.\n\n
Make sure to change at the very least the FullIconFileName parameter to the name of your png file with the ".png" part included, or the program wont work.\n\n
3.- Open a terminal in the folder the script and files are in, and run the command "python script.py".\n\n
4.- Congratulations, you have the mod ready for use or upload using the mod_uploader.exe located in your Starbound\win64 folder!\n\n
