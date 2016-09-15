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

One of the cool things about the XLR8 board is it can be burned with different FPGA images and those images can have different Xcelerator Blocks (XBs) and can even run at different clock speeds than the Arduino Uno's standard 16MHz. After you've selected XLR8 under Tools->Board, you will see a Tools->FPGA Image menu option.

To burn a new image to the FPGA, select the desired image under Tools->FPGA Image, and then select Tools->Burn Bootloader. (Instead of burning a bootloader, you'll be burning a new image to the FPGA which takes a little over a minute). To help us improve our products, copy the URL that is printed after the process is complete and paste it into a web browser along with any comments you may have. Then upload a sketch and enjoy the awesomeness.

When an Arduino sketch is compiled for XLR8 using the Verify/Compile and/or Upload buttons or menu selection in the Arduino IDE, the Tools->FPGA image selection at the time of the compile needs to have the same CPU speed (16MHz or 32MHz) as the image that has been burned onto the FPGA. If you have installed our [XLR8Info](https://github.com/AloriumTechnology/XLR8Info) library, you can use File->Examples->XLR8Info->GetXLR8Version to help determine what image is currently burned onto the FPGA.

Many of the FPGA images that you can burn include the Floating Point, Servo, and NeoPixel XBs. Libraries that take advantage of their performance are available:
* [XLR8Float](https://github.com/AloriumTechnology/XLR8Float)
* [XLR8Servo](https://github.com/AloriumTechnology/XLR8Servo)
* [XLR8NeoPixel](https://github.com/AloriumTechnology/XLR8NeoPixel)
* [XLR8ADC](https://github.com/AloriumTechnology/XLR8ADC)

Any questions or comments? Let us know on our forum at [http://forums.aloriumtech.com/](http://forums.aloriumtech.com/)