# Anemoment Pi-Hat-TriSonica Schematic Review

### <a name="sd_section"></a>Issues with Second SD Card
According to section five of the [BCM2835 Arm Peripherals](../BCM2835-ARM-Peripherals.pdf) document, the BCM SOC only supports a single SD Card interface.  The [device tree file](https://github.com/torvalds/linux/blob/master/arch/arm/boot/dts/bcm283x.dtsi), which is common between this chip and the RPi 3's BCM2837, similarly indicates a single SD card controller is available.

### Raspberry Pi Connector
* The pinout matches publicly available references.

* Series Terminators?  Pop-options for pullups/pulldowns?

* Verify the layout of this connector matches how you want it to mount on the RPI.

### Serial Port LTC2870
* Not sure what sort of driver support is needed/available for functionality beyond UART.  Maybe you could talk me though it?

* Pinout matches [datasheet](http://cds.linear.com/docs/en/datasheet/28701fb.pdf).

* TX/RX pins appear correct.

* According to the [datasheet](http://cds.linear.com/docs/en/datasheet/28701fb.pdf), DZ should not be floated.

### Level Converter ST3232ECTR
* Pinout matches [datasheet](http://www.st.com/content/ccc/resource/technical/document/datasheet/60/fc/e5/60/2c/24/41/88/CD00002950.pdf/files/CD00002950.pdf/jcr:content/translations/en.CD00002950.pdf).

### RTC DS1307Z+T&R
* Pinout matches [datasheet](https://datasheets.maximintegrated.com/en/ds/DS1307.pdf).

### TriSonica Power Supply
* Pinout matches [datasheet](http://www.cui.com/product/resource/pds1-s.pdf).
