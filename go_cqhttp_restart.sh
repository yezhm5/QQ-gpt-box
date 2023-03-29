cd go-cqhttp
for ip in `cat pid.list`
do
	{
		echo "kill -9 $ip"
		kill -9 $ip
	}
done
nohup ./go-cqhttp & echo $! >> pid.list
