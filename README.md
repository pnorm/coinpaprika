## Recruitment Task - backend internship

Hi!
This is my solution of the recruitment task posted at
https://git.profil-software.com/recruitment-03-2021/recruitment-task-backend-internship

**Bonus tasks**
  - --coin parameter for specifying other types of cryptocurrencies (default **btc-bitcoin**),


#### 1. Clone repository
```sh
$ git clone https://github.com/pnorm/coinpaprika.git
```

#### 2. Create and activate virtual environment
```sh
~/coinpaprika$ python3 -m venv env
~/coinpaprika$ source env/bin/activate
```
#### 3. Install requirements
```sh
(env):~/coinpaprika$ pip install -r requirements.txt
```
### 4. Examples how to use script

 #### 4.1. Calculate average price of currency by month for given period.
 - Example 1
```sh
(env):$ python script.py average-price-by-month --start-date=2020-02 --end-date=2020-03

Date 	 Average Price ($)
2020-02  9663.33833
2020-03  6884.02536
```
 - Example 2
```sh
(env):$ python script.py average-price-by-month --start-date=2020-02 --end-date=2020-03 --coin=eth-ethereum

Date 	 Average Price ($)
2020-02  239.12726
2020-03  160.41598
```
 -  **the commands below throw exceptions**
 - Example 3
```sh
(env):$ python script.py average-price-by-month --start-date=2020-02-01 --end-date=2020-03-01

Invalid date pattern
```
 - Example 4
```sh
(env):$ python script.py average-price-by-month --start-date=2020-02 --end-date=2020-03 --coin=eth-ether

Sorry, we don't have that coin.
```
 - Example 5
```sh
(env):$ python script.py average-price-by-month --start-date=2020-02 --end-date=2020-01

Start date can't be after end date.
```
#### 4.2. Find longest consecutive period in which price was increasing.
 - Example 1
```sh
(env):$ python script.py consecutive-increase --start-date=2020-02-01 --end-date=2021-01-01 --coin=eth-ethereum

<<< Longest consecutive period was from 2020-04-21 to 2020-04-29 with increase of $43.62 >>>
```
 - **the commands below throw exceptions**
 - Example 2
```sh
(env):$ python script.py consecutive-increase --start-date=2020-01-01 --end-date=2021-03-01

You can fetch max 366 rows in one request. Change date range.
```
 - Example 3
```sh
(env):$ python script.py consecutive-increase --start-date=2020-02-01 --end-date=2019-01-01 --coin=eth-ethereum

Start date can't be after end date.
```
 - Example 4
```sh
(env):$ python script.py consecutive-increase --start-date=2020-02-01 --end-date=2020-02-01 --coin=eth-ethereum

There is no increase in a given period of time.
```
#### 4.3. Export data for given period in one of selected format csv or json.
 - Example 1
```sh
(env):$ python script.py export --start-date=2020-02-01 --end-date=2021-01-01 --coin=eth-ethereum --format=csv --file=test

Data successfully saved to the CSV file.

(env):$ ls data
eth-ethereum_test.csv
```
 - Example 2
```sh
(env):$ python script.py export --start-date=2020-02-01 --end-date=2021-01-01 --coin=eth-ethereum --format=json --file=test

Data successfully saved to the JSON file

(env):$ ls data
eth-ethereum_test.csv  eth-ethereum_test.json
```
 - Example 3
```sh
(env):$ python script.py export --start-date=2020-02-01 --end-date=2021-01-01 --coin=eth-ethereum --format=txt --file=test

You can export only to csv or json.
```
### Json structure
```json
[
    {
        "Date": "2020-02-01",
        "Price": 183.93398133
    },
    {
        "Date": "2020-02-02",
        "Price": 188.6811418
    }
 ]
```

### CSV structure
```
Date,Price
2020-02-01,183.93398133
2020-02-02,188.6811418
2020-02-03,190.33774687
2020-02-04,189.10232025
```
