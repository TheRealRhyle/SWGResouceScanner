# SwG to Galaxy Harvester

## Idea

A run-able script that will read resource data from the game screen and parse it in such as way that it can be directly loaded to GalaxyHarvester.  

### Prep work:

 [ ](Ensure connection to GalaxyHarvester.)[https://github.com/pwillworth/galaxyharvester/wiki/Web-Services]
 [ ]Pull auth token, store authToken locally. This is needed for Phase II. - Done
	
Phase I - Getting and Parsing:
	[ ] Get data from the screen. - Done
	2: Parse data. - Done
    3: Save to a text file. - Done
	4: Validate data. - Done

Phase II - Galaxy Harvester Integration:
	1: Format output string for submitting to GH. - Done.
    2: Post resource manually using formatted string. - Done
	3: Post to Galaxy Harvester. - Done - Delayed.

Phase III - Troubleshooting and Future planning:
    1: Planet name does not show on compass when you first log in, need to travel/switch planets. This will break utils/planet_coords
    -- Planet name should come from chat trigger, coords can come from screen data.
    2: Posting to Discord works if provided with an webhook.
    3: Need to implement some for of feedback for success/failure to post to GH.
    4: Read chatlog for information and text triggers. 
    -- C:\SWG Restoration III\profiles\rhyle\Restoration\
    5: Debug log

Phase IV - Create an EXE:
    1: convert python to distributable exe.
