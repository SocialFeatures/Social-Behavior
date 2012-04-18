'''
Compile messages for each pair users in input file

Output to standard out in format:
<sender> <recipient> <text1> <text2> ...

usage: python A_to_B_messages.py <sorted_message_text_file>

Input file should be in format:
<sender> <recipient> <text>

Message text file must be sorted
Sorting can be done with the unix sort command as follows:
sort -k1n,1 -k2n,2 <message_text_file> > <sorted_message_text_file>

Original message text file can be generated by using extract_from_json.py
with a fields file with the line:
user:id in_reply_to_status_id text
and input being the json files that contain the statuses

'''

import sys

def from_to(line):
	columns = line.split(' ')
	return columns[0]+' '+columns[1]

def message_text(line):
	text = line[line.find(' ')+1:]
	return text[text.find(' ')+1:].strip()
	
def is_undirected(line):
	users = from_to(line)
	return users[users.find(' '):]==' None'
	
	
def main(argv):
	filename = argv[0]
	current = ''
	to_print = 'first'
	for line in open(filename):
		if not line.strip(): continue
		if is_undirected(line): continue
		if from_to(line) == current:
			print to_print,
			print '  '+message_text(line),
			to_print = ''
		else: to_print = '\n'+from_to(line)+'  '+message_text(line)
		current = from_to(line)

if __name__ == '__main__':
    main(sys.argv[1:])