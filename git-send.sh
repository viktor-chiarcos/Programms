echo "Add all files..."
echo "Status:"
echo
git add *
echo ""
echo "Commit the update..."
echo "Status:"
echo
git commit -a -m "update on "$HOSTNAME" from "$USER" in git-send"
echo ""
echo "Update all files..."
echo "Status:"
echo
git pull
echo ""
echo "Please search your password."
echo "then say exit"
bash
echo ""
echo "Send on your git-repository..."
echo "Status:"
echo
git push
echo ""
echo "all commits:"
echo ""
git log
echo ""