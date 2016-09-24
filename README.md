# Alorium Technology Arduino Boards
This repository contains support for the following Alorium Technology Arduino-compatible development boards:

* [XLR8](http://www.aloriumtech.com)

After completing the steps below, you will be able to select Alorium Technology's XLR8 board from your Arduino IDE's menu bar. The XLR8 board will appear as an added as an entry to the Arduino **Tools** > **Board** menu.

*Note: The below "Installation Instructions" assume you have completed step 2.5 of our ["XLR8 Quick Start"](http://www.aloriumtech.com/xlr8-quickstart/) guide.*

### Installation Instructions
##### 1. Add board support for our products.

  1. For Windows and Linux: Go to **File** > **Preferences**, in your Arduino IDE menu bar.
  
  1. For Mac: Go to **Arduino** > **Preferences**, in your Arduino IDE menu bar.
  
  2. Locate the 'Additional Boards Manager URLs' input field.
  
  3. Paste this URL into the "Additional Boards Manager URLs" input field (*Note: multiple URLs can be added to this field by separating each URL with a comma.*)
        https://raw.githubusercontent.com/AloriumTechnology/Arduino\_Boards/master/package\_aloriumtech\_index.json. 

##### 2. Install Alorium's XLR8 board package.

  1. Go to **Tools** > **Board** > **Boards Manager**. 
  
  2. Type "alorium," in the search field and you will see an option to install board files for Alorium Arduino compatible boards. 
  
  3. Select the "Alorium XLR8 Boards" package and then click "Install."
  
  4. Check that the XLR8 board package now exists in your list of available boards.

    1. Go to **Tools** > **Board**. You should see a new section titled "Alorium XLR8 Boards" now exists. Under this new heading should be the XLR8 board. You can select the XLR8 board just like you would normally select the "Arduino/Genuino Uno" board.

  5. Select your new XLR8 board from the Board menu.

##### 3. Return to the ["XLR8 Quick Start"](http://www.aloriumtech.com/xlr8-quickstart/) and begin step 3.2 to continue setting up your XLR8 Board.


Any questions or comments? Let us know on our forum at [http://forums.aloriumtech.com/](http://forums.aloriumtech.com/)

Last Updated: 9/23/2016