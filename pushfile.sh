#!/usr/bin/env bash




comment="Auto pushing any new file to GitHub"

git add .
git commit -m "$comment"

git push origin main


