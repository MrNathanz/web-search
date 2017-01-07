import webbrowser
import sys

searchEngines = ["google", "yahoo", "bing", "duckduckgo"]
question1 = "What search engine do you want to use?"
question2 = "You can choose between Google, Yahoo, Bing and DuckDuckGo."
engine_url = ""


def engine_decision():
    while True:
        print(question1)
        print (question2)
        engine_choice = input("> ").lower()
        if engine_choice in searchEngines:
            print("\nChoice accepted...")
            global engine_url
            if engine_choice.lower() == "google":
                engine_url = "https://www.google.nl/?gws_rd=ssl#q="
                break
            elif engine_choice.lower() == "yahoo":
                engine_url = "https://search.yahoo.com/search;_ylc=X3oDMTFiN25laTRvBF9TAzIwMjM1MzgwNzUEaXRjAzEEc2VjA3NyY2hfcWEEc2xrA3NyY2h3ZWI-?p="
                break
            elif engine_choice.lower() == "bing":
                engine_url = "https://www.bing.com/search?q="
                break
            elif engine_choice.lower() == "duckduckgo":
                engine_url = "https://duckduckgo.com/?q="
                break
        else:
            print("Error... Please retry.\n")
    search()


def search():
    while True:
        print("\nWhat do you want to search the web for?")
        web_request = input("> ").replace(" ", "+")
        search_url = engine_url + web_request
        print("\nAccessing the web with the following URL:\n" + search_url + "\n")
        webbrowser.open(search_url)
        while True:
            print("Do you want to search the web for something else? (Y/N)")
            again = input("> ")
            if again.lower() == "yes" or again.lower() == "y":
                break
            elif again.lower() == "no" or again.lower() == "n":
                while True:
                    print("Are you sure? The program will close if you are. (Y/N)")
                    sure = input("> ")
                    if sure.lower() == "yes" or sure.lower() == "y":
                        sys.exit()
                    elif sure.lower() == "no" or sure.lower() == "n":
                        break
                    else:
                        print("Error... Please retry.\n")
            else:
                print("Error... Please retry.\n")

if __name__ == '__main__':
    engine_decision()
