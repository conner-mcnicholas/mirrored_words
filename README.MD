
# GOAL

This script finds the instances where 2 words require the same keystrokes, except mirroring left and right hand responsibilities           
	(i.e. 'p' corresponds with 'q', 'f' corresponds with 'j', etc)


Results are compiled for each of the available English words lists from MonkeyType.com as input           
	(i.e. 200, 1k, 5k, 10k, 25k, 450k)


## RESULTS



Using wordlist --> English_200.txt

	total # pairs: 0


Using wordlist --> English_1k.txt

	total # pairs: 1

	longest:4
	[['cell', 'miss']]

Using wordlist --> English_5k.txt

	total # pairs: 2

	longest:4
	[['miss', 'cell'], ['prey', 'quit']]

Using wordlist --> English_10k.txt

	total # pairs: 4

	longest:4
	[['dell', 'kiss'], ['miss', 'cell'], ['prey', 'quit']]

Using wordlist --> English_25k.txt

	total # pairs: 9

	longest:5
	[['swill', 'loess']]

Using wordlist --> English_450k.txt

	total # pairs: 357

	longest:7
	[['murkily', 'crudest'], ['sillily', 'lessest']]
