# LBRclaw-fuck-your-claw-game
leaf blower revolution claw game automation


this is usable for any version of the claw game, however youll have to manually set the locations your looking at for the code. left and top are the important ones to change. 

ive left in some debug code you can use to check if yours is placed correctly. and ive included a variations system but i advise against using it. 

youll need to define all the searched for items based on the hex color of them. i recommend downloading autoit and usign their window info app to get both the location and the hex codes for your colors.

you will need pyautogui, numpy, and time installed in order for the script to function.

it misses alot, this is because the game moves too fast for the app, in the browser version i turned hardware acceleration off and it never missed. 
if you can speed up the processing of this app please do im happy to see upgrades

i might make a ui for this at some point but do not count on it.
a good note is that if hardware acceleration is off, for some reason the colors change slightly. this will cause an error so make sure your colors are based on your current settings

(im planning to remake this in autoit3 to see if that speeds it up)
