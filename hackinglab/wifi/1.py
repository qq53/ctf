with open('pass.txt', 'a+') as dic:
  for year in range(1980, 2015):
    for mon in range(1, 13):
      for day in range(1, 32):
        print '%d%02d%02d' % (year, mon, day)
        dic.write('%d%02d%02d\n' % (year, mon, day))