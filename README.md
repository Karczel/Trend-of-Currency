# Trend of Currency

Ui to see similarity in currency trend to see connections between each currency

## Note:
if tk combobox choices went beyond window span,  <br/>
move the tk screen down so that it will display combobox choices upwards instead of downwards. <br/>
### There are 2 places that will require some time to load:
* Open for the first time per session.
* Changing the main currency in first page.
But other than that, other features shouldn't take longer than a minute.

## How to install
In your terminal, do the following: <br/>
``` 
git clone https://github.com/Karczel/Trend-of-Currency
 ```

## How to run:
### Go to Project directory: <br/>
``` 
cd <cloned project directory>
 ```
to get ```<cloned project directory>```;
find your cloned project and get its directory from its properties.

### Create a virtual environment: <br/>
Mac: <br/>
``` 
python -m venv env
 ```

Windows: <br/>
```
.\env\Scripts\activate (concept)
```
```
. env/bin/activate
```

### Install all requirements in requirements.txt: <br/>
``` 
pip install -r requirements.txt
 ```

### run app.py in your Python virtual environment:<br/>
```
python3 app.py
```

## References to project documents.  This is a section with links to wiki docs. Include links to:
* Project Proposal
* Development Plan - what you will do each week and a milestone for that week's work
* UML diagrams of the design

## References

### Dataset: <br/>
[Foreign Exchange Rates 2000-2019](https://www.kaggle.com/datasets/brunotly/foreign-exchange-rates-per-dollar-20002019)<br/>


### Coding References:<br/>

[Pages code](https://stackoverflow.com/questions/14817210/using-buttons-in-tkinter-to-navigate-to-different-pages-of-the-application)<br/>

[Rolling slope code](https://stackoverflow.com/questions/42138357/pandas-rolling-slope-calculation)<br/>

[Tree column](https://stackoverflow.com/questions/44331033/python-tkinter-treeview-column-sizes)<br/>

[Linked tree view](https://stackoverflow.com/questions/61404261/tkinter-selecting-an-item-from-a-treeview-using-single-click-instead-of-double)<br/>

[Draw graph](https://matplotlib.org/2.0.2/examples/user_interfaces/embedding_in_tk.html)<br/>

[Correct treeview output](https://stackoverflow.com/questions/34166030/obtaining-last-value-of-dataframe-column-without-index)<br/>

[Image Button](https://www.youtube.com/watch?v=6VbzpWL49Q4)<br/>

[Charts in tkinter window](https://datatofish.com/matplotlib-charts-tkinter-gui/)<br/>
