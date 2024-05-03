from pyflowchart import Flowchart
with open('test.py') as t:
    code= t.read()

tc = Flowchart.from_code(code)
print(tc.flowchart())