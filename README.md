# RecipeAllocation

## Contents

1. [Introduction](#introduction)
2. [Algorithm](#algorithm)
3. [Project Structure](#project-structure)
4. [How To Run](#how-to-run)


### Introduction

The project contains the implementation of recipe allocation algorithms for the default orders. It return a **Boolean** value representing if the constraints imposed are satisfied or not.

### Algorithm

Greedy Allocation: Utilizes the recipes for which the stock is maximum. The detailed working is listed below

1. We create a *max-Priority* queue for recipes based on the stock
2. We create another *max-Priority* queue for orders based on the number of recipes required.
3. For each order with `k` required recipes we select the top `k` recipes in stock. 
4. We reduce the count by the number of portions required for the order and push it back in the queue
5. We reduce the order count by 1

**Time Complexity** `O(nlog(a)+nlog(b)), where n is the number of orders, m is the different recipes in stock, b is the different types of orders`

**Note** it is possible to bring the complexity down to `O(nlog(a))` by using a sorted list instead of a priority queue for orders. However, it is left as future work as the value of `b` is very small
 
 ### Project Structure
 
    .
    ├── data                   # JSON files
    ├── source                 # Implementation of classes such as Recipes, Allocator etc.
    ├── utility                # Utility functions which can be used across the app
    ├── Dockerfile             # Dockerfile containing the docker instructions to set up the environment
    └── README.md
  
### How To Run
In order to the project. We need to set up the docker which ensures the consistency of the project across platforms. After the docker is set up we utilize `python` to run the `main.py`

##### Setting up the docker
Firstly, navigate to the `$ROOT` of the project. The proejct structre at `$ROOT` is displayed above(#project-structure)
Execute the command
`docker built -t recipe_allocation .`
This builds the image. Next, we need to run the image
`docker run -it recipe_allocation`
This will cause the miniconda3 enivronment inside the terminal to change to `env`. We can now execute the code 

##### Executing the application

Make sure the `JSON` files are placed in the `data` folder
**execution**
`python -p ./data/ -o orders.json -s stock.json main.py`

**help**
`python -h main.py`

**p.s** Prints the boolean value representing if the constraints in the problems are met or not. **True** for constraints being satisfied
**False** otherwise
