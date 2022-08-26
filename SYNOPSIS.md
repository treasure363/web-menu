# Project Description
Our Project is based on Hotel Management using Web Application. In a self-serve waiterless restaurant, you can place your order using modern technology rather than physically placing it. Our project will be using a Website to present the Menu as well as Place your Order directly without any hustle. 

# Need
* Creating potential for improvement of existing services/practice
* Beneficial to the restaurants which lack labor services
* Reducing time consumption for overall process
* Minimizing the error percentage of the services
* Better crowd control for busy hours
* Easier to track and manage orders since we provide a Database
* The overall process becomes more simplified
* Go green, Reduces paper usage
  
# Language
* Python
* HTML
* CSS
* JavaScript

# Tech Stack
* Django Framework
* Django Models  
  Django Models are a level of abstraction on top of SQL that allow us to work with databases using Python classes and objects rather than direct SQL queries. We are using SQLite3 Database.
* ReactJS

# Working
Our project is mainly divided into 4 major Steps:
* Reaching the website via QR Scan/Manual URL
* Browsing through the menu virtually
* Placing the Order	
* Finalizing your order [Payment/Review]

-Reaching the website via QR Scan/Manual URL [1 Week]  
Customers will be able to scan the website through a QR Code placed on their Table. Otherwise, they can manually go to the provided URL on their browser.  

-Browsing through the menu virtually [3 Weeks]  
After reaching the website, users can explore different dishes according to their preference. Here we will be using a database to show different items. Users can filter, sort and select options to their preference.  

-Placing the order [2 Weeks]  
Users can add/delete items from cart which will be used to place their orders. They also have the options to modify the dish by including add-on, specific instructions and takeaway as per their preferences. They can place multiple orders.  

-Finalizing your order [Payment/Review] [1 Week]  
Users are given various payment methods to choose from. Users can submit their personal review of their experience.


# Database
<h2>User Table:</h2>
Column Overview:

| Attribute             | Description                           |
| --------------------- | ------------------------------------- |
| Username              | Set to the Table Number               |
| Password              | Random Hash Value                     |
| Cart                  | `Foreign Key` Linking `Cart` Table    |
| Order                 | If the last order[cart] has been placed succesfully|
| Amount                | Total bill to be paid                 |

<table>
    Table Overview:
    <tr>
        <th>Username
        <th>Password
        <th>Cart
        <th>*Order[Check]
        <th>Amount
    </tr>
    <tr>
        <td>String
        <td>String
        <td>List[Cart Foreign Key]
        <td>Boolean
        <td>Float
    </tr>
    <tr>
        <td>Table_6
        <td>6e3681d1707f
        <td>[1, 2, 3]
        <td>True
        <td>520
    </tr>
</table>
<br>

<h2>Cart Table:</h2>
Column Overview:

| Attribute             | Description                           |
| --------------------- | ------------------------------------- |
| ID                    | `Primary Key`                         |
| Items                 | `Foreign Key` Linking `Quantity` Table|

<table>
    Table Overview:
    <tr>
        <th>ID
        <th>Items
    </tr>
    <tr>
        <td>Integer
        <td>List[Quantity Foreign Key]
    </tr>
    <tr>
        <td>1
        <td>[1]
    </tr>
    <tr>
        <td>2
        <td>[2, 3]
    </tr>
    <tr>
        <td>3
        <td>[3]
    </tr>
</table>
<br>

<h2>Quantity Table:</h2>
Column Overview:

| Attribute             | Description                           |
| --------------------- | ------------------------------------- |
| ID                    | `Primary Key`                         |
| Item_ID               | `Foreign Key` Linking `Item` Table   |
| Quantity              | Stores number of Items                |

<table>
    Table Overview:
    <tr>
        <th>ID
        <th>Item_ID[Item Foreign Key]
        <th>Quantity
    </tr>
    <tr>
        <td>Integer
        <td>Integer
        <td>Integer Default 1
    </tr>
    <tr>
        <td>1
        <td>1 [Dish1]
        <td>1
    </tr>
    <tr>
        <td>2
        <td>2 [Dish2]
        <td>1
    </tr>
    <tr>
        <td>3
        <td>3 [Dish3]
        <td>2
    </tr>
</table>
<br>

<h2>Item Table:</h2>
Column Overview:

| Attribute             | Description                           |
| --------------------- | ------------------------------------- |
| ID                    | `Primary Key`                         |
| Name                  | Item Name                             |
| Description           | Short Descrition/Ingredients Used     |
| Image_Path            | Stores the Path to Item Image         |
| Ratings               | Ratings of customer for current item  |
| Price                 | Cost of current item                  |
| Ordered               | Stores number of times the Item is Ordered|

<table>
    Table Overview:
    <tr>
        <th>ID
        <th>Name
        <th>Description
        <th>Image_Path
        <th>Ratings
        <th>Price
        <th>Ordered
    </tr>
    <tr>
        <td>Integer
        <td>String
        <td>String
        <td>String
        <td>Float
        <td>Float
        <td>Integer
    </tr>
    <tr>
        <td>1
        <td>Dish1
        <td>Tasty
        <td>`~/app/public/1.png`
        <td>4.0
        <td>149
        <td>0
    </tr>
    <tr>
        <td>2
        <td>Dish2
        <td>Vary Tasty
        <td>`~/app/public/2.png`
        <td>4.2
        <td>50
        <td>0
    </tr>
    <tr>
        <td>3
        <td>Dish3
        <td>Sweet Dish
        <td>`~/app/public/3.png`
        <td>4.1
        <td>20
        <td>0
    </tr>
</table>
<br>

<h2>Category Table:</h2>
Column Overview:

| Attribute             | Description                           |
| --------------------- | ------------------------------------- |
| Name                  | Item Name                             |
| Description           | Short Descrition                      |
| Image_Path            | Stores the Path to Category Image     |
| Item_ID               | `Foreign Key` Linking `Item` table    |

<table>
    Table Overview:
    <tr>
        <th>Name
        <th>Description
        <th>Image Path
        <th>Item_ID[Item Foreign Key]
    </tr>
    <tr>
        <td>String
        <td>String
        <td>String
        <td>List
    </tr>
    <tr>
        <td>Starters
        <td>First course of your meal
        <td>`~/app/public/starters.png`
        <td>[1]
    </tr>
    <tr>
        <td>Main Course
        <td>Fill your stomach fully
        <td>`~/app/public/main_course.png`
        <td>[2]
    </tr>
    <tr>
        <td>Desert
        <td>Final taste/Digestion
        <td>`~/app/public/desert.png`
        <td>[3]
    </tr>
</table>
<br>

# Admin Interface

# Pages
* Dashboard/Menu:  
`localhost:port/menu/`
* Individual Category  
`localhost:port/menu/$name`
* Individual Item  
`localhost:port/menu/$name/$id`
* Orders:  
<i>@requires_authentication</i>  
`localhost:port/order/`
* Login Page [Optional]  
`localhost:port/login/`

# Summary
We will be using Python Django Framework as the base for the website which will include HTML, CSS and JavaScript Languages as well. For the Database we have Django Models which provides an abstraction for SQLite3. 
For communication between frontend and backend, REST API will be used.


# Challenges

# Experience
