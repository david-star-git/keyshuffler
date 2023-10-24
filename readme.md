# Password Generator

A Python script for generating random passwords with custom options.

## Language Versions
[![English](https://img.shields.io/badge/English-English-blue)](readme.md)
[![German](https://img.shields.io/badge/Deutsch-German-blue)](readme_de.md)
[![Spanish](https://img.shields.io/badge/Español-Spanish-blue)](readme_es.md)

## Introduction

This Python script allows you to generate random passwords with specific options, such as password length and the inclusion of extended character sets. You can use this tool to create strong and secure passwords for your applications or accounts.

## Features

- Generate random passwords with a specified length.
- Include extended character sets for stronger passwords.
- Customize character sets to meet your requirements.

## Getting Started

### Prerequisites

To use this script, you need to have Python installed on your system. You can download and install Python from the official website: [Python Downloads](https://www.python.org/downloads/).

### Installation

1. Clone the repository to your local machine using the following command:

    ```bash
    git clone https://github.com/david-star-git/keyshuffler.git
    ```

2. Change the working directory to the project folder:

    ```bash
    cd KeyShuffler
    ```

3. Run the script with the desired options (see [Usage](#usage)).

## Usage

To generate a password, run the script with the following command:

```bash
python password_generator.py
```

By default, this will generate a 50-character password with only standard ASCII characters. You can customize the password length and character set using the following options:

- **-l** or **--length**: Specify the length of the password.
- **-e** or **--extended**: Include extended character set for stronger passwords.

Example usages:

- Generate a 12-character password with extended characters:

```bash
python password_generator.py -l 12 -e
```

## Customization

You can customize the character sets used for normal and extended characters by editing the `normal_chars` and `extended_chars` variables inside the script. The default values provide a reasonable set of characters for generating passwords, but you can modify them to suit your needs.

```py
normal_chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_+=-[]{}|;:'\"<>,.?/~"
extended_chars = " ¡⅛£¤⅜⅝⅞™±°¿˛¯˘˚ÞØı↑¥Ŧ®€§ΩÆẞÐªŊĦ ̇&Ł ̣ˇ—÷×º’‘‚©‹›ˍ|»«¢„“”µ·…–^˝łĸ ̣ħŋđðſæ@ſ€¶ŧ←↓→øþ¨’¸\}][{¬½¼³²¹⁴⁵⁶⁷⁸⁹⁰}]"
```

## License

This project is licensed under the [GNU General Public License, version 3.0](LICENSE). You can find the full license text [here](https://www.gnu.org/licenses/gpl-3.0.html).