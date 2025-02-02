### Numpy Arrays

***Q: What are the `numpy` arrays? Why do we need them?***

`numpy` is one of the commonly used python modules/packages, which stands for numerical python. Numpy arrays are multidimensional arrays that are optimized for computing, especially for operations such as matrix multiplication.

To be able to use python modules, we first need to import them.
"""

# Commented out IPython magic to ensure Python compatibility.
import numpy as np
import pandas as pd

# The following two modules matplotlib and seaborn are for plots
import matplotlib.pyplot as plt
import seaborn as sns # Comment this if seaborn is not installed
# %matplotlib inline

# The module re is for regular expressions
import re

import warnings
warnings.filterwarnings('ignore')

"""### Pandas Dataframes

***Q: What are the*** `pandas` ***dataframes? Why do we need them? What is the crucial difference between numpy matrices and*** `pandas` ***dataframes?***

Pandas: an excellent tool to work with datasets

Dataframes: the central data structure of pandas library
- Evolved out of tables
- Most suitable for data manipulation tasks  

Pandas is built on top of numpy. The crucial difference between numpy matrices and pandas dataframes is that the columns in a Dataframe can be of different datatypes such as numerical, categorical, textual, etc.

First we load the [Titanic dataset from Kaggle](https://www.kaggle.com/c/titanic) stored in the `csv` file as a dataframe using [`read_csv`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_csv.html) function.
"""

df = pd.read_csv('https://raw.githubusercontent.com/AashitaK/datasets/main/titanic.csv')
df

"""As it turns out to be rather big dataset to display, we can comment the above cell by adding # in front of df and run it again to get rid of the output.

Next, let's check the numbers of rows and columns in the dataset.
"""

df.shape

"""So, the dataset consists of 891 rows and 12 columns.

We use `head()` function to peek into the first 5 rows (or any number of rows by using `head(n)`).
"""

df.head()
#df.tail(10)

"""The [Titanic dataset](https://www.kaggle.com/c/titanic) that we will explore today is sourced from a [Kaggle](https://www.kaggle.com/) beginner-level competition.  

Goal of the competition: To apply the tools of machine learning to predict which passengers survived the Titanic tragedy.

[Description for the columns](https://www.kaggle.com/c/titanic/data) is as follows.  

|Variable|	Definition|	Key|   
|:---  |:--- |:---|
|PassengerId| Passenger ID |
|Survived| 	Survival|	0 = No, 1 = Yes |
|Pclass	|Ticket class|	1 = 1st, 2 = 2nd, 3 = 3rd|
|Sex	|Sex|
|Age	|Age in years	|
|SibSp	|# of siblings / spouses aboard the Titanic	|
|Parch	|# of parents / children aboard the Titanic	|
|Ticket	|Ticket number	|
|Fare	|Passenger fare	|
|Cabin	|Cabin number	|
|Embarked	|Port of Embarkation	|C = Cherbourg, Q = Queenstown, S = Southampton|

Q: What are the features?

Features are nothing but the variables in our model or the columns in our dataset. For example, `PClass`, `Age`, `Sex`, `Fare`, etc. are features for this particular dataset.

The final goal is to design a model to predict whether a passenger survives or not.
* Which of the above features seem like important predictors?
* How can you analyse the data in view of this objective?
    
Q: What is feature engineering?
* Detecting and handling missing values
* Encoding categorial features into numerical values
* Creating new features from the existing ones

---

### 1. Selecting rows and columns from the dataframe

How do we select a column from the dataframe? Say, we want to select the *Name* column from the dataframe.

Remember, we used square brackets for indexing lists, strings and numpy arrays in Python, for example `A[0]`.
"""

df['Name'].head()

"""Since we do not want all the rows in the output, we have used `head()` function at the end.

How do we select **multiple columns**? Suppose we want to select the columns *Name, Sex* and *Age* from the dataframe. Hint: Use a list of columns inside the square brackets.
"""

L=['Name', 'Age', 'Sex']
df[L]
#df[['Name', 'Age', 'Sex']]

df[['Name', 'Age', 'Sex']]

"""We can also select **rows** by putting a certain **condition on a column**. Say, we want only those rows for which the gender is *'female'*."""

df[df["Sex"] == "female"].head(3)

"""Now, we want to retrieve only the female passengers traveling in the first class. Hint: Add another conditional `df['Pclass']==1` to the above code using the operator `&` and make sure to wrap the two conditionals with parenthesis `()`."""

df[(df["Sex"] == "female")&(df["Pclass"]==1)]
df[(df["Sex"] == "female")&(df["Pclass"]==1)].shape[0] #number of rows
df[(df["Sex"] == "female")&(df["Pclass"]==1)].shape[1] #number of columns

"""We can also get the number of passengers using the shape method which gives us both the number of columns and the number of rows. Write the code to count the number of female passengers traveling in the first class."""



"""#### The `loc` and `iloc` methods
So far, we have seen how to retrieve:
* some select columns, or
* certain rows based on conditionals.

What if we want to slice off a portion of the dataframe with some specific rows **and** columns? We use `.loc[]` or `.iloc[]` methods for this purpose.
* `.iloc[]` method is primarily integer position based and gets rows/columns at particular positions in the index (so it **only takes integers** as index).
* `loc[]` method is label based and gets rows/columns with particular labels from the index. Thus, it can be used to **put conditions on rows and retrieve select columns simultaneously**.

For example, we want to get the name and the survival information for all the adults above 70 years.
"""

df.loc[df['Age']>70, ['Name', 'Survived']]

"""Write the code to retrieve the **name, age and survival** information for all the **female passengers traveling in the first class**."""

#df.loc[(df[["Sex"] == 'female') & (df['Pclass'] == 1)], ['Name', 'Age', 'Survived']]

df.loc[(df["Sex"] == "female")&(df["Pclass"]==1),['Name', 'Age', 'Survived']]

"""The `iloc[]` method let us retrieve rows by passing sequence of indexes. For example, we can select the rows numbered 100th to 105th. The indexing works exactly like python lists and numpy arrays."""

df.iloc[100:106]

"""Write the code to retrieve every 100th row from the dataframe."""

df.iloc[0::100]

"""Write the code to retrieve the last 10 rows from the dataframe using `iloc[]` method."""

df.iloc[-10::]
#df.tail(10)
df.iloc[881:891]

"""---

## Instructions for the exercise session:
- There are two exercise sections (section 2 and 3) below and they are alloted 45 min and 30 min respectively.
- The exercise involves new concepts not covered in the guided session above. Please feel free to ask questions and take help from me and/or your peers in the breakout room.
- The hints are provided for the each of the exercises. The built-in functions to be used for them are provided with a clickable link to the user manual.
- The exercise sessions are time-bound and you are encouraged to work in groups to speed things up!
- If you finished a section early, move on to the next one. There is an optional section 4 at the end.

---

### 2. Exploring the dataset (45 min)

Use [`describe`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.describe.html) function for numerical features (columns) to get a brief overview of the statistics of the data.
"""

df.describe()

"""Do the same as above for qualitative (non-numerical) features. Hint: Use `include=['O']` parameter in the [`describe`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.describe.html) function."""

df.describe(include=['O'])

""" Use the built-in pandas function to count the number of surviving and non-surviving passengers. Hint: Use [`value_counts()`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.value_counts.html) on the column `df['Survived']`."""

df.value_counts('Survived')
#df['Survived'].value_counts()

"""Below is a pie chart of the same using `matplotlib`:"""

plt.axis('equal')
plt.pie(df['Survived'].value_counts(), labels=('Died', "Survived"));
plt.show()

"""Below is a bar chart for the survival rate among male and female passengers using `seaborn` which we imported above as `sns`. Here is [Seaborn cheatsheet](https://s3.amazonaws.com/assets.datacamp.com/blog_assets/Python_Seaborn_Cheat_Sheet.pdf)."""

sns.barplot(x = 'Sex', y = 'Survived', data = df);
plt.show()

df.head()

"""Plot the survival rate among passengers in each ticket class."""

sns.barplot(x = 'Pclass', y = 'Survived', data = df);
plt.show()

"""We can also check the survival rate among both genders within the three ticket classes as follows."""

sns.barplot(x='Pclass', y='Survived', hue='Sex', data=df);

"""From the above chart, do you think that the gender affect the chance of survival for all the three ticket classes equally? Or does it seem like gender's effect is more pronounced for a certain ticket class passengers than others? We plot the  point estimates and confidence intervals for each sub-category to see it more clearly."""

sns.pointplot(x='Sex', y='Survived', hue='Pclass', data=df);

"""Notice the steeper slope for the second class.

It seems that gender and ticket class put together give more information about the survival chance than both of them separately. Please feel free to later explore other variables and combination of variables in depth in your own time.

How many children were on board? Hint: Use indexing on rows using conditional on the *Age* column and then the [`shape`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.shape.html) method to count the rows as seen above.
"""

#df["Age"]<18.shape
#df["Age"]<18
#df.head()
#df[df["Age"]<=18, ["Name", "Age", "Survived"]]
df[df["Age"] <= 18].shape

"""How many of the children on board survived? Hint: Add another conditional for the *Survived* column to the above code."""

df[(df["Age"] <= 18) & (df["Survived"] == 1)].shape

"""Use the functions [`isnull()`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.isnull.html) and [`sum()`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.sum.html) chained one after the other on the dataframe to find out the number of missing values in each column."""

df.isnull().sum()

"""**Detecting missing values** is an important first step in Feature Engineering, that is preparing the features (independent variables) to use for building the machine learning models.

The next step is **handling those missing values**. An option is to drop the rows or columns that have some or a lot of missing values, but that also means discarding relevant information. Another option is to fill them with something appropriate.

Discuss:
1. What are the pros and cons of dropping the rows and/or columns with missing values?
    - Should you drop none, all or some of the columns with missing values for this dataset in view of building the predictive model?
    - Ditto for rows with missing values.
3. If you consider filling the missing values, what are the possible options?
    - Can you make use of other values in that column to fill the missing values?
    - Can you make use of other values in that row as well as values in that column to fill the missing values
4. Can the title in the name column be used for guessing a passengers' age based on the age values of other passengers with the same title?

What is the most common port of embarkment? Hint: Check the frequency (counts) of each value in the Embarked column using the built-in function [`value_counts()`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.value_counts.html) as seen above.
"""

df.head()

"""As we saw above, there are missing values in the column for *Embarked*. Fill them with the most commonly occuring value. Hint: Use [`fillna()`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.fillna.html)."""

df["Embarked"].fillna("S", inplace=True)

"""Let us check whether the missing values for the *Embarked* column is indeed filled."""

df.isnull().sum()

"""If not, there are two options to fix this. One is to set `inplace` parameter in the `fillna()` function as `True` and another is to use assignment operator `=` as in `df = df.function()`.

***Question***: Why is the `inplace` keyword False by default? This is true not just for `fillna()` but for most built-in functions in pandas.

Answer: To facilitate method chaining or piping i.e. invoking multiple operations one after the other. For example, `df.isnull().sum()` used above. Chaining is more commonly used in pandas as compared to another programming style i.e. using nested function calls. Please read more [here](https://towardsdatascience.com/the-unreasonable-effectiveness-of-method-chaining-in-pandas-15c2109e3c69), if interested.

We should remove the *Cabin* column from the DataFrame -- too many values are missing. Hint: Use [`drop()`](https://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.drop.html) with appropriate value for the `axis` keyword.
"""

df.drop("Cabin", axis=1, inplace=True)
#df.isnull().sum()
#df.head()

"""Let us check whether the column is indeed dropped. If not, modify the code above accordingly."""

df.head()

"""What is the age of the oldest person on board?"""

df.loc[df['Age'].idxmax(), "Age"]

"""Find all the passenger information for the oldest person on board. Hint: Use [`loc[]`](https://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.loc.html) method with [`idxmax()`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.idxmax.html) for the Age column."""

df.loc[df['Age'].idxmax()]

"""---

### 3. Feature Engineering: Creating a new column for the titles of the passengers (30 min)

The real-world datasets many-a-times contain useful information in the textual format. Text mining is an important area of data science and one of the most powerful tool is [regular expressions](https://www.gnu.org/software/sed/manual/html_node/Regular-Expressions.html) that are not specific to python, but have much wider applications.

In this section, you are going to create a new feature for the titles of the passengers derived from their names using regular expressions. For that, let us first take a look at the passengers' names.
"""

df.loc[:20, 'Name'].values
#df.loc[20:,"Age"].values

"""We notice one of the identifying characteristics of the titles above are that they end with a period. Regular expressions are very useful in the process of such data extraction and we will use them using the python module `re` to extract the titles from the *Name* column. We will first use regular expressions characters to construct a pattern and then use built-in function `findall` for pattern matching.

Some useful regular expression characters:
- `\w`: pattern must contain a word character, such as letters.
- `[ ]`: pattern must contain one of the characters inside the square brackets. If there is only one character inside the square brackets, for example `[.]`, then the pattern must contain it.

Let's try this.
"""

re.findall("\w\w[.]", 'Braund, Mr. Owen Harris')

"""It worked! It returned a list instead of the string, so we use indexing to get the first element of the list."""

re.findall("\w\w[.]", 'Braund, Mr. Owen Harris')[0]

"""Let us try it on another name:"""

re.findall("\w\w[.]", 'Heikkinen, Miss. Laina')[0]

"""So, we want a pattern that automatically detects the length of the title and returns the entire title.

For regular expressions, \+ is added to a character/pattern to denote it is present one or more times. For example, `\w+` is used to denote one or more word characters. Fill in the regular expression in the below cell that will detect a period preceeded by one or more word characters.
"""

# Fill in below:
re.findall("\w\w+[.]", 'Heikkinen, Miss. Laina')[0]

"""The output should be `'Miss.'`

Summary: For pattern matching the titles using regular expressions:
- First we make sure it contains a period by using `[.]`.
- Secondly, the period must be preceeded by word characters (one or more), so we use `\w+[.]`.

Write a function `get_title` that takes a name, extracts the title from it and returns the title.
"""

def get_title(x):
  return re.findall("\w\w+[.]",x)[0]

"""Check that the function is working properly by running the following two cells."""

get_title('Futrelle, Mrs. Jacques Heath (Lily May Peel)')

"""The output should be `'Mrs.'`. Note: Make sure that the funtion returns a string and not a list. Please modify the above function accordingly."""

get_title('Simonius-Blumer, Col. Oberst Alfons')

"""The output should be `'Col.'`.

Create a new column named Title and extract titles from the Name column using the above function `get_title`. Hint: Use built-in [`map()`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.map.html) function. The syntax is `df['New_column'] = df['Relevant_column'].map(function_name)`.
"""

df['Title'] = df['Name'].map(get_title)

"""Let us peek into the dataframe."""

df.head()

"""List all the unique values for the titles along with their frequency. Hint: Use an inbuilt pandas function"""

df["Title"].value_counts()

"""Now, we want to replace the various spellings of the same title to a single one. Hint: Use the below dictionary with the [`replace`](https://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.replace.html) function

`title_dictionary = {'Ms.': 'Miss.', 'Mlle.': 'Miss.',
              'Dr.': 'Rare', 'Mme.': 'Mrs.',
              'Major.': 'Rare', 'Lady.': 'Rare',
              'Sir.': 'Rare', 'Col.': 'Rare',
              'Capt.': 'Rare', 'Countess.': 'Rare',
              'Jonkheer.': 'Rare', 'Dona.': 'Rare',
              'Don.': 'Rare', 'Rev.': 'Rare'}`
"""

title_dictionary = {'Ms.': 'Miss.', 'Mlle.': 'Miss.', 'Dr.': 'Rare', 'Mme.': 'Mrs.', 'Major.': 'Rare', 'Lady.': 'Rare', 'Sir.': 'Rare', 'Col.': 'Rare', 'Capt.': 'Rare', 'Countess.': 'Rare', 'Jonkheer.': 'Rare', 'Dona.': 'Rare', 'Don.': 'Rare', 'Rev.': 'Rare'}
df.replace({"Title": title_dictionary}, inplace=True)

"""List all the unique values for the titles along with their frequency to check that the titles are replaced properly."""

df["Title"].value_counts()

"""What is the median age of passengers? Hint: Use the inbuilt function [`median`](http://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.median.html)."""

df["Age"].median()

"""What is the median age of passengers with the title 'Miss.'? Hint: Use [`loc[]`](https://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.loc.html) method for slicing off the select rows and the *Age* column."""

df.loc[df["Title"] == "Miss.", 'Age'].median()

"""What is the median age of passengers with the title 'Mrs.'?"""

df.loc[df["Title"] == "Mrs.", 'Age'].median()

"""Is there a noticeble difference in the median ages for the passengers with the above two titles? Should we take titles into account while filling the missing values for the *Age* column? If yes, how?

This is the end of the exercise session. If you finished early, move on to the next notebook for merging datasets.

---

#### Acknowledgment:
* [Titanic dataset from Kaggle](https://www.kaggle.com/c/titanic) dataset openly available in Kaggle is used in the exercises.
"""
