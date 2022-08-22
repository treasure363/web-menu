# Project Description
# Language
# Tech Stack
# Working
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
