## this for school management system tutorial from Django Mastery you tube channel

### In command prompt
> mkdir sms

> cd sms

> python -m venv .smsenv (but I wasn't used **python**, used **py**)

> code . (to open in vscode shortcut)

> source .smsenv/Scripts/activate (but I used **.smsenv/Script/activate**)

> pip install django

### Notes
* Some time I want to used html comment in VSCode like <!-- --> this when I press ctrl+/ but VSCode was prompted {% comment %}  {% endcomment %}, So I change custom user snippet as following: *
If you don't want to disable/uninstall any plugin, you can create a snippet to put a comment. For example, I create a snippet that add HTML comments:

    "comment HTML": {
      "prefix": "chtml",
      "body": ["<!-- $1 -->"],
      "description": "Comment HTML line"
    }
You can insert that right after the comment in File > Preferences > User Snippets > {YourExtension}

Then, when you start typing 'chtml' in that kind of files, IntelliSense will prompt that snippet.

Maybe this is a workarround, but it works excellent for me. Hope it helps!

https://code.visualstudio.com/docs/customization/userdefinedsnippets