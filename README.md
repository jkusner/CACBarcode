# CACBarcode
Convert scanned CAC barcodes (PDF417 and Code39) into Python objects with all data parsed

A simple one class library under the MIT license designed to help python programmers who need to parse CAC barcodes.


# Usage
```python
from cacbarcode import PDF417Barcode, Code39Barcode

# To parse a barcode, simply do
barcode = PDF417Barcode("data here")

# or the other kind
barcode = Code39Barcode("data here")

# If you want an EDIPI, but aren't sure which barcode is being scanned, do this:
edipi = None
barcode_data = "BARCODE DATA HERE"

try:
  barcode = PDF417Barcode(barcode_data)
  # if this was the wrong type, an exception will be thrown
  # otherwise, this was the correct type, so set the edipi
  edipi = barcode.edipi
except:
  # Try the other barcode type
  try:
    barcode = Code39Barcode(barcode_data)
    
    edipi = barcode.edipi
  except:
    # Neither barcode was correct
    print("Neither barcode worked!")
    
print("EDIPI =", edipi)
```

The easiest way to use this library is with a barcode scanned connected to a computer.
The barcode scanner emulates keyboard input, so doing
```python
barcode = PDF417Barcode(input(">"))
```
will be a very easy way to parse barcodes.

To easily see the contents of the barcode, simply print the object
```python
print(barcode)
```

For more information on CAC barcode structure, see http://www.cac.mil/docs/DoD-ID-Bar-Code_SDK-Formats_v7-5-0_Sep2012.pdf
