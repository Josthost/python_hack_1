"""
text: "fooziman" output => "foozimaN"
"""

def fn_hack_4():
    result = "fooziman"
    #...

    result = result[0:7] + result[-1].upper()

    return result