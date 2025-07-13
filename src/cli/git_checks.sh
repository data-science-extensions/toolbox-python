export git_tag="v1.3.2"
git log --oneline $git_tag..HEAD > git_output/git_1.txt
git log --stat $git_tag..HEAD > git_output/git_2.txt
git log --oneline --graph --decorate $git_tag..HEAD > git_output/git_3.txt
git log --oneline --tags $git_tag..HEAD > git_output/git_4.txt
git log $git_tag..HEAD > git_output/git_5.txt
git diff --name-only $git_tag..HEAD > git_output/git_6.txt
git diff $git_tag..HEAD > git_output/git_7.txt
git rev-list --count $git_tag..HEAD > git_output/git_8.txt
git tag --list > git_output/git_9.txt
git show --format=fuller $git_tag > git_output/git_10.txt
