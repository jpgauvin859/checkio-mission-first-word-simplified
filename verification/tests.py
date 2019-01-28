"""
TESTS is a dict with all of your tests.
Keys for this will be the categories' names.
Each test is a dict with
    "input" -- input data for a user function
    "answer" -- your right answer
    "explanation" -- not necessarily a key, it's used for an additional info in animation.
"""


TESTS = {
    "Basics": [
        {
            "input": "Hello world",
            "answer": "Hello"
        },
        {
            "input": "a word",
            "answer": "a"
        },
        {
            "input": "hi",
            "answer": "hi",
            "explanation": "text consists of only one word"
        }
    ],
    "Extra": [
        {
            "input": "Holy Edison",
            "answer": "Holy"
        }
    ]
}
