def convert(text):
  
  
    text = text.replace("happy :)", "🙂")
    text = text.replace(" sad :(", "🙁")
    return text

def main():
    user_input = input("Enter text with emoticons: ")
    converted = convert(user_input)
    print(converted)


main()
