# Day 25 – Reading CSV Files (File I/O, csv, and pandas)
## 📘 Overview
Today I explored multiple ways to read and process CSV files in Python, including:

- Basic file reading with .readlines()

- Using the csv module to parse rows

- Using the pandas library for powerful DataFrame operations and CSV handling
------------------

### 📂 File: main.py
#### 🔧 Tasks Performed
**📄 Using File I/O (.readlines())**
- Opened and read raw lines from a CSV file (weather_data.csv).

- Stripped the header row manually using pop(0).

**📄 Using the csv module**
- Parsed the CSV data row-by-row.

- Extracted temperature values and converted them to integers.

- Calculated average temperature manually from the list.

**🐼 Using pandas**
- Loaded CSV into a DataFrame with pandas.read_csv().

- Explored data using:

    - data["temp"], data.condition, and row filtering

    - Mean and max temperature calculations

- Filtered rows based on conditions (e.g., "Monday", max temp).

- Converted temperatures to Fahrenheit.

- Created and saved a new DataFrame to new_data.csv.
--------------

### 📂 File: squirrel-count.py
**🔧 Tasks Performed**
- Read the 2018 Central Park Squirrel Census CSV into a DataFrame.

- Extracted the Primary Fur Color column.

- Counted the number of squirrels by fur color: Gray, Cinnamon, and Black.

- Created a summary DataFrame from the counts and printed it.

### 📊 Output Format
```bash
     Fur  Count
0   grey    ###
1    red    ###
2  black    ###
```