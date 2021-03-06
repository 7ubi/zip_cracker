# ZIP CRACKER

## Description

A tool to get the password of a password-protected zip file.

## Disclaimer

This project was made for educational purposes only! 

## Install requirements

1. Navigate to the projects' location in the console.

```
cd path/to/this/project
```

2. Run this command to install all requirements.

```
pip install -r requirements.txt
```


## How to use

1. Run this command to get the password with a password list.

```
python zip_cracker.py [Path and name of the zip file] [Path and name of the password list]
```

2. Run this command to get the password with bruteforce without using a password list.

```
python zip_cracker.py [Path and name of the zip file]
```

## Credit

- Provided password list by [SecLists](https://github.com/danielmiessler/SecLists/blob)
  - MIT License

    Copyright (c) 2018 Daniel Miessler
    
    Permission is hereby granted, free of charge, to any person obtaining a copy
    of this software and associated documentation files (the "Software"), to deal
    in the Software without restriction, including without limitation the rights
    to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
    copies of the Software, and to permit persons to whom the Software is
    furnished to do so, subject to the following conditions:
    
    The above copyright notice and this permission notice shall be included in all
    copies or substantial portions of the Software.
    
    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
    IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
    FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
    AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
    LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
    OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
