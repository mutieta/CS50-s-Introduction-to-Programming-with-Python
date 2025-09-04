def main():
   response = input("Mood patrol: :) or :( ")
   response = convert(response)
   print(response)

def convert(txt):
   txt = txt.replace(":)","🙂").replace(":(","🙁")
   return(txt)

main()