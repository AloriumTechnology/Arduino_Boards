# Alorium Technology Arduino Boards

This repository contains support for the following Alorium Technology Arduino-compatible development boards:

* [XLR8](http://www.aloriumtech.com)

Each board will be added as an entry to the Arduino **Tools** > **Board** menu.

### Installation Instructions

To add board support for our products, go to **File** > **Preferences**, (on OS X it's **Arduino** > **Preferences**) and paste this URL into the 'Additional Boards Manager URLs' input field:

	https://raw.githubusercontent.com/AloriumTechnology/Arduino_Boards/master/package_aloriumtech_index.json

This field can be found in 'Preferences...' under the Arduino File menu. Multiple URLs can be listed by separating them with commas.

Now, under the **Tools** > **Board** > **Boards Manager...**, if you type in "alorium", you will see an option to install board files for Alorium Arduino compatible boards. Click "Install" to add these to your list.

Now, when you select the Boards list, you will see a collection of new boards for Alorium.

One of the cool things about the XLR8 board is it can be burned with different FPGA images and those images can have different Xcelerator Blocks (XBs) and can even run at different clock speeds than the Arduino Uno's standard 16MHz. After you've selected XLR8 under Tools->Board, you will see a Tools->FPGA Image menu option. This can be used a few different ways:
* If you don't know or don't care what version is burned on the FPGA and just want to upload a sketch, just choose one of the "other version" items to tell the compiler what speed the FPGA is running at (it's 16MHz unless you've burned a faster image). Then do Upload like you would for any other Arduino board.
* If you want to burn a new image to the FPGA, select the desired image (one with a version number) under Tools->FPGA Image, and then select Tools->Burn Bootloader. (Instead of burning a bootloader, you'll be burning a new image to the FPGA which takes a little over a minute). To help us improve our products, copy the URL that is printed after the process is complete and paste it into a web browser along with any comments you may have. Then upload a sketch and enjoy the awesomeness. 
* If you want to switch to image 0 (there's probably no reason you would want to, but if you did....), select Tools->FPGA Image->Image 0, and then select Tools->Burn Bootloader. Instead of burning a bootloader or a new FPGA image, you'll be switching to a fail-safe image that can't be overwritten; it takes a few seconds to make the switch. The image you previously had is not lost and you will return to that image the next time the board is powered off and back on.

If you have installed our [XLR8Info](https://github.com/AloriumTechnology/XLR8Info) library, you can use File->Examples->XLR8Info->GetXLR8Version to help determine what image is currently burned onto the FPGA.
Many of the FPGA images that you can burn include the Floating Point, Servo, and NeoPixel XBs. Libraries that take advantage of thier performance are available:
* [XLR8Float](https://github.com/AloriumTechnology/XLR8Float)
* [XLR8Servo](https://github.com/AloriumTechnology/XLR8Servo)
* [XLR8NeoPixel](https://github.com/AloriumTechnology/XLR8NeoPixel)
* [XLR8ADC](https://github.com/AloriumTechnology/XLR8ADC)

Any questions or comments? Let us know on our forum at [http://forums.aloriumtech.com/](http://forums.aloriumtech.com/)