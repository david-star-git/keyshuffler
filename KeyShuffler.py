import argparse
import string
import random

def generate_password(length, extended=False):
    normal_chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_+=-[]{}|;:'\"<>,.?/~"
    extended_chars = " ¡⅛£¤⅜⅝⅞™±°¿˛¯˘˚ÞØı↑¥Ŧ®€§ΩÆẞÐªŊĦ ̇&Ł ̣ˇ—÷×º’‘‚©‹›ˍ|»«¢„“”µ·…–^˝łĸ ̣ħŋđðſæ@ſ€¶ŧ←↓→øþ¨’¸\}][{¬½¼³²¹⁴⁵⁶⁷⁸⁹⁰}]" if extended else ""
    characters = normal_chars + extended_chars

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    parser = argparse.ArgumentParser(description="Generate a random password")
    parser.add_argument("-l", "--length", type=int, default=50, help="Length of the password")
    parser.add_argument("-e", "--extended", action="store_true", help="Use extended character set")

    args = parser.parse_args()
    password = generate_password(args.length, args.extended)
    print(password)

if __name__ == "__main__":
    main()
