def clean(normal):
    cleaned_input = ''
    for x in normal:
        if x.isalpha():
            cleaned_input += x.lower()

    
    cleaned = ''
    for char in normal:
        if char.isalpha():
            cleaned += char.lower()
    
    reversed_string = cleaned[::-1]
    
    if reversed_string == cleaned_input:
        print(reversed_string, "is a Palindrome")
    else:
        print(reversed_string,"is not a Palindrome")
    
normal = input("give me a word!: ")
    
reverse = clean(normal)