commit_message=${1}
time_travel_days=${2:-0}
submodule_name=${3:-0}

# current date minus time_travel_days
commit_date=$(date -d "$date - $time_travel_days days")
echo Commit as $commit_date

# if change is inside submodule 
if [ $# -eq 3 ]; then
    cd $submodule_name
    git add .
    GIT_COMMITTER_DATE="$commit_date" git commit --date "$commit_date" -m "$commit_message"
    git push origin main
    cd ../
fi

git add .
GIT_COMMITTER_DATE="$commit_date" git commit --date "$commit_date" -m "$commit_message"
git push origin main

