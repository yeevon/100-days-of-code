# Coffee Machine ☕️
## 📘 Overview
A console-based coffee machine simulation that allows users to order drinks, insert coins, and receive change — all while tracking resources and total income.

---
## 🧠 Features
- Supports three drink types: espresso, latte, and cappuccino

- Tracks inventory: water, milk, and coffee

- Accepts coin input: quarters, dimes, nickels, and pennies

- Handles:

  - Payment and change

  - Insufficient funds

  - Resource shortages

- Displays a status report with report command

- Supports turning off the machine with off command

## 🧪 Example Use
```bash
What would you like? (espresso/latte/cappuccino): latte
Insert quarters: 10
Insert dimes: 0
Insert nickels: 0
Insert pennies: 0
Here is your change: $0.00
Here is your latte. Enjoy!
```

## 🗂️ Commands
|**Command**	|**Description**|
|--------------|-----------------|
|espresso	|Orders an espresso|
|latte	|Orders a latte|
|cappuccino	|Orders a cappuccino|
|report	|Prints current resources and money|
|off	|Turns off the machine|