import re


def validIPAddresses(string):
    # Write your code here.
    dot1 = 1
    dot2 = 2
    dot3 = 3
    ips = []
    print(len(string))
    for dot1 in range(len(string)):
        for dot2 in range(len(string)):
            for dot3 in range(len(string)):
                substring1 = string[0:dot1]
                substring2 = string[dot1:dot2]
                substring3 = string[dot2:dot3]
                substring4 = string[dot3:]
                no_leading_zeros = check_integer(substring1) and \
                                    check_integer(substring2) and \
                                    check_integer(substring3) and \
                                    check_integer(substring4)
                # print(check_integer(substring1), substring2, substring3, substring4)
                if no_leading_zeros == True:
                    # print("hi")
                    sub_string_less_255 = 0 <= int(substring1) <= 255 and \
                                          0 <= int(substring2) <= 255 and \
                                          0 <= int(substring3) <= 255 and \
                                          0 <= int(substring4) <= 255

                    if sub_string_less_255 and no_leading_zeros:
                        accepted_ip = substring1 + "." + substring2 + "." + substring3 + "." + substring4
                        ips.append(accepted_ip)
    return ips

def check_integer(string):
    if len(string) == 0:
        return False
    if len(string) > 1 and string[0] == "0":
        return False
    else:
        return True

# print(''[0])

print(validIPAddresses("1921680"))