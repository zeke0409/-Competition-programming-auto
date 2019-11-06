import sys
import webbrowser
import pyperclip
#webbrowser.open("http://google.com/")
#print("hello")
args = sys.argv

if len(sys.argv) > 1:
    number = args[1]
else:
    number = pyperclip.paste()

#print(address)
webbrowser.open("https://atcoder.jp/contests/"+number+"/tasks/"+number+"_a")
webbrowser.open("https://atcoder.jp/contests/"+number+"/tasks/"+number+"_b")
webbrowser.open("https://atcoder.jp/contests/"+number+"/tasks/"+number+"_c")
webbrowser.open("https://atcoder.jp/contests/" +
                number + "/tasks/" + number + "_d")
webbrowser.open("https://atcoder.jp/contests/" +
                number + "/tasks/" + number + "_e")
