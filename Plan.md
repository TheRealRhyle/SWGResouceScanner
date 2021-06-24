# SwG to Galaxy Harvester

## Idea

A run-able script that will read resource data from the game screen and parse it in such as way that it can be directly loaded to GalaxyHarvester.  

### Prep work

- [x] ~~Ensure connection to [GalaxyHarvester](https://github.com/pwillworth/galaxyharvester/wiki/web-Services).~~
- [x] ~~Pull auth token~~
- [x] ~~Store authToken locally. This is needed for Phase II.~~

### Phase I - Getting and Parsing

- [x] ~~Get data from the screen.~~
- [x] ~~Parse data.~~
- [x] ~~Save to a text file.~~
- [x] ~~Validate data.~~

### Phase II - Galaxy Harvester Integration

- [x] ~~Format output string for submitting to GH.~~
- [x] ~~Post resource manually using formatted string.~~
- [x] ~~Post to Galaxy Harvester. - Delayed.~~

### Phase III - Troubleshooting and Future planning

- [ ] Planet name does not show on compass when you first log in, need to travel/switch planets. This will break utils/planet_coords
- --> Planet name should come from chat trigger, coords can come from screen data?
- [x] ~~Posting to Discord works if provided with an webhook.~~
- [ ] Need to implement some for of feedback for success/failure to post to GH.
- [ ] Read chatlog for information and text triggers.
- C:\SWG Restoration III\profiles\>user name<\Restoration\
- This does not work as the chat log is only stored on logout, area transition, or turning off the log.
- [ ] Debug log

Phase IV - Create an EXE:
- [ ] convert python to distributable exe.
