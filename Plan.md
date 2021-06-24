# SwG to Galaxy Harvester

## Idea

A run-able script that will read resource data from the game screen and parse it in such as way that it can be directly loaded to GalaxyHarvester.  

### Prep work:

- [x] Ensure connection to [GalaxyHarvester](https://github.com/pwillworth/galaxyharvester/wiki/web-Services).
- [x] Pull auth token
- [x] Store authToken locally. This is needed for Phase II.

### Phase I - Getting and Parsing:

- [ ] Get data from the screen.
- [ ] Parse data.
- [ ] Save to a text file.
- [ ] Validate data.

Phase II - Galaxy Harvester Integration:
1: Format output string for submitting to GH..
    2: Post resource manually using formatted string.
3: Post to Galaxy Harvester. - Delayed.

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
