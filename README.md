# DO-Temp-Humidity-Sensor
Code for Arduino Thermistor sensor

- Arduino board used is Arduino Uno
- Arduino_Code reads data from sensor
- Python GUI plots data into a live graph, and there's a button to start/stop logging (exported as csv file)


Notes on GUI Code:

1) Log file is appended to, so delete/rename log file before running again
2) Log file directory is printed to the console
3) If port number can’t be accessed/errors with module, restart kernel (Ctrl+K on Pyzo)
