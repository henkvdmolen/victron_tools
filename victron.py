#
# This tools logs battery time, voltage, current, load current
#

from optparse import OptionParser
import serial
import time


def main():
    opt_parser = OptionParser()
    opt_parser.add_option('-p','--port',help='Port to use',dest='port')
    (options, args) = opt_parser.parse_args()
    
    if not options.port:
        print "-p is required"
        return

    input = serial.Serial(options.port, 19200,timeout=1)
    t0 = time.time()
    data = {}
    while True:
        line = input.readline()
        line_split = line.split()

        if len(line_split) ==2:
            key = line_split[0].strip()
            value = line_split[1].strip()
            
            data[key] = value

            if key == 'PID':  # assume this one comes first
                print (time.time()-t0), data.get('V',0), data.get('I',0), data.get('IL',0)
                data = {}


if __name__ == '__main__':
    main()

