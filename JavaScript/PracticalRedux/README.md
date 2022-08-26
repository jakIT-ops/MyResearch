## Inspiration for the Sample Application

### Project Features

* Track XP and improve pilot skills and abilities
* Integration with MegaMek and MegaMekLab
* Planetary map and the plotting of jumpship travel
* Organize a TO&E
* Create and resolve missions and scenarios
* Repair and salvage units
* Equipment tracking
* Financial tracking

For Project `Mini-Mek`, we’re only going to deal with a couple of these, and at a very simple level. Here’s the list of features we’ll build in this course:

* A tabbed UI containing different panes, controlled by Redux state
* Load JSON data describing the pilots and BattleMechs in a combat force
      * For both pilots and Battlemechs: Show a list of all items
      * Allow selection of an item in the list, and show details of the selected item
* Edit the details for a pilot
* Deletion of pilots
* Modal dialogs that can be stacked on top of each other, and used as “pickers” for * choosing values like colors
* Context menus for interactions such as commands for specific list items
