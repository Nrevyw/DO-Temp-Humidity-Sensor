# DO-Temp-Humidity-Sensor
Code for Arduino Thermistor sensor

- Arduino board used is Arduino Uno
- Arduino_Code reads data from sensor
- Python GUI plots data into a live graph, and there's a button to start/stop logging (exported as csv file)


Notes on GUI Code:

1) Edit COM port in line 93
2) Log directories need to be edited before use (lines 46-47 in GUI Code(..).py ; lines 11 & 47 in Arduino+OM-24 Compile.py)
3) Log file is appended to, so rename/delete prior log file before running again
4) Log file directory is printed to the console 
5) If port number can’t be accessed/errors with module, restart kernel (Ctrl+K on Pyzo)
