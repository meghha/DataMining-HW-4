# Add import files
import pickle



# -----------------------------------------------------------
def question1():
    answers = {}

    # string "yes" or "no"
    answers["(a)"] = "no"
    answers["(b)"] = "no"
    answers["(c)"] = "yes"
    answers["(d)"] = "yes"

    # explain-string: explanation in english prose
    answers["(a) explain"] = "The rule set is not mutually exhaustive because the criterion should be that every instance must satisfy only one rule. If it meets the conditions of one rule, it cannot simultaneuosly satisfy another. An example is for the first rule it can classify a Homeowner as Default Borrower, whether the person has high annual income or not. However, if a record satisfies both first and fifth rule (Medium Annual Income and currently employed), then it will be Yes and No at the same time, which is not mutually exclusive"
    answers["(b) explain"] = "For a mutually exhaustive rule set, all the instances/records would be classified. However, in this case not all records may be satisfied" 
    answers["(c) explain"] = "Yes ordering would be necessary for the rules, as without ordering, rules may contradict each other for once instance. An example of this is rule 6 and rule 3, if they are not in order, the instance maybe misclassified."
    answers["(d) explain"] = "Yes, a default class is needed if there is an instance which does not satisfy any rule. In this case, there are instances which might not satisfy any of the rules. Example is rule 5, where if the annual income is medium and currently employed is No, then what is the DB value?"

    return answers


# -----------------------------------------------------------
"""
def question2():
    answers = {}

    # string "yes" or "no"
    answers["(a)"] = None
    answers["(b)"] = None
    answers["(c)"] = None
    answers["(d)"] = None

    # explain_string: explanation in english prose
    answers["(a) explain"] = None
    answers["(b) explain"] = None
    answers["(c) explain"] = None
    answers["(d) explain"] = None

    return answers
"""
# -----------------------------------------------------------
def question3():
    answers = {}

    # string "yes" or "no"
    answers["(a)"] = "no"
    answers["(b)"] = "no"
    answers["(c)"] = "yes"

    # explain-string: explanation in english prose
    answers["(a) example"] = "Rules are not mutually exclusive, when a record can satisfy more than one rule. In this example table, the record for Pigeon satisfies both R1 and R3"
    answers["(b) example"] = "Mutually exhaustive rules mean that all th records should satisy atleast one rule. In this table, the record for turtle does not satisfy any of the 4 rules"
    answers["(c) example"] = "Order is needed for the rules, as otherwise one record may get classified to more than one class, by satisfying more than one rule"

    return answers
# -----------------------------------------------------------
def question7():
    answers = {}

    # bool: True/False
    answers["(a)"] = True
    answers["(b)"] = True
    answers["(c)"] = False
    answers["(d)"] = True

    # explain_string: explanation in english prose
    answers["(a) explain"] = None
    answers["(b) explain"] = None
    answers["(c) explain"] = None
    answers["(d) explain"] = None

    return answers

# -----------------------------------------------------------
def question8():
    answers = {}

    # float
    answers["(a) P(X_1=1)"] = 0.65
    answers["(a) P(X_2=1)"] = 0.41
    answers["(a) P(X_1=1,X_2=1)"] = 0.28

    # string: "dependent" or "independent"
    answers["(a) Relationship between X_1 and X_2"] = "dependent"

    # string: "yes" or "no"
    answers["(b) X_1 and X_2 conditionally independent given the class?"] = "no"

    # float
    answers["(c) P(X_1=1 | +)"] = 0.8
    answers["(c) P(X_1=1 | -)"] = 0.5
    answers["(c) P(X_2=1 | +)"] = 0.5
    answers["(c) P(X_2=1 | -)"] = 0.32
    answers["(c) P(X_3=1 | +)"] = 0.4
    answers["(c) P(X_3=1 | -)"] = 0.16

    # For each row give the class predicted by the model after training using Naive Bayes
    # String: either '+' or '-'
    answers["(d) Row 1"] = "+
    answers["(d) Row 2"] = None
    answers["(d) Row 3"] = None
    answers["(d) Row 4"] = None

    # float between 0 and 1
    answers["(d) Training error rate"] = None

    return answers

# --------------------------------------------------------
def question9():
    answers = {}

    # int
    answers["(a) K"] = 5
    answers["(b) K"] = 50

    # explain_string
    answers["(a) explain"] = "A value of K = 5, is considered since the dataset has a very clear decision boundary. This means that any data point has a high probability of being in the class belonging to its closest neighbour. Therefore, taking a value of 5 strikes a balance between bias and variance, with the  that the data is correctly classified"
    answers["(b) explain"] = "Since, in the second case, the data points are overlapping quite a bit, taking a higher value of K will ensure that the boundary is smooth and there is no overfitting" 

    return answers

# --------------------------------------------------------
def question10():
    answers = {}

    # float
    answers["(a) P(A=1|+)"] = 0.6
    answers["(a) P(B=1|+)"] = 0.4
    answers["(a) P(C=1|+)"] = 0.8
    answers["(a) P(A=1|-)"] = 0.4
    answers["(a) P(B=1|-)"] = 0.4
    answers["(a) P(C=1|-)"] = 0.2

    # type: explanatory string
    answers["(a) P(A=1|+) explain your answer"] = "The conditional probability for P(A|B) is equal to the probability of A and B occuring together divided by the probability of B. In this case there are 3 instances where both A=1 with class = + occurs together, and a total of 5 + instances are there, hence the conditional probability is 3/5 which is 0.6"
  
    # type: float
    # note: R is the sample (A=1,B=1,C=1)
    answers["(b) P(+|R)"] = 0.96
    answers["(b) P(R|+)"] = 0.192
    answers["(b) P(R|-)"] = 0.032

    # string, '+' or '-'
    answers["(b) class label"] = "+"

    # explain_string
    answers["(b) Explain your reasoning"] = "Using the Naive Bayes approach, the value of P(R|+) and P(R|-) was computed. Since, the probability of P(R|+) is hg=igher, the predicted label is +."
  
    # float
    answers["(c) P(A=1)"] = 0.5
    answers["(c) P(B=1)"] = 0.4
    answers["(c) P(A=1,B=1)"] = 0.2

    # type: string, 'yes' or 'no'
    answers["(c) A independent of B?"] = "yes"
  
    # type: float
    answers["(d) P(A=1)"] = 0.5
    answers["(d) P(B=0)"] = 0.6
    answers["(d) P(A=1,B=0)"] = 0.3

    # type: string: 'yes' or 'no'
    answers["(d) A independent of B?"] = "yes"
  
    # type: float
    answers["(e) P(A=1,B=1|+)"] = 0.1
    answers["(e) P(A=1|+)"] = 0.6
    answers["(e) P(B=1|+)"] = 0.4

    # type: string: 'yes' or 'no'
    answers["(e) A independent of B given class +?"] = "no"

    # type: explanatory string
    answers["(e) A and B conditionally independent given class +, explain"] =  "Since, P(A=1,B=1|+) = 0.1, for A to be conditionally indepenedent of B given +, the product of P(A=1|+) and P(B=1|+) should be equal to 0.1. However, P(A=1|+) * P(B=1|+) = 0.6*0.4 = 0.24, which is not same as 0.1" 
  
    return answers
# --------------------------------------------------------
if __name__ == '__main__':
    answers_dict = {}
    answers_dict['question1'] = question1()
    answers_dict['question2'] = question2()
    answers_dict['question3'] = question3()
    answers_dict['question4'] = question4()
    answers_dict['question7'] = question7()
    answers_dict['question8'] = question8()
    answers_dict['question9'] = question9()
    answers_dict['question10'] = question10()

    with open('answers.pkl', 'wb') as f:
        pickle.dump(answers_dict, f)
