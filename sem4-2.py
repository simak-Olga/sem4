#задача 2 . Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.
def getnumbers(seq):
   listing = []
   for i in seq:
        if i not in listing:
            listing.append(i)
    return listing

def main():
    seq = [1, 2, 3, 4, 5]
    listing = getnumbers(seq)
    print(listing)

    
if __name__ == "__main__":
    main()
