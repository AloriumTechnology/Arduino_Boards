# Alorium Technology Arduino Boards

This repository contains support for the following Alorium Technology Arduino-compatible development boards:

* [XLR8](http://www.aloriumtech.com)

Each board will be added as an entry to the Arduino **Tools** > **Board** menu.

### Installation Instructions

To add board support for our products, go to **File** > **Preferences**, and paste this URL into the 'Additional Boards Manager URLs' input field:

	https://raw.githubusercontent.com/AloriumTechnology/Arduino_Boards/master/package_aloriumtech_index.json

This field can be found in 'Preferences...' under the Arduino File menu. Multiple URLs can be listed by separating them with commas.

Now, under the **Tools** > **Board** > **Boards Manager...**, if you type in "aloriumtech", you will see an option to install board files for Alorium Arduino compatible boards. Click "Install" to add these to your list.

Now, when you select the Boards list, you will see a collection of new boards for Alorium.

The XLR8 board can be run at multiple speeds. To choose the speed you want **you must select the correct processor** in the 'Tools' menu.

Note, this will only work under Arduino IDE versions 1.6.4 and up. Also, with version 1.6.6 you may need to use http instead of https for the link to the .json file in File > Preferences. For Arduino versions prior to 1.6.4 (back to 1.5) you should be able to extract the boards.txt file from alorium-avr-1.0.0.tar.bz2 and manually install it.
