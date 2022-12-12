"""The functions and procedures of this file
are responsible for sorting the classifica-
tion of the World Cup.

"""

def _insertion_sort(classification : dict, key : str) -> None:

    # Reference
    # https://pt.wikipedia.org/wiki/Insertion_sort

    for group in classification.values():

        length : int = len(group);

        for i in range(length):
            current = group[i];
            j = i - 1;

            while j >= 0 and group[j][key] < current[key]:
                group[j+1] = group[j];
                j-= 1;

            group[j+1] = current;

def sort_classification(classification : dict, *args) -> None:
    
    # To sort according to FIFA, it has to be done in reverse order

    for key in reversed(args):
        _insertion_sort(classification, key);

#-----------------------------------------------------------------#
#----------------------------- Tests -----------------------------#

if __name__ == '__main__':

    example = {
        'A' : [
                {'name' : 'Germany', 'pt' : 4, 'gd' : 2},
                {'name' : 'Japan', 'pt' : 6, 'gd' : 3},
            ],
        };

    # Before sorting it
    print(example);

    sort_classification(example, 'gd', 'pt');

    # After sorting it
    print(example);

