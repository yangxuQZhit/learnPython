def drop_first_last(grades):
  first, *middle, last = grades
  return sum(middle)

if __name__ == '__main__':
  print(drop_first_last([2, 3, 4, 5, 6, 7]))
