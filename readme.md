# A tutorial on using Python with a newer style of webdev [versus LAMP ]


### To work on this project locally, 

- ```wsl``` Fire up *WSL* from a command line
- ```cd ~``` Navigate to *home*. You can store this repo wherever you want, I use *~/code/*
- ```gh repo clone ill13/web_project``` Clone this repo to your home folder
- ```code .``` To open VS Code with this project loaded


### Github Quick Reference
- ```ptg "things I did"``` to push to github [ptg]: See the *Push to GitHub* in *01_Prereqs/Prereq_GitHub/readme.md*
- Github being pissy and you want to overwrite? : ```git push origin --force``` then do regular push like ```ptg "stuff"```

### *venv*: Virtual Environment Quick Reference
- ```python -m venv venv``` Once that completes you can use ```source venv/bin/activate``` to start it.
- When you are done with *venv* and you'd like to exit the virtual environment, just type ```deactivate``` to exit. 
- Note: Don't forget to create a *.gitignore* and add the *venv/* folder so Github doesn't get full of stuff

