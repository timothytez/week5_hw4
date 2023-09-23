# You probably know the "like" system from Facebook and other pages.
    #People can "like" blog posts, pictures or other items. 
    #We want to create the text that should be displayed next to such an item.

    # Implement the function which takes an array containing the names of people that like an item.
    # The given array's names will always be valid, and will not contain any numbers or special characters.
    #  It must return the display text as shown in the examples:

    # []                                -->  "no one likes this"
    # ["Peter"]                         -->  "Peter likes this"
    # ["Jacob", "Alex"]                 -->  "Jacob and Alex like this"
    # ["Max", "John", "Mark"]           -->  "Max, John and Mark like this"
    # ["Alex", "Jacob", "Mark", "Max"]  -->  "Alex, Jacob and 2 others like this"
    # Note: For 4 or more names, the number in "and 2 others" simply increases.


def liked_ppl (alist):
    if len(alist) == 0:
        print ("no one likes this")
    elif len(alist)== 1:
        return f'{alist[0]} likes this'
    elif len(alist)== 2:
        return f'{alist[0]}, {alist[1]} likes this'
    elif len(alist)== 3:
        return f'{alist[0]}, {alist[1]}, {alist[2]} likes this'
    elif len(alist)>= 4:
        return f'{alist[0]}, {alist[1]} and {len(alist)-2} others likes this'
    
print(liked_ppl(["Max", "John", "Mark", "Sean"]))