# Enter frontend dir
cd ../OnlineJudgeFE
# Download deps and build the frontend
yarn
if [ ! -e "${base}/build/vendor-manifest.json" ]
then
    yarn build:dll
fi 
yarn build
# Copy the dist dir to OnlineJudge
rm -rf ../OnlineJudge/dist
cp -rf ./dist ../OnlineJudge/dist
# Go back to the deploy dir
cd ../OnlineJudgeDeploy
# Build docker containers
sudo docker-compose build