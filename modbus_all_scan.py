import serial
import modbus_tk.defines as cst
from modbus_tk import modbus_rtu

PORT = "COM4"
BAUDRATE = 9600

def main():
    # Open the serial port
    master = modbus_rtu.RtuMaster(serial.Serial(port=PORT, baudrate=BAUDRATE, bytesize=8, parity='N', stopbits=1, xonxoff=0))
    master.set_timeout(1)

    # Scan all Slave IDs from 1 to 256
    for slave_id in range(1, 256):        
        try:
            address = 0
            for address in range(1, 9999):
                data = master.execute(slave_id, cst.READ_HOLDING_REGISTERS, address, 1)
                print("Found device: slave_id={}, data={}".format(slave_id, data))            
        except modbus_rtu.ModbusInvalidResponseError:
            print("Slave ID {} is not responding".format(slave_id))
        except Exception as e:
            print("An error occurred while scanning slave_id={}: {}".format(slave_id, str(e)))

if __name__ == '__main__':
    main()

