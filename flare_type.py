import re

status_log_path = 'https://help.datadoghq.com/attachments/token/5bPyRk1nbAbWB1X9m4NLYhXYc/?name=datadog-agent-2023-08-16T22-21-37Z-info.zip'

# Extract the last part of the URL
split_log_path = status_log_path.split('=')[-1]

"""
Extract the status from the file name using regular expression. This also checks if a match was found using the regular expression search. If a match was found, it accesses the second captured group (the status) using match.group(2), converts it to title case using .capitalize(), and assigns it to the status variable. Then, it prints the status. If no match was found, it prints an error message.
"""

match = re.search(r'(.+)-(\w+)\.zip', split_log_path)
if match:
    status = match.group(2).capitalize()
    print(status)
else:
    print("Unable to extract status information from the URL.")
