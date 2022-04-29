
### 安装 pip install csvkit

### 文档地址 
```angular2html
https://csvkit.readthedocs.io/en/latest/index.html
```
### 以下操作需要在终端执行

### Convert Excel to csv
```angular2html
in2csv data.xls > data.csv
```

### Convert JSON to CSV
```angular2html
in2csv data.json > data.csv
```

### Print column names
csvcut -n data.csv

Select a subset of columns:
```angular2html
csvcut -c column_a,column_c data.csv > new.csv
```

### Reorder columns:
```angular2html
csvcut -c column_c,column_a data.csv > new.csv
```
### Find rows with matching cells:

```angular2html
csvgrep -c phone_number -r "555-555-\d{4}" data.csv > new.csv
```

### Convert to JSON:
```angular2html
csvjson data.csv > data.json
```

### Generate summary statistics:
```angular2html
csvstat data.csv
```

### Query with SQL:
```angular2html
csvsql --query "select name from data where age > 30" data.csv > new.csv
```

### Import into PostgreSQL:
```angular2html
csvsql --db postgresql:///database --insert data.csv
```

### Extract data from PostgreSQL:
```angular2html
sql2csv --db postgresql:///database --query "select * from data" > new.csv
```


