prompt_a = """
I am a marketing manager at a retail company and we have just finished
a three-month campaign. My team has collected customer feedback through
an online survey and we now have about 500 responses stored in a
spreadsheet. Each response includes the customer's age group, the
product they purchased, their satisfaction rating from 1 to 5, and a
short written comment. I need to present the findings to our CEO next
Friday in a way that is easy to understand. Can you analyse this data
for me, highlight which age groups and products have the lowest
satisfaction scores, identify the most common complaints from the
written comments, and summarise everything in a short paragraph I can
use as an executive summary?
"""

prompt_b = """
Role: You are a data analyst helping a retail marketing team.
Task: Analyse customer survey data from a 3-month campaign.
Data: 500 responses containing age group, product purchased,
satisfaction rating (1-5), and written comments.
Steps:
1. Identify age groups and products with the lowest satisfaction scores.
2. Extract the most common themes from the written comments.
3. Summarise findings in an executive summary paragraph.
Audience: CEO presentation on Friday.
Constraints: Keep the summary concise and free of technical jargon.
"""


# Task 1
# Read both prompts above carefully, then answer the questions below as comments.

# Q8a: Which prompt do you think will get a better response from an AI?
# Your answer: Prompt B.

# Q8b: Give TWO reasons to support your choice.
# Your answer (Reason 1): Prompt B is clearly structured into labelled sections
# (Role, Task, Data, Steps, Audience, Constraints), which removes ambiguity and
# gives the AI a numbered sequence of steps to follow, so no requirement gets
# buried or overlooked the way it can be in a long conversational paragraph.
# Your answer (Reason 2): Prompt B assigns an explicit role ("data analyst")
# and states explicit constraints ("concise and free of technical jargon"),
# which steers both the perspective and the tone of the output, making the
# response more likely to match what the CEO audience actually needs.

# Q8c: What is ONE strength of the prompt you did NOT choose?
# Your answer: Prompt A provides richer real-world context — who the requester
# is (a marketing manager), why the analysis matters (a CEO presentation next
# Friday), and how the output will be used — which helps the AI judge the
# purpose and stakes behind the request, not just the mechanical steps.


# Task 2
# Rewrite either prompt by borrowing ONE element from the other
# to make it stronger. Explain what you borrowed and why.
# Your answer: I rewrote Prompt B by borrowing the business context from
# Prompt A (who is asking and why the analysis is needed). The structured
# format of B stays intact, but the added "Context" line explains the purpose
# behind the request, helping the AI tailor its findings to a real business
# decision rather than treating the task as a generic exercise.

prompt_b_improved = """
Role: You are a data analyst helping a retail marketing team.
Context: The requester is a marketing manager whose team has just finished
a three-month campaign and must present the survey findings to the CEO
next Friday in a way that is easy to understand.
Task: Analyse customer survey data from a 3-month campaign.
Data: 500 responses containing age group, product purchased,
satisfaction rating (1-5), and written comments.
Steps:
1. Identify age groups and products with the lowest satisfaction scores.
2. Extract the most common themes from the written comments.
3. Summarise findings in an executive summary paragraph.
Audience: CEO presentation on Friday.
Constraints: Keep the summary concise and free of technical jargon.
"""
