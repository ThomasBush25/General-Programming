########################################################
# Thomas Bush
# Punnett Square
# Python 3.7.0
# For use on a Bio Lab Assignment 
########################################################
# sets the header on the table
def headtex():
	head = '\\begin{table}[]\n\\centering\n\\caption{Punnett square}\n\\label{punnettsquare}\n'
	return head

# sets the width	
def width(c1, c2):
	w = '\\begin{tabular}{l|' + 'l'*max(len(c1), len(c2)) + '}\n\\hline\n'
	return w

# sets the header
def freqhead():
	freqhead = '\\begin{table}[]\n\\centering\n\\caption{Genotypes frequencies}\n\\label{genotypesfreq}\n\\begin{tabular}{ll}\n\\hline\nGenotypes & Frequencies \\\ \\hline'
	return freqhead

# sets footer		
def foottex():
	foot = '\n\\end{tabular}\n\\end{table}'
	return foot
		
# finds all possible combinations of alleles a parent can pass on to their offspring
def get_all_combinations(parent):
	if len(parent) == 1:
		return [parent[0][0], parent[0][1]]
	else:
		genlist = []
		for x in get_all_combinations(parent[1:]):
			genlist.append(parent[0][0] + x)
			genlist.append(parent[0][1] + x)
		return genlist

# makes rows to put in tables
def make_row(genotype, allele):
	row = []
	for a in genotype:
		row.append(a + allele)
	return row
    
# generates table
def make_table(parent1, parent2):
	table = []
	for a in parent1:
		table.append(make_row(parent2, a))
	return table

# formats and prints Punnett square
def print_table(table, c1, c2): 
	latextable = []
	divlength = (len(c1[0])*2+4)*2**(len(c1[0]))
	print('')
	print('', end=' ')
	for a in c2:
		print(' '*(len(c1[0])+3) + a + '', end=' ')
		latextable.append('& ' + a + ' ')
	print('\n' + ' '*(len(c1[0])+1) + '-'*(divlength))
	latextable.append('\\\ \n\\hline\n')
	
	for i, row in enumerate(table):
		print(c1[table.index(row)], end=' ')
		latextable.append(c1[table.index(row)] + ' & ')
		print('|', end=' ')
		for j, cell in enumerate(row):
			print(cell + ' | ', end=' ')
			if j != len(row)-1:
				latextable.append(cell + ' & ')
			else:
				latextable.append(cell + ' ')
		print('\n' + ' '*(len(c1[0])+1) + '-'*(divlength))
		if i != len(table)-1:
			latextable.append('\\\ \n')	
	return latextable		

# calculates frequencies for each genotype present in table
def print_genotype_frequencies(table):
	freqtable = []
	freqtable.append('\n')
	calculated = []
	genotypes = [a for b in table for a in b]
	for k, x in enumerate(genotypes):
		count = 0
		for y in genotypes:
			if sorted(x) == sorted(y):
				count += 1
		if sorted(x) not in calculated:
			print("The frequency of the " + x + " genotype is " + str(float(count)/float((len(genotypes)))*100) + "%.")
			freqtable.append(x + ' & ' + str(float(count)/float((len(genotypes)))*100) + '\\% \\\ \\hline \n')	
		calculated.append(sorted(x))
	return freqtable

# welcome message
print('') 
print('|----------   Punnett Square Maker   ----------|')
print('|                                              |') 
print('|     Enter the genotypes of each parent.      |')
print('|  There should be two alleles for each gene.  |')
print('|  Each allele is represented by one letter.   |')
print('|                                              |') 
print('|----------------------------------------------|')
print('')

###########################################################
# main part of program
###########################################################
while True:
	p1 = input("Please enter the genotype of the first parent: ").split(' ')
	p2 = input("Please enter the gentype of the second parent: ").split(' ')
	c1 = get_all_combinations(p1)
	c2 = get_all_combinations(p2)
	a = make_table(c1, c2)
	latextable = print_table(a, c1, c2)
	freqtable = print_genotype_frequencies(a)
	print('')

	action = input("Type restart to restart and add another table.\n")
	if action == "restart":
		print('')
		print("Restart.\n")
	else:	
		quit()




