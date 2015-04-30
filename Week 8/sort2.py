def swap(items, first_index, second_index):
	temp = items[first_index]
	items[first_index] = items [second_index]
	items[second_index] = temp

def selection_sort(numbers):
	for i in range(len(numbers)):
		least = i
		for j in range(i + 1, len(numbers)):
			if numbers[j] < numbers[least]:
				least = j

		swap(numbers,least,i)

a = [1,3,-2,55,12]
selection_sort(a)
print(a)

#Imame spisuk s elementi


#I bez da triem elementite trqbva da gi razmestim taka
# Che da sa ot mai malkoto do nai golqmoto