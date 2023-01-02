def setValue(question: str) -> str:
    return input("Bot: " + question + "\n==> ")

def printChat(string: str) -> None:
    print("Bot: " + string)

def printYesNo(question: str) -> bool:
    ans = None
    while(ans==None):
        in_value = setValue(question + " (Lựa chọn)\
                            \n1. Có \
                            \n2. Không")
        match in_value:
            case '1':
                ans=True
            case '2':
                ans=False
            case _:
                printChat("Lựa chọn không có, vui lòng nhập lại!")
    return ans