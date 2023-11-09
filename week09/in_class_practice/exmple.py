# python

# program will convert number to binary, hex, or octal
# will receive num

def get_num():
    return 10

def get_format():
    return "all"

def num_convert(num, format_type):
    binary = convert_to_binary(num)
    octal = convert_to_octal(num)
    hex = convert_to_hex(num)
    return "b0111"

def display_converted_nums(num):
   print(f"The formatted number is {num}")

def convert_to_binary(num):
    return "b0111"

def convert_to_hex(num):
    return "0347"

def convert_to_octal(num):
    return "0xff"

def test_num_convert():
    assert num_convert(10, "all") == "b1010 0xa 0o12"

def main():
    num = get_num()
    format_type = get_format()
    converted_nums = num_convert(num, format_type)
    display_converted_nums(converted_nums)
    print("Hello, World!")

if __name__ == "__main__":
    main()