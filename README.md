# RecipeAllocation

## Contents

1. [Introduction](#introduction)
2. [Algorithm](#algorithm)
3. [Project Structure](#project structure)
4. [How To Run](#how to run)


### Introduction

The project contains the implementation of recipe allocation algorithms for the default orders. It return a **Boolean** value representing if the constraints imposed are satisfied or not.

### Algorithm

There are two different algorithms implemented for the pipeline.
  
  1. Greedy Allocation: Utilizes the recipes for which the stock is maximum
  2. GCD Allcoation: The idea is similar to the previous however, instead of iterating over a single order, we iterate over a mini-batch of orders.
  
 ### Project Structure
 
    .
    ├── data                   # JSON files
    ├── source                 # Implementation of classes such as Recipes, Allocator etc.
    ├── utility                # Utility functions which can be used across the app
    └── README.md
  
### How To Run

##### Setting up the docker


##### Executing the application

Make sure the `JSON` files are placed in the `data` folder
**execution**
`python --o orders.json --s stock.json main.py`

**p.s** Prints the boolean value representing if the constraints in the problems are met or not. **True** for constraints being satisfied
**False** otherwise
