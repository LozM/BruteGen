# BruteGen
Python class for generating brute forced wordlists without writing them to disk.

Current iteration is stored internally in the class.

## Usage
### Init
`from brutegen import BruteGen`

`bg = BruteGen(min_len, max_len, charset_str)`

Example:

`charset = 'abcdefghijklmnopqrstuvwxyz0123456789'`

`bg = BruteGen(6,10,charset)`
### Get the next N number of words in sequence
`wordlist = bg.Next(10000)`

This process can be repeated until done with the follow

`while not bg.IsDone(): wordlist = bg.Next(n)`
### Reset the internal word counter
`bg.Reset()`
