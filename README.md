# Babysitter Kata

## Run unit tests:
```bash
$ python -m unittest discover
.....................
----------------------------------------------------------------------
Ran 21 tests in 0.001s

OK

```

## Run application:
```bash
$ python babysitter.py START_TIME END_TIME FAMILY

    python babysitter.py start end family

    start	start time between 5:00pm and 4:00am.	 ex. 7:00pm
    end		endtime between 5:00pm and 4:00am.	 ex. 1:00am
    family	family a, b, or c.			 ex. c
	
		
$ python babysitter.py 5:00pm 10:00pm a
You should charge $75 for family a if you started at 5:00pm and ended at 10:00pm
```


## There are no external dependancies. This was built using python 3.7.3, but should work with any 3.x version of python
