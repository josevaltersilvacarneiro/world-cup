"""The functions and procedures of this file
are responsible for sorting the classifica-
tion of the World Cup.

"""

def _sort_object(classification : dict, key : str) -> None:
    """The Cpython Compiler uses the Tim Sort Algorithm to
    order. By using it, the code becomes simpler and more
    efficient.

    """

    for group in classification.values():
        group.sort(key=lambda game : game[key], reverse=True)

def sort_classification(classification : dict, *args) -> None:
    
    # To sort according to FIFA, it has to be done in reverse order

    for key in reversed(args):
        _sort_object(classification, key);

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

