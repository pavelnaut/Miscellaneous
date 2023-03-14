commit_message=${1}
time_travel_days=${2:-0}
commit_submodule=${3:-css-exercises}

# current date minus time_travel_days
commit_date=$(date -d "$date - $time_travel_days days")
echo Commit as $commit_date
cd $commit_submodule
git add .
GIT_COMMITTER_DATE="$commit_date" git commit --date "$commit_date" -m "$commit_message"
git push origin main
cd ../
git add .
GIT_COMMITTER_DATE="$commit_date" git commit --date "$commit_date" -m "$commit_message"
git push origin main
