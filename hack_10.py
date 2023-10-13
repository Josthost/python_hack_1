"""
text: "fooziman" output => ["F","0","0","Z","1","M","@","N"]
"""

def fn_hack_10():
    result = "fooziman"
    #...

    result = result.upper()

    result = result.replace("O","0").replace("I","1").replace("A","@")

    result = result[0].split()+result[1].split()+result[2].split()+result[3].split()+result[4].split()+result[5].split()+result[6].split()+result[7].split()


    return result  