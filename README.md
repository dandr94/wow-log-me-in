# WoW Log me In

Simple program that allows you to schedule your next wow login. It uses 'Tabs' as main thing to find your play button in Battlenet. Decided to make it because since the launch of WOTLK pre patch there was a lot of que in my server, so if I came home late there were like 5 h que times. Code requires some clean up but it works fine, so what ever. For visual presentation check the 'gif'.
* This will not keep your character in game. I'm personally against things like these that can keep your character in game since, you take space for someone else who wants to play. This app only allows you to launch the game at specific time.

## How to use it:

1. Download the exe or download the src.py and run it in your terminal.
> Pretty sure the exe will raise false positives, so don't worry.
  
2. Find the amount of tabs needed:
> **To see the amount of tabs needed: Fully close your launcher then opened it, start pressing 'tab' and count how much you need until your reach the play button.* 
2. Run the app. You will see the frame of the app:

 * Dir: 
> Click browse and select your WoW Classic shortcut.
 * Time (24h format): 
>on H insert the hour and on M insert the minutes when you want your game to launch. 
  * Tabs: 
>Insert the tabs needed to reach your play button.

3. Click launch:
>When the times comes up it will launch your exe. 


## Requirements

1. To work normally you need to fully close your launcher.
  

## Issues 
 * You need to know how big of a que you will be placed on and estimate the time to launch the app.
 * Sometimes Blizzard places pop up adds when you launch your game. This can break the app because the amount of tabs will be wrong.
 *If you Add or Remove favorites, you need to find the right amount of tabs again.
 

## After thoughts
I was experimenting with X and Y coordinates to move the mouse on the play button but it was a lot more annoying since sometimes the launcher is on the wrong position for some reason.
Tried too with visually locating something on the screen if you have an image file of it but sometimes it didn't work, so the 'tabs' method seemed the most acceptable. Probably there is other methods that are a lot easier than my methods, but yeah... this was what I came with and it worked for me and my friends.
