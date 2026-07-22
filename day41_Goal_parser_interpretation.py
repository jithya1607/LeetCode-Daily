#41 Goal parser interpretation
# Given a string command, you need to return a string that interprets the command. The command consists of an alphabet of "G", "()", and/or "(al)" in some order. The interpreted result of "G" is "G", "()" is "o", and "(al)" is "al".
def interpret(self, command: str) -> str:
    b=''
    for i in range(len(command)):
        if command[i]=='G':
            b+='G'
        elif command[i]=='(':
            if command[i+1]==')':
                b+='o'
            else:
                b+='al'
        else:
            continue
    return b             