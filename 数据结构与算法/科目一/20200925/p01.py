"""
Copyright (c) Huawei Technologies Co., Ltd. 2021-2021. All rights reserved.
Description: easy_ut p01 file
Author: zhangxiaoan 00565442
Create: 2021/5/13 21:27
"""


def match(ip1, ip2, mask):
    ip1_list = [int(ip) for ip in ip1.split(".")]
    ip2_list = [int(ip) for ip in ip2.split(".")]

    match_len = 0
    for ip1_seg, ip2_seg in zip(ip1_list, ip2_list):
        if mask >= 8:
            if ip1_seg == ip2_seg:
                match_len += 8
                mask -= 8
            else:
                return match_len
        else:
            while ip1_seg & 128 == ip2_seg & 128 and mask > 0:
                match_len += 1
                ip1_seg <<= 1
                ip2_seg <<= 1
                mask -= 1
            return match_len


def find_ip(ip, ip_masks):
    max_ip, max_len = None, 0

    for ip_mask in ip_masks:
        dst_ip, mask = ip_mask.split("/")
        match_len = match(ip, dst_ip, int(mask))
        if match_len > max_len:
            max_ip = ip_mask
            max_len = match_len

    return max_ip

if __name__ == "__main__":
    ip = "192.168.0.3"
    ip_masks = ["10.166.50.0/23", "192.0.0.0/8", "10.255.255.255/32", "192.168.0.1/24", "127.0.0.0/8",
                "192.168.0.0/24"]
    print(find_ip(ip, ip_masks))

