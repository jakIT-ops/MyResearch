# 1. Introduction to Linear Programming and Optimization

### How to formulate a linear programming problem

In order to formulate any real-world problem into a linear programming problem, we need to perform the following steps:

1. Identify all the decision variables, or the different parameters of the problem.

2. Write the objective function, or the attribute we want to maximize or minimize.

3. Mention the constraints, or the limitation of resources that should be kept in mind.

All of these have to be linear functions in order to solve them using linear programming.

### Example of formulating a linear programming problem

Suppose Abacus Inc. is a computer manufacturing company. The company only manufactures two types of computers. One is a high-performance computer targeted for business entities, and the other is an affordable one with an average performance targeted for the everyday consumer. Let’s call these two types of computers Unity-Pro (UP) and Unity-Nor (UN). We assume the assembly of each type of computer requires only two parts, that is, part A and part B. The requirements for each unit are:

* One UP computer requires 2 units of part A and 3 units of part B.

* One UN computer requires 1 unit of part A and 2 units of part B.

Now the company needs to make a decision in order to maximize its profit in the current quarter. The problem is how many different UP and UN units it should produce with the current stock limitation. It has 1,000 units of part A and 1,300 units of part B. Every single UP unit sold results in a profit of $200, while each UN unit results in a profit of $100.

# 2. Real-life Examples of Linear Programming in Python

### Food and agriculture

Those who work in agriculture have the enormous responsibility to meet the food requirements of the population. Therefore, a natural constraint exists between the supply and demand of food. In agriculture, linear programming is employed to make smart decisions about the expenditure and distribution of resources.

* Maximizing crop yields

Linear programming is used to maximize the yield of crops by taking into consideration different constraints, such as nutrient concentration, demand for the crop, and its profitability.

* Food distribution

Linear programming is used to optimize the distribution of food to different regions. Multiple factors like the food’s shelf life, transportation cost, and demand for the product serve as the constraining variable for the optimization problem.

* Diet plan

Linear programming is used by nutritionists to optimize the calorie intake for a healthy and balanced diet.

### Business and finance

Linear programming is extensively used by business managers and financial analysts to set up the budget, optimize expenditures, and maximize profits. Business-minded employees particularly need it for the management of assets and profits, production, and transportation. On the other hand, financiers use it for scheduling payments and funds transfers, as well as optimizing a mix of financial products such as investments, debits, or credits.

### Engineering and technology

Engineers usually have to work with a limited set of resources and time to complete their projects. That’s why they need to ensure the best possible quality of their project under the given constraints.

* Biomedical engineers need to find the optimal amount of resources (batch size, quantity of enzymes, and time of reaction) to maximize the profits of the product.

* The triple constraints of project management (resources, scope, cost) bind engineering projects. All the problem variables like budget and time act as problem variables and need to be optimized to maximize the quality of the project.

* In designing power systems, especially hybrid systems having multiple power sources (such as hydraulic, wind, or solar), electrical engineers need to optimize the demand for each of the power sources.


## Introduction to PuLP

PuLP is a free, open-source library that solves optimization problems computationally. To use PuLP for this purpose, we first need to create a mathematical model of an optimization problem that includes the optimization variables and constraints. Then, we use an optimizer to solve the linear programming problems. You may sometimes hear this called LP optimization. Any of the external linear programming solvers like CBC, GLPK, CPLEX, Gurobi, and others can be used in this way. The solver updates the optimization variables to their optimal value.


## Configuring and importing PuLP

PuLP can be configured and imported by executing the following commands:

```py
pip install pulp
from pulp import *
```

## Solvers In PuLP

Currently, the PuLP library has the following optimizers for solving LP problems:

* CBC                 

* GLPK              

* CLP

* CPLEX

* Gurobi    

* MOSEK

* FICO XPRESS

* Choco SolverMIPCL

* SICP
