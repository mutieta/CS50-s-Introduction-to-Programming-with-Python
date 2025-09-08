vowel = ["a", "e", "i", "o", "u"]

def main():
    input_text = input("Input: ")
    output_text = (input_text)
    for char in output_text:
        if char.lower() in vowel:
            output_text = output_text.replace(char, "")
    print("Output:", output_text)
main()