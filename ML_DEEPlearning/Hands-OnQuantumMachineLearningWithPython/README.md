## Prerequisites

The prerequisites of this course are as follows:

* We’ll cover some mathematics and physics, and walk through all the concepts that we will need. While this includes some mathematical notation and formulae, we’ll keep it at the minimum required to solve our practical problems.

* The theoretical foundation of quantum machine learning may appear overwhelming at first sight. But be assured that it is not harder than learning a new programming language when put into the proper context and explained conceptually.

* We’ll be writing a lot of code. Knowing Python is helpful for this course. However, if you don’t know Python, another language, such as Java, JavaScript, or PHP will be fine, too. If you know programming concepts, such as if-then-else-constructs and loops, then learning the syntax will be a piece of cake.

* If you’re familiar with functional programming constructs, such as map, filter, and reduce, you’re already well equipped. If not, don’t worry. We’ll get you started with these constructs, too. We don’t expect you to be a senior software developer. We’ll go through all the source code,line by line.

* By the time you finish the first few chapters of this course, you will be proficient with mathematics, understanding physics, and writing the code.

* This course is not just for beginners. There’s a lot of advanced content in here, too. Many chapters cover, explain, and apply quantum machine learning algorithms developed in the last two years. You can directly apply the insights this course provides to your job and research.


# Quantum Machine Learning—Beyond The Hype

### What is quantum machine learning?

Quantum machine learning is the use of quantum computing for the computation of machine learning algorithms.

There are many portrayals on these two technologies. They start with machines that understand the natural language of humans, and end with a utopia or dystopia, depending on the media. Don’t fall for the hype! An unbiased and detailed look at a technology helps us steer clear of any misunderstandings that surround it. Let’s start with machine learning.

### What is machine learning?

According to Cassie Kozyrkov, Chief Decision Scientist at Google, “Machine learning is a thing-enabler, essentially.”

With machine learning, the aim is to put a label onto an unlabeled thing. There are three main ways of doing this: classification, regression, and segmentation.

### Classification

In classification, we try to predict the discrete label of an instance. Given the input and a set of possible labels, we try to guess which one it is. Here’s a picture. Is it a cat or a dog?

### Regression

Regression is about finding a function to predict the relationship between input and dependent continuous output values.
For example, given that we know our friends’ income and the effective tax rates, can we estimate the tax rate given our income, even though we don’t know the actual calculation?

### Segmentation

Segmentation is the process of partitioning the population into groups with similar characteristics, which are likely to exhibit similar behavior. Given that we produce an expensive product, such as yachts, and a population of potential customers, who do we want to try to sell to?

# Quantum Computing

### Superposition

Superposition refers to the quantum phenomenon where a quantum system can exist in multiple states concurrently.

> The quantum system does not exist in multiple states concurrently. It exists in a complex linear combination of a state, 0, and a state, 1. It is a different kind of combination that is neither “or” nor “and.” We will explore this state in-depth in this course.

### Interference

Quantum interference is what allows us to bias quantum systems toward the desired state. The idea is to create a pattern of interference where the paths leading to wrong answers interfere destructively and cancel out, but the paths leading to the correct answer reinforce each other.

### Entanglement

Entanglement is a robust correlation between quantum particles. Entangled particles remain perfectly correlated even if they are separated by great distances.

# The Case for Quantum Machine Learning

## Classical machine learning algorithm

We’ve learned that machine learning algorithms contain three components: representation, evaluation, and optimization.

* When we look at the representation, current machine learning algorithms such as the GPT-3 network, published in 2020, come to mind. GPT-3 produces human-like text, but it has 175 billion parameters. In comparison, the IBM Q quantum computer has 27 quantum bits only. So even though quantum bits store a lot more information than a classical bit, since it is not 0 or 1, quantum computers are far from advancing machine learning for their representation ability.

* During the evaluation, the machine learning algorithm tries to predict the label of a thing. Classically, this involves measuring and transforming data points. For instance, neural networks rely on matrix multiplications. These are tasks classical computers are good at. However, if we have 175 billion parameters, calculating the resulting prediction takes many matrix multiplications.

* Finally, the algorithm needs to improve the parameters in a meaningful way. The problem is to find a set of parameter values that result in better performance. With 175 billion parameters, the number of combinations is endless.

> Classical machine learning employs heuristics that exploit the structure of the problem to converge to an acceptable solution within a reasonable time. However, despite advanced heuristics, training the GPT-3 would require 355 years on a single GPU, and cost $4.6 million.
