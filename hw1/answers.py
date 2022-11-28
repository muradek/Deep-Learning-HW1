r"""
Use this module to write your answers to the questions in the notebook.

Note: Inside the answer strings you can use Markdown format and also LaTeX
math (delimited with $$).
"""

# ==============
# Part 1 answers

part1_q1 = r"""
**Your answer:**
1. False. 
in-sample error is the error rate we get on the same data set we used to build our predictor.
the dataset is a subset of the dataset that was not used to build the model, hence it estimates the out of sample error. 

2. False.
for example, given a data with two labels (dogs and cats), we can split the data to two disjoint subsets where each 
subset has samples of a specific label (i.e train set = all samples labeled cats, test set = all samples labeled dogs).  
As each sample is uniquely labeled, those are disjoint subsets. the model would probably label everything as cats unlike
a model based on subsets that consist of samples with label distribution which is equal to the data set distribution. 

3. True. 
This question is ambiguous as the definitions of "test set" and "using" vary in different sources.
To answer clearly, we'll first present our terminology:
In CV we first allocate a subset of the dataset to be test set. We then use cross validation on the *rest of the dataset
(*excluding the test set). At this part we name the new subsets "training set" and "validation set". 
So, in the training process of the CV routine, we repeatedly use different training and validation sets, but not the 
test set. Finally, after the training process we use the test set to estimate our models out os sample error. 

4. False.
Following the logic and terminology presented above, the test set is used to estimate our generalization error.  

Write your answer using **markdown** and $\LaTeX$:
```python
# A code block
a = 2
```
An equation: $e^{i\pi} -1 = 0$

"""

part1_q2 = r"""
**Your answer:**
His approach of adding an L2 regularization term to the loss function is justified as it minimizes chances of 
overfitting model due to overinflated weights. However, as a hyperparameter, the regularization rate \lambda should not
be determined by the test set, but optimized by the training process based on the training and validation set.

Write your answer using **markdown** and $\LaTeX$:
```python
# A code block
a = 2
```
An equation: $e^{i\pi} -1 = 0$

"""

# ==============
# Part 2 answers

part2_q1 = r"""
**Your answer:**
In our model, increasing the values of k does not improve generalization for unseen data. 
In our model, k=1 mostly had the highest accuracy, followed by k=3 that somtimes even slightly surpassed k=1.  
We assume that theres high variability of the samples representations, such that for a test sample, 
it is likely to find a training sample that is very close (low l2 dist), so for k=1 we'll get a more accurate decision.
But, the larger k we use, we get more false labels in our top-k (since the l2 dist between wrong labels with similar 
representation is close to that of a right label with "far" representation), which leads to lower accuracy.

Write your answer using **markdown** and $\LaTeX$:
```python
# A code block
a = 2
```
An equation: $e^{i\pi} -1 = 0$

"""

part2_q2 = r"""
**Your answer:**
1. k-fold CV is better than Training on the entire train-set with various models and selecting the best model w.r.t 
train-set accuracy in the *sense of model's ability to generalize its performance to an unseen data*. In a more 
"extreme" manner, in the CV method we decrease the chances of overfitting compared to the suggested method.    

2. In this case, the suggested method is again increasing the risk of overfitting, just this time it iss overfitting
to the test set. In a sense, thie means our model will underfit to the training set. Usually this will lead
to a "bad" model as the training set is usually bigger and "better distributed" than the test set.   


Write your answer using **markdown** and $\LaTeX$:
```python
# A code block
a = 2
```
An equation: $e^{i\pi} -1 = 0$

"""

# ==============

# ==============
# Part 3 answers

part3_q1 = r"""
**Your answer:**


Write your answer using **markdown** and $\LaTeX$:
```python
# A code block
a = 2
```
An equation: $e^{i\pi} -1 = 0$

"""

part3_q2 = r"""
**Your answer:**


Write your answer using **markdown** and $\LaTeX$:
```python
# A code block
a = 2
```
An equation: $e^{i\pi} -1 = 0$

"""

part3_q3 = r"""
**Your answer:**


Write your answer using **markdown** and $\LaTeX$:
```python
# A code block
a = 2
```
An equation: $e^{i\pi} -1 = 0$

"""

# ==============

# ==============
# Part 4 answers

part4_q1 = r"""
**Your answer:**


Write your answer using **markdown** and $\LaTeX$:
```python
# A code block
a = 2
```
An equation: $e^{i\pi} -1 = 0$

"""

part4_q2 = r"""
**Your answer:**


Write your answer using **markdown** and $\LaTeX$:
```python
# A code block
a = 2
```
An equation: $e^{i\pi} -1 = 0$

"""

part4_q3 = r"""
**Your answer:**


Write your answer using **markdown** and $\LaTeX$:
```python
# A code block
a = 2
```
An equation: $e^{i\pi} -1 = 0$

"""

# ==============
