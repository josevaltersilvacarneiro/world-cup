"""The functions and procedures of this file
are responsible for sorting the classifica-
tion of the World Cup.

"""

from operator import itemgetter

def sort_classification(classification : dict, *args) -> None:
    """The Cpython Compiler uses the Tim Sort Algorithm to
    order. By using it, the code becomes simpler and more
    efficient.

    """
    
    for group in classification.values():
        group.sort(key=itemgetter(*args), reverse=True);

#-----------------------------------------------------------------#
#----------------------------- Tests -----------------------------#

if __name__ == '__main__':

    example = {
        'A' : [
                {'name' : 'Germany', 'pt' : 6, 'gd' : 4},
                {'name' : 'Japan', 'pt' : 6, 'gd' : 3},
            ],
        };

    # Before sorting it
    print(example);

    sort_classification(example, 'pt', 'gd');

    # After sorting it
    print(example);

