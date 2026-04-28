import csv
rows=[['name','age'],['Alice',22],['Bob',25]]
with open('users.csv','w',newline='') as f:
    import csv
    writer=csv.writer(f)
    writer.writerows(rows)