from tabulate import tabulate
print(tabulate([['Alice', 24], ['Bob', 19]], headers=['Name', 'Age'], tablefmt='orgtbl'))

def print_table(data, cols, wide):
    '''Prints formatted data on columns of given width.'''
    n, r = divmod(len(data), cols)
    pat = '{{:{}}}'.format(wide)
    line = '\n'.join(pat * cols for _ in range(n))
    last_line = pat * r
    print(line.format(*data))
    print(last_line.format(*data[n*cols:]))