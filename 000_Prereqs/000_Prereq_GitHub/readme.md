Github being pissy and you want to overwrite? : ```git push origin --force``` then do regular push


# Setting up GitHub for projects



#### Install Git

```sudo apt-get update```
```sudo apt-get upgrade```
```sudo apt install git```

```bash
git config --global user.name "ill13"
git config --global user.email ill13@ill13.com
git commit -m "updated readme"
```

https://itslinuxfoss.com/install-configure-git-ubuntu-22-04/
https://www.thiscodeworks.com/install-gh-cli-linux-installation-linux-bash-wsl-github-cli/61fb00eab783be0015bbafb2

##### Install gh in WSL

```bash
#!/usr/bin/env bash
# install github-cli
VERSION=`curl  "https://api.github.com/repos/cli/cli/releases/latest" | grep '"tag_name"' | sed -E 's/.*"([^"]+)".*/\1/' | cut -c2-`
echo $VERSION
mkdir ~/downloads
curl -sSL https://github.com/cli/cli/releases/download/v${VERSION}/gh_${VERSION}_linux_amd64.tar.gz -o ~/downloads/gh_${VERSION}_linux_amd64.tar.gz
cd ~/downloads
tar xvf gh_${VERSION}_linux_amd64.tar.gz
sudo cp gh_${VERSION}_linux_amd64/bin/gh /usr/local/bin/
gh version
sudo cp -r ~/downloads/gh_${VERSION}_linux_amd64/share/man/man1/* /usr/share/man/man1/
# man gh
gh auth login
rm -r ~/downloads
```
#### Push to git

From *home folder* ```nano .bashrc``` and add this

```bash
### SAFER LAZY GIT
function ptg() {
  git add .
  if git commit -a -m "$1"; then
    read -r -p "Are you sure you want to push these changes? [y/N]} " response
    case "$response" in
      [yY][eE][sS]|[yY])
        git push
        ;;
      *)
        git reset HEAD~1 --soft
        echo "Reverted changes."
        ;;
    esac
  fi
}
```