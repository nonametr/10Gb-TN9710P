#!/bin/python3

def read_binary_file_to_c_header(file_name):
    try:
        with open(file_name, 'rb') as file:
            data = file.read()

        # Convert to 16-bit hex values
        hex_data = []
        for i in range(0, len(data), 2):
            value = data[i:i+2]
            if len(value) == 2:
                hex_value = '0x{:02x}{:02x}'.format(value[1], value[0])
            else:
                hex_value = '0x{:02x}00'.format(value[0])
            hex_data.append(hex_value)

        # Header content
        header_content = """
#ifndef _MV88X3310_PHY_H
#define _MV88X3310_PHY_H

static u16 MV88X3310_phy_initdata[] __initdata  = {{  
/* {} */
""".format(file_name)

        # Adding hex data
        for hex_value in hex_data:
            header_content += "  {},\n".format(hex_value)

        # Footer content
        header_content += """
}};

unsigned int  MV88X3310_phy_firmware_len = {};
#endif
""".format(len(data))

        return header_content
    except FileNotFoundError:
        return "Error: File '{}' not found.".format(file_name)
    except Exception as e:
        return "An error occurred: {}".format(e)

file_name = "./x3310fw_0_3_10_0_10860.hdr"
c_header = read_binary_file_to_c_header(file_name)

with open("MV88X3310_phy.h", "w") as output_file:
    output_file.write(c_header)
