"""

### Input: List[Message]
## class Message:
##   content: Union[str, List[Union[str, Dict[str, str]]]]
## Content e.g ->
"saigeeth", [saigeeth], [{"foo": "bar"}], [{"foo1": "bar1"}, {"foo2": "bar2"}], ["saigeeth", {"foo1": "bar1"}]

"saigeeth",        -->                    "SAIGEETH"
["saigeeth"],      -->                    ["SAIGEETH"]
["saigeeth", "vamsee"],      -->          ["SAIGEETH", "VAMSEE"]
[{"foo": "bar"}],  -->                    [{"foo": "BAR"}]
[{"foo1": "bar1"}, {"foo2": "bar2"}], --> [{"foo1": "BAR1"}, {"foo2": "BAR2"}]
["saigeeth", {"foo1": "bar1"}]  -->       ["SAIGEETH", {"foo1": "BAR1"}]


#class Message:
    content: Union[str, List[Union[str, Dict[str, str]]]]

def upper_func(input: List[Message]):

    Given a list of type "Message", I wanted to return a list of type "Message"
    with plain strings in uppercase and dictionary values in uppercase.

   #:param input:
    #:return:
"""
from typing import List, Union, Dict

class Message:
    def __init__(self, content: Union[str, List[Union[str, Dict[str, str]]]]):
        self.content = content

def convert_to_upper(messages: List[Message]) -> List[Message]:
    def recursive_convert(content):
        if isinstance(content, str):
            return content.upper()
        elif isinstance(content, dict):
            return {key: value.upper() for key, value in content()}
        elif isinstance(content, list):
            return [recursive_convert(sub_content) for sub_content in content]
        else:
            return content

    return [Message(recursive_convert(message.content)) for message in messages]