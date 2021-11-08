# Overvierw
Each directory contains a distinct python script

## cell-phones-finder
This script reads input data from a file `system_logs.txt` and extracts any cell phone numbers that it finds.
The output is stored in a dynamically generated filed called `cell_phones.txt`

```
cd cell-phones-finder
python main.py
```


## streaming-service-cost-calculator
This script calculates the total cost for a list of track records in a music streaming service. 

The following rules are used for calculating the cost:
- Each track that is played for less than 3 minutes, is charged with 5 cents per second.
- Each track that is played for more than 3 minutes, is charged with 200 cents per minute (ignoring seconds).
- The track with the longest streaming duration has 50% discount.

```
cd streaming-service-cost-calculator
python main.py
```