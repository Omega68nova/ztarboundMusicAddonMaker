import glob, os, json, re, shutil

#A python script that given a bunch of .ogg files and a small png icon automatically creates a addon for the FU/Ztarbound music player that can me instantly uploaded to the starbound workshop or used.
#To run it simply write "python ./script.py" in a console opened in the folder with all the files.

GroupName ="ABC" #A shortened name of the group.
FullGroupName="Abecedary Burst Condemnation" #The full name of the music group used for description.
FullIconFileName = "icon.png" #The name of the icon file.
Author ="Omega68" #The name of the author.

fileset = [f for f in glob.glob("*.ogg")]
filenames=[]
#Renaming the files for convenience and getting the titles so they look better in the ingame UI
for f in fileset:
   filenames.append(
      {
          "name": GroupName+" - "+(re.sub(r"(\w)([A-Z0-9]1+)", r"\1 \2", f[:-4]).replace("_", " ")).title(), #Visible name, taken from file name but with spaces after caps and numbers and replacing underscores.
          "directory": "/music/"+ GroupName+"_"+f
      }
   )
   os.rename(f,  GroupName+"_" + f)
THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
my_file = os.path.join(THIS_FOLDER, 'output.json')
musiclistconfigpatch= [
    {
        "op": "add",
        "path": "/"+GroupName,
        "value": filenames
    },
    {
        "op": "add",
        "path": "/##album_icons##/"+GroupName,
        "value": "/interface/scripted/fm_musicplayer/"+FullIconFileName
    }
] #The patch file that adds the music files to the music player

#Making all the folders needed for the mod...
if not os.path.exists(THIS_FOLDER+"\music"):
    os.makedirs(THIS_FOLDER+"\music")
if not os.path.exists(THIS_FOLDER+"\interface"):
    os.makedirs(THIS_FOLDER+"\interface")
if not os.path.exists(THIS_FOLDER+"\interface\scripted"):
    os.makedirs(THIS_FOLDER+"\interface\scripted")
if not os.path.exists(THIS_FOLDER+"\interface\scripted\fm_musicplayer"):
    os.makedirs(THIS_FOLDER+"\interface\scripted\\fm_musicplayer")
#Writing the patch file into an actual file in the needed folder
with open(THIS_FOLDER+"\interface\scripted\\fm_musicplayer\musiclist.config.patch", "w") as file:
    file.write(json.dumps(musiclistconfigpatch, indent=4))
#Copying the icon file to the needed folder
shutil.copy(THIS_FOLDER+"\\"+FullIconFileName, THIS_FOLDER+"\interface\scripted\\fm_musicplayer\\"+FullIconFileName)


#Moving the renamed files to the music folder
fileset = [f for f in glob.glob("*.ogg")]
for f in fileset:
    shutil.move(f,".\music\\"+f)
#Making the mod metadata file
metadata= {
  "author" : Author,
  "description" : "Adds music from "+FullGroupName+" to the FU/Ztarbound music player.",
  "friendlyName" : "[FU] "+FullGroupName+" Music Player Addon",
  "name" : "[FU] "+FullGroupName+" Music Player Addon",
  "tags" : "Musical Instruments and Songs",
  "version" : "1.0"
}
with open("_metadata", "w") as file:
    file.write(json.dumps(metadata, indent=4))
#Turning the icon into the mod icon for the workshop/mod manager in the game
os.rename(FullIconFileName,"_previewimage")
