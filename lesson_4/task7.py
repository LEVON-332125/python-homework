# *Define a collection of programming languages (names), add new language name from console if it’s not C#
languages=['html','jawa','python']
# languages.append(input())
language=input()
if language!='C#':
    languages.append(language)
    print(languages)